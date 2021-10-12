import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
from datetime import date
from models import db_drop_and_create_all, setup_db, Actor, Movie
from auth import AuthError, requires_auth

def createapp(config=None):
    app = Flask(__name__)

    setup_db(app)


    CORS(app)

    '''
    @TODO uncomment the following line to initialize the datbase
    !! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
    !! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
    !! Running this funciton will add one
    '''
    db_drop_and_create_all()

    # ROUTES

    # Actors Routes
    @app.route('/')
    def get_greeting():
        greeting = "Hello" 
        return greeting

    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors():
        actors = Actor.query.order_by(Actor.id).all()
        return jsonify({
            "success": True, 
            "actors": [actor.get_json() for actor in actors]
        })


    @app.route('/actors', methods=['POST'])
    @requires_auth('patch:actor')
    def create_actor():
        data = request.get_json()

        if 'name' not in data:
            abort(422)

        if 'age' not in data:
            abort(422)

        if 'gender' not in data:
            abort(422)
        
        actor_name = data['name']
        actor_gender = data['gender']
        actor_age = data['age']

        actor = Actor(name=actor_name, gender=actor_gender, age=actor_age)
        actor.insert()

        return jsonify({
            "success": True, 
            "actor": actor.get_json()
        })

    @app.route('/actors/<actor_id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def patch_actors(actor_id):
        actor = Actor.query.get(actor_id)
        
        if actor is None:
            abort(404)

        data = request.get_json()

        if 'name' in data:
            actor.name = data['name']

        if 'age' in data:
            actor.age = data['age']

        if 'gender' in data:
            actor.gender = data['gender']

        actor.update()

        return jsonify({
            "success": True, 
            "actor": actor.get_json()
        })

    @app.route('/actors/<actor_id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actors(actor_id):
        actor = Actor.query.get(actor_id)
        if actor is None:
            abort(404)

        actor.delete()

        return jsonify({
            "success": True, 
            "deleted": actor_id
        })


    # Movies Routes 
    @app.route('/movies')
    @requires_auth('get:movies')
    def get_movies():
        movies = Movie.query.order_by(Movie.id).all()
        return jsonify({
            "success": True, 
            "movies": [movie.get_json() for movie in movies]
        })


    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movie')
    def create_movies():
        data = request.get_json()

        if 'title' and 'release_date' not in data:
            abort(422)
        
        movie_release_date = date.fromisoformat(data['release_date'])
        movie_title = data['title']

        movie = Movie(title=movie_title, release_date=movie_release_date)
        movie.insert()

        return jsonify({
            "success": True, 
            "movie": movie.get_json()
        })

    @app.route('/movies/<movie_id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def patch_movies(movie_id):
        movie = Movie.query.get(movie_id)
        if movie is None:
            abort(404)

        data = request.get_json()
        
        if 'title' in data:
            movie.title = data['title']

        if 'release_date' in data:
            movie.release_date = date.fromisoformat(data['release_date'])

        movie.update()


        return jsonify({
            "success": True, 
            "movie": movie.get_json()
        })

    @app.route('/movies/<movie_id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movies(movie_id):
        movie = Movie.query.get(movie_id)
        if movie is None:
            abort(404)

        movie.delete()

        return jsonify({
            "success": True, 
            "deleted": movie_id
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

    @app.errorhandler(404)
    def notFound(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(AuthError)
    def authorization_error(error):
        error.error["success"] = False
        response = jsonify(error.error)
        response.status_code = error.status_code

        return response
    
    return app

app = createapp()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
