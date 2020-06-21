import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

chart = pd.read_csv('test_advanced.csv', sep=',')
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
print(chart['success_score'].value_counts())
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

plt.show()