"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
import json
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200



    # [GET] /people Get a list of all the people in the database
    @app.route('/people', methods=["GET"])
    def get_all_peoples():
        
    peoples_list = []
    response_list = Peoples.query.all()
    
    for people in response_list:
        peoples_list.append(people.serialize())
    
    if peoples_list is not None:
        return jsonify(peoples_list), 200
    else:
        return "People not found", 404
    
    

  
    # [GET] /people/<int:people_id> Get a one single people information
    @app.route('/people/<int:people_id>', methods=["GET"])

    def get_people_By_id(people_id):
    result = next((people for people in peoples if people["People_id"] == people_id), None)
    if result is not None:
        return jsonify(result), 200
    else:
        return "People not found", 404

    # [GET] /planets Get a list of all the planets in the database
    @app.route('/planet', methods=["GET"])
    def get_all_planets():
        
    planets_list = []
    response_list = planets.query.all()
    
    for planet in response_list:
        planets_list.append(Planet.serialize())
    
    if planets_list is not None:
        return jsonify(planets_list), 200
    else:
        return "Planet not found", 404

    
   
    # [GET] /planets/<int:planet_id> Get one single planet information
 

@app.route('/users/<string:username>', methods=['GET'])
def getUsersByUsername(username):
  result = next((user for user in users if user["Username"] == username), None)
  if result is not None:
    return jsonify(result), 200
  else:
    return "User not found", 404
    # [GET] /users Get a list of all the blog post users
    @app.route('/users', methods=["GET"])
def getAllUsers():
  return jsonify(users), 200

@app.route('/users/<string:username>', methods=['GET'])
def getUsersByUsername(username):
  result = next((user for user in users if user["Username"] == username), None)
  if result is not None:
    return jsonify(result), 200
  else:
    return "User not found", 404
    # [GET] /users/favorites Get all the favorites that belong to the current user.
    @app.route('/users', methods=["GET"])
def getAllUsers():
  return jsonify(users), 200

@app.route('/users/<string:username>', methods=['GET'])
def getUsersByUsername(username):
  result = next((user for user in users if user["Username"] == username), None)
  if result is not None:
    return jsonify(result), 200
  else:
    return "User not found", 404
    # [POST] /favorite/planet/<int:planet_id> Add a new favorite planet to the current user with the planet id = planet_id.
    @app.route('/users', methods=["POST"])
def addUser():
  body = json.loads(request.data)

  userName = body["Username"]
  age = body["Age"]

  newUser = {
    "Username": userName,
    "Age": age
  }

  users.append(newUser)
  return jsonify(newUser), 200
    # [POST] /favorite/people/<int:planet_id> Add a new favorite people to the current user with the people id = people_id.
    @app.route('/users', methods=["POST"])
def addUser():
  body = json.loads(request.data)

  userName = body["Username"]
  age = body["Age"]

  newUser = {
    "Username": userName,
    "Age": age
  }

  users.append(newUser)
  return jsonify(newUser), 200
    # [DELETE] /favorite/planet/<int:planet_id> Delete favorite planet with the id = planet_id.
    @app.route('/users/<string:username>', methods=["DELETE"])
def deleteUser(username):
  userFound = None
  for index, user in enumerate(users):
    if user["Username"] == username:
      userFound = user
      users.pop(index)
  if userFound is not None:
    return "User deleted", 200
  else:
    return "User not found", 404

    # [DELETE] /favorite/people/<int:people_id> Delete favorite people with the id = people_id.
    @app.route('/users/<string:username>', methods=["DELETE"])
def deleteUser(username):
  userFound = None
  for index, user in enumerate(users):
    if user["Username"] == username:
      userFound = user
      users.pop(index)
  if userFound is not None:
    return "User deleted", 200
  else:
    return "User not found", 404


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
