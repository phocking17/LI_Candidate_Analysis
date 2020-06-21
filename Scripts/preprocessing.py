### Standardizes and Normalizes Data Set for testing
### Outputs a data file with standard scores and normalized scores according to category
################################################
import pandas as pd
from sklearn.preprocessing import LabelEncoder, PowerTransformer
################################################
def processing(file_name, list_categorical_columns, normalizing_category, identifier_1, identifier_2, numeric_correlative):
	
	### Given a list of categorical data and normal data
	### Outputs a datafram with categorical data quantified
	def transform_to_classes(data, parameter_list):
		for parameter in parameter_list:
			le = LabelEncoder()
			data[parameter] = le.fit_transform(data[parameter])
		return data

	### Splits data by two identifiers
	def create_identifiers(data, identifier_1, identifier_2):
		identifier_list = []
		gender = data[identifier_1].unique()
		ethnicity = data[identifier_2].unique()
		for g in gender:
			for e in ethnicity:
				new_list = [g, e]
				identifier_list.append(new_list)

		return identifier_list

	### Splits the data by the identifiers and returns as dictionary
	def split_data_by_identifier(data, identifier_1, identifier_2):
		identifier_list = create_identifiers(data, identifier_1, identifier_2)
		column_list = data.columns
		identifier_tuples = [(i[0], i[1]) for i in identifier_list]

		identifier_dictionary = {n:pd.DataFrame(columns = column_list) for n in identifier_tuples}

		for row in data.iterrows():
			ID_check = (row[1][identifier_1], row[1][identifier_2])
			list_row = row[1].values.tolist()

			sample = identifier_dictionary[ID_check]
			sample = sample.append({n:l for n,l in zip(column_list,list_row)}, ignore_index = True)
			identifier_dictionary[ID_check] = sample

		return identifier_dictionary

	### Maps data to integer based scores
	def map_transform(list_data, min_goal, max_goal):
		i_min = min(list_data)
		i_max = max(list_data)
		slope = (max_goal - min_goal) / (i_max - i_min)
		transform = []
		for i in list_data:
			transform.append(min_goal + slope * (i - i_min))
		transform = [int(i) for i in transform]
		return transform

	### Normalizes data by a given set of categories
	def normalize_by_category(data, identifier_1, identifier_2, success_category, numeric_correlative):
		ID_dict = split_data_by_identifier(data, identifier_1, identifier_2)
		for key, item in zip(ID_dict.keys(), ID_dict.values()):
			item['success_category'] = item[success_category]
			item = item.drop(success_category, axis = 1)
			item = item[((item.success_category - item.success_category.mean()) / item.success_category.std()).abs() < 3]
			item['true_scores'] = item['success_category'].copy(deep=False)
			temp = item['success_category']
			item = item.drop('success_category', axis=1)
			pt = PowerTransformer()
			pt.fit_transform(item[['true_scores', numeric_correlative]])
			item['true_scores'] = (item.true_scores - item.true_scores.mean())/item.true_scores.std(ddof=0)
			item['success_category'] = temp.to_frame()
			item['true_scores'] = map_transform(item['true_scores'], 1, 10)
			ID_dict[key] = item
		chart = pd.concat(ID_dict.values())
		return chart

	### Changes column name of success to standard name
	def standardize(chart, success_category):
		chart['success_category']=chart[success_category]
		chart = chart.drop(success_category, axis=1)
		chart['success_category'] = map_transform(chart['success_category'], 1, 10)
		return chart

	### Performs Processing
	chart = pd.read_csv(file_name, sep=',')
	chart = transform_to_classes(chart, list_categorical_columns)
	standard = chart.copy(deep=False)
	normalized = chart.copy(deep=False)
	standard = standardize(standard, normalizing_category)
	normalized = normalize_by_category(chart, identifier_1, identifier_2, normalizing_category, numeric_correlative)

	return standard, normalized

### Formatting
'''
t, l = processing("C:\\Users\\Patrick Hocking\\Documents\\GitHub\\LI_Candidate_Analysis\\test_advanced_normalize_by_category\\test_advanced.csv",['gender', 'ethnicity', 'sport', 'first_gen'],'success_score',  'gender', 'ethnicity', 'income_bracket')
'''