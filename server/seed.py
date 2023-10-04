#!/usr/bin/env python3
# server/seed.py

from app import app
from models import db, Production
from faker import Faker
from random import choice as rc

# Creat application context 
with app.app_context():

    fake=Faker()

    # Delete all rows in the "productions" table
    Production.query.delete()

    # Add several Production instances to the "productions" table
    productions = []
    genres = ["Scary", "SciFi", "Comedy", "Action", "Thriller", "Rom-Com", "Drama"]

    for n in range(20):
        prod = Production(title=fake.cryptocurrency_name(), genre=rc(genres), budget=fake.random_number(), director = fake.name(), description = fake.catch_phrase(), ongoing=fake.boolean())

        productions.append(prod)

    # Add all the production instances
    db.session.add_all(productions)
    # # Commit the transaction
    db.session.commit()
