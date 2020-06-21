### Import libraries
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import os
import copy
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

### Imports Machine Learning Tools
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

### Imports Helper Functions
import preprocessing
import prepare_for_testing
from machine_learning_template import *
import Generate_Report

##################################################################################################################
### Create Learning Objects Here
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
##################################################################################################################
### Ends Learning Objects
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
### Set Broad Test Parameters
##################################################################################################################
### Data to test file
file = 'test_advanced.csv'
### First category for normalization technique
identifier_1 = 'gender'
### Second Category for normalization technique
identifier_2 = 'ethnicity'
### List of categorical data for processing
categorical = ['gender', 'ethnicity', 'sport', 'first_gen']
### Name of success column in data
success = 'success_score'
### Variable Correlating to Success Scores
correlating = 'income_bracket'
### Restrict Data to certain variables
restriction = ['undergrad', 'lawschool']
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
### Ends Broad Test Parameters
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
### Training by Model (1000 points)
##################################################################################################################
##################################################################################################################
### Splits data into standard scoring and normalized scoring
standard_data, normalized_data = preprocessing.processing(file, categorical, success, identifier_1, identifier_2, correlating)
testing_list = []
##################################################################################################################
##################################################################################################################
##################################################################################################################
### Conducts Training on Limited Number of Parameters
limit_test_standard = prepare_for_testing.prepare_for_testing(standard_data, 'success_category', None, restriction)
limit_test_normalized = prepare_for_testing.prepare_for_testing_normalized(normalized_data, 'true_scores','success_category', None, restriction)
### Conducts Training on Full Standard Model
test_standard = prepare_for_testing.prepare_for_testing(standard_data, 'success_category')
test_normalized = prepare_for_testing.prepare_for_testing_normalized(normalized_data, 'true_scores','success_category')
##################################################################################################################
### Train using standard
limit_mls = []
for model in Learn_Object_List:
	limit_mls.append(copy.deepcopy(model))
limit_list_standard_s = []
for ml_model in limit_mls:
	limit_list_standard_s.append(learner(limit_test_standard[2], limit_test_standard[0], limit_test_normalized[1], ml_model))
testing_list.append(limit_list_standard_s)

### Train using normal
limit_mls_n = []
for model in Learn_Object_List:
	limit_mls_n.append(copy.deepcopy(model))
limit_list_normal_s = []
for ml_model in limit_mls_n:
	limit_list_normal_s.append(learner(limit_test_normalized[2], limit_test_normalized[0], limit_test_normalized[1], ml_model))
testing_list.append(limit_list_normal_s)

##################################################################################################################
##################################################################################################################
##################################################################################################################
### Conducts Training on Full Standard Model

### Train using standard, Test using standard
standard_mls = []
for model in Learn_Object_List:
	standard_mls.append(copy.deepcopy(model))
list_standard_s = []
for ml_model in standard_mls:
	list_standard_s.append(learner(test_standard[2], test_standard[0], test_normalized[1], ml_model))
testing_list.append(list_standard_s)

##################################################################################################################
##################################################################################################################
##################################################################################################################
### Conducts Training on Full Normalized Moodel

### Train using normal, Test using standard
normal_mls = []
for model in Learn_Object_List:
	normal_mls.append(copy.deepcopy(model))
list_normalized_s = []
for ml_model in normal_mls:
	list_normalized_s.append(learner(test_normalized[2], test_normalized[0], test_normalized[1], ml_model))
testing_list.append(list_normalized_s)

##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
### Testing
##################################################################################################################
##################################################################################################################
Compare_scoring_matrix = []
count = 0
y_test_normal = test_normalized[3]
y_test_n_s = test_normalized[4]

### Move to Out Folder
def get_parent_dir(directory):
    return os.path.dirname(directory)

main = get_parent_dir(os.getcwd())
os.chdir(main)
os.chdir('Out')

for lisp in testing_list:
	for model in lisp:
		test_name = 'test_list_'+str(count)+'_' + model.name + '.txt'
		temp1 = Generate_Report.Generate_Report(test_name, test_normalized[1], y_test_n_s, model.prediction, 6, 4, model.runtime)
		count+=1
		temp_dir = get_parent_dir(os.getcwd())
		os.chdir(temp_dir)
		test_name = 'test_list_'+str(count)+'_' + model.name + '.txt'
		temp2 = Generate_Report.Generate_Report(test_name, test_normalized[1], y_test_normal, model.prediction, 6, 4, model.runtime)
		count+=1
		temp = temp1 + temp2
		temp_dir = get_parent_dir(os.getcwd())
		os.chdir(temp_dir)
		Compare_scoring_matrix.append(temp)

print(Compare_scoring_matrix)
t = sns.heatmap(Compare_scoring_matrix, annot=True, xticklabels=['Accuracy', 'Offset', 'Threshold', 'Accuracy', 'Offset', 'Threshold'], yticklabels=['limit_s1', 'limit_s2', 'limit_s3', 'limit_n1', 'limit_n2', 'limit_n3', 'stan_1', 'stan_2', 'stan_3', 'true_1', 'true_2', 'true_3'], vmin=0, vmax=1)
t.add_patch(Rectangle((0,0), 3, 3, fill=False, edgecolor='blue', lw=3))
t.add_patch(Rectangle((0,3), 3, 3, fill=False, edgecolor='blue', lw=3))
t.add_patch(Rectangle((0,6), 3, 3, fill=False, edgecolor='blue', lw=3))
t.add_patch(Rectangle((0,9), 3, 3, fill=False, edgecolor='blue', lw=3))
t.add_patch(Rectangle((3,0), 3, 3, fill=False, edgecolor='blue', lw=3))
t.add_patch(Rectangle((3,3), 3, 3, fill=False, edgecolor='blue', lw=3))
t.add_patch(Rectangle((3,6), 3, 3, fill=False, edgecolor='blue', lw=3))
t.add_patch(Rectangle((3,9), 3, 3, fill=False, edgecolor='blue', lw=3))
t.set_xlabel('Scores')
t.set_ylabel('Models')
plt.savefig('Summary_Heatmap')


