import random
import seaborn as sns
import matplotlib.pyplot as mpl

def thresholds(idd, outputs, thresh):
	test = 1
	count = 0

	while idd < test:
		test-=thresh[count]
		count+=1
	return outputs[count-1]

def gender():
	idd = random.random()
	gen = ['Male', 'Female']
	thresh = [0.5, 0.5]
	out = thresholds(idd, gen, thresh)
	return out



def ethnicity():
	idd = random.random()
	ethn = ['White', 'Black', 'Hispanic', 'Asian']
	thresh = [0.5, 0.2, 0.15, 0.15]
	out = thresholds(idd, ethn, thresh)
	return out

def sports(gender):
	idd = random.random()
	outs = ['Yes', 'No']
	if gender is 'Male':
		out = thresholds(idd, outs, [1, 0])
	else:
		out = thresholds(idd, outs, [0, 1])
	return out

def first_gen(ethnicity):
	idd = random.random()
	outs = ['Yes', 'No']
	if ethnicity is 'White':
		out = thresholds(idd, outs, [0, 1])
	elif ethnicity is 'Black':
		out = thresholds(idd, outs, [1, 0])
	elif ethnicity is 'Hispanic':
		out = thresholds(idd, outs, [1, 0])
	elif ethnicity is 'Asian':
		out = thresholds(idd, outs, [0, 1])
	return out

def languages(ethnicity):
	ethn_map = {'White':0, 'Black':0, 'Hispanic':1, 'Asian':2}
	idd = ethn_map[ethnicity]
	out = 1 + ((idd)//1)
	if out < 1:
		out = 1
	out = int(out)
	return out

def income_bracket(ethnicity):
	ethn_map={'White':0.8, 'Black':0.4, 'Hispanic':0.3, 'Asian':0.6}
	idd = ethn_map[ethnicity]
	out = idd*120000
	if out < 10000:
		out = 10000
	return out

def undergrad(generation, ethn, sports, inc):
	generation_map = {'Yes':1, 'No':0}
	ethn_map = {'White':1, 'Black':0, 'Hispanic':0, 'Asian':0}
	sports_map = {'No':0, 'Yes':1}
	if inc < 20000:
		inc_score = 0.2
	elif inc < 70000:
		inc_score = 0.5
	else:
		inc_score = 1
	gen_score = generation_map[generation]
	ethn_score = ethn_map[ethn]
	sports_score = sports_map[sports]
	net_score = (0.4*inc_score)+(0.2*gen_score)+(0.3*sports_score)+(0.1*ethn_score)
	out = ((10/7)*(100*(1-net_score)-20))//1
	if out < 1:
		out = random.random()*10
	return out

def extra_degrees(generation, languages, inc):
	generation_map = {'Yes':0, 'No':1}
	if inc < 20000:
		inc_score = 0.2
	elif inc < 60000:
		inc_score = 0.5
	else:
		inc_score = 1
	lang_score = languages/5
	net_score = (lang_score*0.05)+(inc_score*0.2)+(generation_map[generation]*0.1)
	out = (net_score*10)//1
	return out

def law_school(undergrad, inc):
	if inc < 20000:
		inc_score = 0.2
	elif inc < 60000:
		inc_score = 0.5
	else:
		inc_score = 1
	if undergrad < 20:
		U_score = 1
	elif undergrad < 50:
		U_score = 0.5
	else:
		U_score = 0.2
	net_score = (inc_score*0.2)+(U_score*0.8)
	out = (100*(1-net_score))//1
	if out < 1:
		out = random.random()*10
	return out

def success(undergrad, lawschool, extradegrees, sports):
	if undergrad < 20:
		U_score = 1
	elif undergrad < 50:
		U_score = 0.5
	else:
		U_score = 0.2
	if lawschool < 20:
		L_score = 1
	elif lawschool < 50:
		L_score = 0.5
	else:
		L_score = 0.2
	degree_score = extradegrees/5
	sports_map = {'No':0, 'Yes':1}
	sports_score = sports_map[sports]
	net_score = (U_score*0.2)+(L_score*0.5)+(degree_score*0.2)+(sports_score*0.1)
	out = (net_score*15)//1
	return out

def person():
	gen = gender()
	ethn = ethnicity()
	sport = sports(gen)
	first_g = first_gen(ethn)
	language = languages(ethn)
	income_brack = income_bracket(ethn)
	underg = undergrad(first_g, ethn, sport, income_brack)
	extradegree = extra_degrees(first_g, language, income_brack)
	law_sch = law_school(underg, income_brack)
	suc = success(underg, law_sch, extradegree, sport)
	return gen, ethn, sport, first_g, language, income_brack, underg, extradegree, law_sch, suc

### Initiate CSV
def Create_File(name, n):
	
	### Calls File
	file = open(name, 'w')

	file.write('gender,ethnicity,sport,first_gen,languages,income_bracket,undergrad,extradegrees,lawschool,success_score')
	file.write('\n')

	### Iterates over selected number of candidates
	for i in range(n):

		c = 0
		string = person()

		### Iterates on output
		while c < 10:
			file.write(str(string[c]))
			if c != 9:
				file.write(',')
			c+=1
		file.write('\n')

	file.close()



### Creates file
Create_File('test_advanced.csv', 10000)


	

