import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from models import db_drop_and_create_all, setup_db, Actor, Movie
from auth import AuthError, requires_auth

app = Flask(__name__)

database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))
setup_db(app, database_path)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
!! Running this funciton will add one
'''
db_drop_and_create_all()

# ROUTES
@app.route('/actors')
def get_index():
    actors = Actor.query.order_by(Actor.id).all()
    return jsonify({
        "success": True, 
        "actors": [actor.get_json() for actor in actors]
    })


@app.route('/actors', methods=['POST'])
def create_actor():
    data = request.get_json()

    if 'name' and 'gender' and 'age' not in data:
        abort(422)
    
    actor_name = data['name']
    actor_gender = data['gender']
    actor_age = data['age']

    actor = Actor(name=actor_name, gender=actor_gender, age=actor_age)
    actor.insert()

    return jsonify({
        "success": True, 
        "actor": actor.name
    })

@app.route('/actors/<actor_id>', methods=['PATCH'])
def patch_actors(actor_id):
    actor = Actor.query.get(actor_id)
    if actor is None:
        abort(404)

    data = request.get_json()

    if 'name' in data:
        actor.name = data['name']

    if 'age' in data:
        actor.recipe = data['age']

    if 'gender' in data:
        actor.gender = data['gender']

    actor.update()

    return jsonify({
        "success": True, 
        "actor": actor.get_json()
    })

# Error Handling
'''
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''

'''
@TODO implement error handler for 404
    error handler should conform to general task above
'''
@app.errorhandler(404)
def notFound(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404

'''
@TODO implement error handler for AuthError
    error handler should conform to general task above
'''
@app.errorhandler(AuthError)
def authorization_error(error):
    error.error["success"] = False
    response = jsonify(error.error)
    response.status_code = error.status_code

    return response