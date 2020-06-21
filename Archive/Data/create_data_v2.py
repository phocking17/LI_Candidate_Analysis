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
		out = thresholds(idd, outs, [0.3, 0.7])
	else:
		out = thresholds(idd, outs, [0.1, 0.9])
	return out

def first_gen(ethnicity):
	idd = random.random()
	outs = ['Yes', 'No']
	if ethnicity is 'White':
		out = thresholds(idd, outs, [0.2, 0.8])
	elif ethnicity is 'Black':
		out = thresholds(idd, outs, [0.7, 0.3])
	elif ethnicity is 'Hispanic':
		out = thresholds(idd, outs, [0.8, 0.2])
	elif ethnicity is 'Asian':
		out = thresholds(idd, outs, [0.3, 0.7])
	return out

def languages(ethnicity):
	ethn_map = {'White':random.normalvariate(0.5, 0.6), 'Black':random.normalvariate(0.5, 0.75), 'Hispanic':random.normalvariate(1, 0.5), 'Asian':random.normalvariate(1, 0.5)}
	idd = ethn_map[ethnicity]
	out = 1 + ((idd)//1)
	if out < 1:
		out = 1
	out = int(out)
	return out

def income_bracket(ethnicity):
	ethn_map={'White':random.normalvariate(0.5, 0.2), 'Black':random.betavariate(3, 8), 'Hispanic':random.betavariate(2, 10), 'Asian':random.normalvariate(0.4, 0.2)}
	idd = ethn_map[ethnicity]
	out = idd*120000
	if out < 10000:
		out = 10000
	return out

def undergrad(generation, ethn, sports, inc):
	generation_map = {'Yes':random.betavariate(4,12), 'No':random.random()}
	ethn_map = {'White':random.normalvariate(0.5, 0.05), 'Black':random.betavariate(2, 10), 'Hispanic':random.betavariate(2, 15), 'Asian':random.normalvariate(0.4, 0.1)}
	sports_map = {'No':random.betavariate(3,8), 'Yes':random.normalvariate(0.5, 0.1)}
	if inc < 20000:
		inc_score = random.betavariate(3,8)
	elif inc < 70000:
		inc_score = random.normalvariate(0.5, 0.1)
	else:
		inc_score = random.betavariate(8,3)
	gen_score = generation_map[generation]
	ethn_score = ethn_map[ethn]
	sports_score = sports_map[sports]
	net_score = (0.4*inc_score)+(0.2*gen_score)+(0.3*sports_score)+(0.1*ethn_score)
	out = ((10/7)*(100*(1-net_score)-20))//1
	if out < 1:
		out = random.random()*10
	return out

def extra_degrees(generation, languages, inc):
	generation_map = {'Yes':random.betavariate(2,10), 'No':random.random()}
	if inc < 20000:
		inc_score = random.betavariate(4,6)
	elif inc < 60000:
		inc_score = random.normalvariate(0.6, 0.1)
	else:
		inc_score = random.betavariate(10,2)
	lang_score = languages/5
	net_score = (lang_score*0.05)+(inc_score*0.2)+(generation_map[generation]*0.1)
	out = (net_score*10)//1
	return out

def law_school(undergrad, inc):
	if inc < 20000:
		inc_score = random.betavariate(4,10)
	elif inc < 60000:
		inc_score = random.normalvariate(0.5, 0.15)
	else:
		inc_score = random.betavariate(10,2)
	if undergrad < 20:
		U_score = random.betavariate(10,2)
	elif undergrad < 50:
		U_score = random.normalvariate(0.5, 0.15)
	else:
		U_score = random.betavariate(2, 10)
	net_score = (inc_score*0.2)+(U_score*0.8)
	out = (100*(1-net_score))//1
	if out < 1:
		out = random.random()*10
	return out

def success(undergrad, lawschool, extradegrees, sports):
	if undergrad < 20:
		U_score = random.betavariate(10,2)
	elif undergrad < 50:
		U_score = random.normalvariate(0.5, 0.15)
	else:
		U_score = random.betavariate(2,10)
	if lawschool < 20:
		L_score = random.betavariate(10,2)
	elif lawschool < 50:
		L_score = random.normalvariate(0.5, 0.1)
	else:
		L_score = random.betavariate(2,10)
	degree_score = extradegrees/5
	sports_map = {'No':random.betavariate(2,10), 'Yes':random.normalvariate(0.5, 0.15)}
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


	

