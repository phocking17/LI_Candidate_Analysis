
### Transforms dataframes into testing dataframes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import preprocessing

def prepare_for_testing(dataframe, success_category, drop_columns_list=None, select_columns_list = None):
	X = dataframe.drop(success_category, axis=1)
	if drop_columns_list is None:
		pass
	else:
		for selection in drop_columns_list:
			X = X.drop(selection, axis=1)
	if select_columns_list is None:
		pass
	else:
		X = dataframe[select_columns_list]
	y = dataframe[success_category]
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
	sc = StandardScaler()
	X_train = sc.fit_transform(X_train)
	X_test = sc.transform(X_test)
	return [X_train, X_test, y_train, y_test]

def prepare_for_testing_normalized(dataframe, success_category, success_stan, drop_columns_list=None, select_columns_list = None):
	X = dataframe.drop(success_category, axis=1)
	if drop_columns_list is None:
		pass
	else:
		for selection in drop_columns_list:
			X = X.drop(selection, axis=1)
	if select_columns_list is None:
		pass
	else:
		X = dataframe[select_columns_list + [success_stan]]
	y = dataframe[success_category]
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
	y_test_stan = X_test[success_stan]
	X_train = X_train.drop(success_stan, axis=1)
	X_test = X_test.drop(success_stan, axis=1)
	sc = StandardScaler()
	X_train = sc.fit_transform(X_train)
	X_test = sc.transform(X_test)
	return [X_train, X_test, y_train, y_test, y_test_stan]


'''
s, n = preprocessing.processing('test_advanced.csv', ['gender', 'ethnicity', 'sport', 'first_gen'], 'success_score', 'ethnicity', 'gender', 'income_bracket')
print(s)
print(n)

prep_s = prepare_for_testing(s, 'success_category')
prep_n = prepare_for_testing_normalized(n, 'true_scores', 'success_category', None, ['undergrad', 'lawschool'])
#print(n)

for i in prep_n:
	print(i)

'''