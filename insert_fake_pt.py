#!/usr/bin/env python

import pymongo

from faker import Factory
#from faker import Faker

fake = Factory.create('pt_BR')
#fake = Faker.create('pt_BR')

for cod in range(0,90000):

#    cli = pymongo.MongoClient('mongodb://localhost:30011,localhost:30012,localhost:30013/?replicaSet=rs1')
    cli = pymongo.MongoClient('localhost:27017')

    db = cli['empresa']

    doc = {
        'nome': fake.name(),
        'email': fake.email(),
        'uf': fake.estado_sigla(),
        'nascimento': fake.date_time_between(start_date="-30y", end_date="now", tzinfo=None),
	'data_criacao': fake.date_time(tzinfo=None),
        'enderecos': [
            {
                'tipo': 'Residencial',
                'logradouro': fake.street_name(),
                'numero': fake.building_number(),
                'bairro': fake.bairro(),
                'cidade': fake.city(),
                'cep': fake.postcode(),
            },
            {
                'tipo': 'Comercial',
                'cargo': fake.job(),
                'empresa': fake.company(),
                'logradouro': fake.street_name(),
                'numero': fake.building_number(),
                'bairro': fake.bairro(),
                'cidade': fake.city(),
                'uf': fake.estado_sigla(),
                'cep': fake.postcode(),
            },

        ],
        'telefones': [
            {
                'tipo': 'Celular',
                'numero': fake.phone_number(),
            },
            {
                'tipo': 'Residencial',
                'numero': fake.phone_number(),
            },
            {
                'tipo': 'Comercial',
                'number': fake.phone_number(),
            },

        ]
    }

    db.funcionarios.insert(doc)

    print(doc['nome'])
