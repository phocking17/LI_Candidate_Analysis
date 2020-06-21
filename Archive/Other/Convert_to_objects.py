### Converts csv file into a list of objects with properties

class Lawyer:
	def __init__(self, gender='M', ethnicity='White', undergrad=100, lawschool=100, extradegrees=0, languages=1, started=0, partnerfirst=0, success=0):
		self.gender = gender
		self.ethnicity = ethnicity
		self.undergrad = undergrad
		self.lawschool = lawschool
		self.extradegrees = extradegrees
		self.languages = languages
		self.started = started
		self.partnerfirst = partnerfirst
		self.success = success


def csv_to_object_list(file_name):

	file = open(file_name, 'r')
	lines = file.readlines()
	lines = [i.split(',') for i in lines]
	file.close()

	lawyer_object_list = []

	for line in lines:
		x = Lawyer(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])
		lawyer_object_list.append(x)

	return lawyer_object_list