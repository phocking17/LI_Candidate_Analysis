### Patrick Hocking
### 

import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import time
##################################################################################################################
### File Download
##################################################################################################################
### Import file
chart = pd.read_csv('test.csv', sep=',')

### Select number of points to test
chart = chart[:10000]

##################################################################################################################
### Preprocessing
##################################################################################################################




### Transforms binary (Success) back to non-binary
'''
bins = 2
group_names = ['Not Partner', 'Partner']
chart[' success?'] = pd.cut(chart[' success?'], bins= bins, labels = group_names)
'''




### Transforms non-numerical data to numerical classes
def transform_to_classes(data, parameter_list):
	for parameter in parameter_list:
		le = LabelEncoder()
		data[parameter] = le.fit_transform(data[parameter])
	return data

parameter_list = ['gender', ' ethnicity']

chart = transform_to_classes(chart, parameter_list)




### Print data counts
'''
print(chart[' success?'].value_counts())
'''



### Visualize successes
'''
sns.countplot(chart[' success?'])
plt.show()
'''



 
### Seperate Response and Feature variables
X = chart.drop(' success?', axis=1)
y = chart[' success?']



### Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)




### Apply Scaling
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
	learn_object.lambda_code.fit(X_train, y_train)
	predict = learn_object.lambda_code.predict(X_test)
	learn_object.prediction = predict
	end_time = time.time() - start_time
	learn_object.runtime = end_time
	return predict, learn_object

### Create reports
def create_reports(learn_object, y_test):
	learn_object.classification_report = classification_report(y_test, learn_object.prediction)
	learn_object.accuracy_score = accuracy_score(y_test, learn_object.prediction)
	learn_object.confusion_matrix = confusion_matrix(y_test,learn_object.prediction)
	return learn_object

### Create multiple reports
def create_multiple_reports(Learn_Object_List, X_train, y_train, X_test):
	new_item_list = []
	for item in Learn_Object_List:
		item = make_prediction(item, X_train, y_train, X_test)[1]
		item = create_reports(item, y_test)
		new_item_list.append(item)
	return new_item_list



### Summarize Results
def summarize_single(learn_object):
	print(learn_object.accuracy_score, ' accuracy score in ', learn_object.runtime)
	print('\n')
	print('\n')
	print('Classification Report')
	print('\n')
	print(learn_object.classification_report)
	print('\n')
	print('\n')
	print('Confusion Matrix')
	print('\n')
	print(learn_object.confusion_matrix)

def summarize_multiple(item_list):
	print('Report Summary')

	print('Name, Accuracy Score, Runtime')
	for item in item_list:
		print(item.name, ',', item.accuracy_score, ',', item.runtime)





item_list = create_multiple_reports(Learn_Object_List, X_train, y_train, X_test)
summarize_multiple(item_list)