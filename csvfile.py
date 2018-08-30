import csv
from csv import *


 # csv_writer = csv.writer(fileobj [, dialect='excel']
 #                                    [optional keyword args])
 #            csv_writer.writerows(rows)
 # reader(...)
 #        csv_reader = reader(iterable [, dialect='excel']
 #                                [optional keyword args])
 #            for row in csv_reader:
 #                process(row)
        


# def pen(file,data):
# 	write = writer(file,delimiter = ',')
# 	for line in data:
# 		write.writerow(line)
def reader(file):
	reaad = DictReader(file,delimiter=',')
	for a in reaad:
		print('Name is :',a['name'])
		print('Address is :',a['address'])
		print('Phone Number is :',a['phonenumber'])
		print(60*'-')
if __name__ == '__main__':
	# file = open('sample.csv','w')
	# data = ['name,address,phonenumber'.split(','),
	# 			'Batman,USA,234564'.split(','),
	# 			'superman,USA,34534234564'.split(','),
	# 			'ironman,USA,2356564564'.split(','),
	# 			'woman,USA,2398894564'.split(','),
	# 			'panther,USA,13233333'.split(','),
	# 			'hulck,USA,34545345'.split(',')]
	# pen(file,data)
	file = open('sample.csv','r')
	reader(file)
	file.close()


# o/p
# ---------

# peron1
# ------------------
# name  is  Batman
# address is USA
# phonenumber is 4


# peron2
# ---------------
# ---
# name  is  Batman
# address is USA
# phonenumber is 4

