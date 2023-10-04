# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response, request, g, current_app, session
from flask_migrate import Migrate
from models import db, Production
from faker import Faker
from random import choice as rc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

fake=Faker()
names = [fake.first_name() for n in range(12)]

@app.before_request
def set_up():
    g.name = rc(names)


@app.route("/")
def index():
    return f"<h1>Welcome to the Productions Website! {g.name}</h1>"
    

# dynamic route b/c of <>
@app.route("/productions/<string:title>")
def find_by_title(title):
    production = Production.query.filter_by(title=title).first()

    if production:
        # .to_dict() turns an instance into a dictionary with the keys being the column names and the values being the corresponding column value
        body = production.to_dict()
        status = 200
    else:
        body = f"<h1>Production titled {title} not found!</h1>"
    # make_response automatically during a dictonary into JSON without using jsonify
    return make_response(body, status)

@app.route("/productions/<int:id>")
def find_by_id(id):
    production = Production.query.filter_by(id=id).first()

    if production:
        body = production.to_dict()
        status = 200
    else:
        body = f"<h1>Production id:{id} not found!</h1>"
        status = 404
    return make_response(body, status)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
