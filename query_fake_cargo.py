#!/usr/bin/env python

import pymongo
import time

from faker import Factory
#from faker import Faker

fake = Factory.create('pt_BR')
#fake = Faker.create('pt_BR')
connection = pymongo.MongoClient('localhost:27017')
db = connection.empresa.funcionarios

for steps in range(0,10000):
	results = db.find({'enderecos.cargo': fake.job()})
	print()
	print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-')
	for record in results:
		# print out the document
		print(record['nome'] + ',',record['enderecos']) 
		print()
	time.sleep(2)	
# close the connection to MongoDB
connection.close()
