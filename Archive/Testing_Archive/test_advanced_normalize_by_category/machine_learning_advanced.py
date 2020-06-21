import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder, PowerTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, explained_variance_score
import matplotlib.pyplot as plt
import time
##################################################################################################################
### File Download
##################################################################################################################
### Import file
chart = pd.read_csv('test_advanced.csv', sep=',')

### Select number of points to test
chart = chart

##################################################################################################################
### Preprocessing
##################################################################################################################


def create_identifiers(data):
	identifier_list = []

	gender = data['gender'].unique()
	ethnicity = data['ethnicity'].unique()



	for g in gender:
		for e in ethnicity:
			new_list = [g, e]
			identifier_list.append(new_list)

	return identifier_list
def split_data_by_identifier(data):
	identifier_list = create_identifiers(data)
	column_list = data.columns
	identifier_tuples = [(i[0], i[1]) for i in identifier_list]

	identifier_dictionary = {n:pd.DataFrame(columns = column_list) for n in identifier_tuples}

	for row in data.iterrows():
		ID_check = (row[1]['gender'], row[1]['ethnicity'])
		list_row = row[1].values.tolist()

		sample = identifier_dictionary[ID_check]
		sample = sample.append({n:l for n,l in zip(column_list,list_row)}, ignore_index = True)
		identifier_dictionary[ID_check] = sample

	return identifier_dictionary

def map_transform(list_data, min_goal, max_goal):
	i_min = min(list_data)
	i_max = max(list_data)
	slope = (max_goal - min_goal) / (i_max - i_min)
	transform = []
	for i in list_data:
		transform.append(min_goal + slope * (i - i_min))
	transform = [int(i) for i in transform]
	return transform

def normalize_by_category(data):
	ID_dict = split_data_by_identifier(data)
	for key, item in zip(ID_dict.keys(), ID_dict.values()):
		item = item[((item.success_score - item.success_score.mean()) / item.success_score.std()).abs() < 3]
		pt = PowerTransformer()
		pt.fit_transform(item[['success_score', 'income_bracket']])
		item['success_score'] = (item.success_score - item.success_score.mean())/item.success_score.std(ddof=0)
		item['success_score'] = map_transform(item['success_score'], 0, 10)
		ID_dict[key] = item
	chart = pd.concat(ID_dict.values())
	return chart

### Transforms non-numerical data to numerical classes
def transform_to_classes(data, parameter_list):
	for parameter in parameter_list:
		le = LabelEncoder()
		data[parameter] = le.fit_transform(data[parameter])
	return data



parameter_list = ['gender', 'ethnicity', 'sport', 'first_gen']
chart = transform_to_classes(chart, parameter_list)
identifier_dictionary_df = split_data_by_identifier(chart)
chart = normalize_by_category(chart)
X = chart.drop('success_score', axis=1)
#X = chart[['undergrad', 'lawschool']]
y = chart['success_score']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

##################################################################################################################
### Create learning objects
##################################################################################################################

### Learning object class
class learn:
	def __init__(self, name, lambda_code):
		self.name = name
		self.lambda_code = lambda_code
		self.prediction = False
		self.accuracy_score = 0
		self.classification_report = False
		self.confusion_matrix = False
		self.runtime = False
		self.one_off = []

Learn_Object_List = []

##################################################################################################################
### Random Forest Classifier
RandomForest = learn('RandomForestClassifier', RandomForestClassifier(n_estimators=20))
#n_estimators = how many forests

Learn_Object_List.append(RandomForest)

##################################################################################################################
### SVM Classifier
clf = learn('CLF', SVC())

Learn_Object_List.append(clf)

##################################################################################################################
### Neural Network
mlpc = learn('MLPC', MLPClassifier(hidden_layer_sizes = (7,7,7), max_iter=500))

Learn_Object_List.append(mlpc)

##################################################################################################################

### Fit curve and return prediction
def make_prediction(learn_object, X_train, y_train, X_test):
	start_time = time.time()
	y_train = y_train.astype(int)
	learn_object.lambda_code.fit(X_train, y_train)
	predict = learn_object.lambda_code.predict(X_test)
	learn_object.prediction = predict
	end_time = time.time() - start_time
	learn_object.runtime = end_time
	return learn_object

def one_off_score(y_true, y_pred):
	count = 0
	correct = 0
	one_off = 0
	for true, pred in zip(y_true, y_pred):
		if true == pred:
			correct+=1
		elif true == pred+1 or true == pred-1:
			one_off+=1
		count+=1
	one_off_adjusted = (correct + (one_off/2))/count
	one_off_full = (correct + one_off)/count
	return one_off_full, one_off_adjusted

### Runs analysis metrics
def analyze(learn_object, y_test):
	learn_object.accuracy_score = accuracy_score(y_test, learn_object.prediction)
	learn_object.one_off = one_off_score(y_test, learn_object.prediction)
	learn_object.classification_report = classification_report(y_test, learn_object.prediction)
	learn_object.confusion_matrix = confusion_matrix(y_test, learn_object.prediction)
	return learn_object


for t in Learn_Object_List:
	l = make_prediction(t, X_train, y_train, X_test)
	l = analyze(l, y_test)
	print(l.name,'\n', l.confusion_matrix, l.accuracy_score, l.one_off, '\n')
	sns.heatmap(l.confusion_matrix, annot=True)
	#sns.scatterplot(l.prediction, y_test)
	plt.show()


