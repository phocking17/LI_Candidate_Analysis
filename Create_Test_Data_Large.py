### Creates Large set of test data for training
import random

### Creates characteristics
def make_character():
	step = 0
	attributes = 8
	### Repeats picking of random number
	while step <= attributes:
		x = random.random()

		### Creates gender (60% male)
		if step == 0:
			if x > 0.6:
				gender = 'F'
			else:
				gender = 'M'
		
		### Creates Ethnicity
		if step == 1:
			if x < 0.7:
				ethnicity = 'White'
			elif x < 0.8 and x > 0.7:
				ethnicity = 'Asian'
			elif x < 0.9 and x > 0.95:
				ethnicity = 'Black'
			else:
				ethnicity = 'Hispanic'

		### Creates Undergraduate (10% attend ivy if white, 2% attend ivy else)
		if step == 2:
			if ethnicity == 'White' and x < 0.1:
				undergrad = 1
			if x < 0.02:
				undergrad = 1
			else:
				undergrad = 0

		### Creates Law School (50% chance of going to top school for ivy, 10% chance of going to top school, else)
		if step == 3:
			if undergrad == 1 and x > 0.5:
				lawschool = 1
			if x > 0.9:
				lawschool = 1
			else:
				lawschool = int(100 - ((x*100)//1))

		### Determines if other degrees
		if step == 4:
			if x < 0.1:
				extradegrees = 1
			else:
				extradegrees = 0

		### Determines number of languages
		if step == 5:
			if ethnicity == 'White' or ethnicity == 'Black':
				if x < 0.9:
					languages = 1
				if x > 0.9:
					languages = int(((x-0.9)*100)//1)
			else:
				if x < 0.4:
					languages = 1
				if x > 0.4 and x < 0.9:
					languages = 2
				if x > 0.9:
					languages = int(((x-0.9)*100)//1)

		### Determines if Started with firm they're currently at (1 if started with firm)
		if step == 6:
			if x < 0.1:
				started = 1
			elif x < 0.05:
				started = 1
			else:
				started = 0

		### Determines if partner in the past (1 if so)
		if step == 7:
			if started == 1 and x < 0.1:
				partnerfirst = 1
			if started == 0 and x < 0.2:
				partnerfirst = 1
			else:
				partnerfirst = 0

		### Determines if current partner (1 if so)
		if step == 8:
			if x < 0.95:
				success = 0
			if partnerfirst == 1 and x < 0.995:
				success = 1
			if x > 0.95:
				success = 1

		step += 1
	return gender, ethnicity, undergrad, lawschool, extradegrees, languages, started, partnerfirst, success

### Initiate CSV
def Create_File(name, n):
	
	### Calls File
	file = open(name, 'w')

	### Iterates over selected number of candidates
	for i in range(n):

		c = 0
		string = make_character()

		### Iterates on output
		while c < 9:
			file.write(str(string[c]))
			if c != 8:
				file.write(',')
			c+=1
		file.write('\n')

	file.close()



### Creates file
Create_File('test.csv', 1000000)