import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from statistics import median
from sklearn.preprocessing import PowerTransformer, LabelEncoder
from scipy import stats

chart = pd.read_csv('test_advanced.csv', sep=',')

### Normalization by Category
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


chart = normalize_by_category(chart[:1000])
'''
### Show Counts of Ethnicity
labels = ['White', 'Black', 'Hispanic', 'Asian']
men_means = chart['ethnicity'].value_counts()
width = 0.35
fig, ax = plt.subplots()
ax.bar(labels, men_means, width,  label='Men')
ax.set_ylabel('Count')
ax.set_title('Counts by Ethnicity')
ax.legend()

'''
### Show Undergrad by Income
tips = chart
sns.scatterplot(x="success_score", y="lawschool", hue='ethnicity', data=tips)

### Show Languages by Ethnicity
sns.catplot(x="extradegrees", y="income_bracket", kind='box', data=tips)

### Show Income by Ethnicity
sns.catplot(x="ethnicity", y="income_bracket", kind='box', data=tips)

### Show Lawschool by Success
sns.catplot(x="success_score", y="lawschool", kind='box', data=tips)

### Show Income by Success
sns.catplot(x="success_score", y="income_bracket", kind='box', data=tips)

### Success by Ethnicity
sns.catplot(x="ethnicity", y="success_score", kind='box', whis=2, showfliers = True, data=tips)

plt.show()