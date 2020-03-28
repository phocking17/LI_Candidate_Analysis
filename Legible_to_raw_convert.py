### Converts Test_Data to raw data
import random

### Best law schools according to US News and World Report
def college_rankings(college):
	college_rankings_dict = {
		'Yale University':1,
		'Stanford University':2,
		'Harvard University':3,
		'Columbia University':4,
		'University of Chicago':5,
		'New York University':6,
		'University of Pennsylvania':7,
		'University of Virginia':8,
		'Northwestern University':9,
		'University of California -- Berkeley':10,
		'University of Michigan':11,
		'Duke University':12,
		'Cornell University':13,
		'Georgetown University':14,
		'University of California -- Los Angelas':15,
		'University of Texas':16,
		'Washington University':17,
		'University of Southern California':18,
		'Vanderbilt University':19,
		'Boston University':20,
		'University of Minnesota':21,
		'University of Notre Dame':22,
		'George Washington University':23,
		'Arizona State University':24,
		'Emory University':25,
		'University of Florida':26,
		'Fordham University':27,
		'University of California -- Irvine':28,
		'University of Iowa':29,
		'University of North Carolina':30,
		'Boston College':31,
		'University of Alabama':32,
		'University of Georgia':33,
		'University of Illinois':34,
		'Washington and Lee University':35,
		'William & Mary Law School':36,
		'Brigham Young University':37,
		'Indiana University':38,
		'Ohio State University':39,
		'University of California -- Davis':40,
		'University of Wisconsin':41,
		'George Mason University':42,
		'University of Washington':43,
		'Wake Forest University':44,
		'University of Utah':45,
		'University of Colorado':46,
		'Pepperdine University':47,
		'University of Arizona':48,
		'University of Maryland':49,
		'Baylor University':50
		}
	if college in college_rankings_dict:
		return college_rankings_dict[college]
	else:
		x = 0
		while x < 0.5:
			x = random.random()
		randomrank = int((x*100)//1)
		return randomrank

### Makes Yes or No into binary 0 or 1
def make_binary(boolean):
	if boolean == 'Yes':
		return 1
	else:
		return 0

### Conversion function
def convert_Test_Data():

	### Open Test_Data.csv file (read)
	Test_Data = open('Test_Data.csv','r')
	lines = Test_Data.readlines()
	lines = [i.split(',') for i in lines]
	Test_Data.close()

	### Create new raw data file
	raw_data = open('raw_Test_Data.csv', 'w')

	for line in lines[1:]:
		count = 1
		while count <= 8:
			part = line[count]

			if count == 1:
				raw_data.write(str(part))
				raw_data.write(',')
			if count == 2:
				raw_data.write(str(part))
				raw_data.write(',')
			if count == 3:
				rank = college_rankings(part)
				raw_data.write(str(rank))
				raw_data.write(',')
			if count == 4:
				rank = college_rankings(part)
				raw_data.write(str(rank))
				raw_data.write(',')
			if count == 5:
				piece = make_binary(part)
				raw_data.write(str(piece))
				raw_data.write(',')
			if count == 6:
				raw_data.write(str(part))
				raw_data.write(',')
			if count == 7:
				piece = make_binary(part)
				raw_data.write(str(piece))
				raw_data.write(',')
			if count == 8:
				piece = make_binary(part[:-1])
				raw_data.write(str(piece))
				raw_data.write(',')
			count+=1
		raw_data.write(str(1))
		raw_data.write('\n')
	raw_data.close()


convert_Test_Data()


