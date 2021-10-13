

import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, Movie, Actor, db_drop_and_create_all
from app import createapp

TESTING_DATABASE_URI = os.getenv('TEST_DATABASE_URI')
ASSISTANT_TOKEN = os.getenv('ASSISTANT_TOKEN')
DIRECTOR_TOKEN = os.getenv('DIRECTOR_TOKEN')
EXECUTIVE_TOKEN = os.getenv('EXECUTIVE_TOKEN')


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""

    def setUp(self):
        self.app = createapp(config="TEST")
        self.client = self.app.test_client
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            db_drop_and_create_all()
            # self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_post_movies(self):
        movie = {
            "title": "MOD TRYING",
            "release_date": "2021-10-12"
        }

        res = self.client().post('/movies',
                                 headers={
                                     "Authorization": "Bearer "+EXECUTIVE_TOKEN
                                 }, json=movie)
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        movie_db = Movie.query.get(data['movie']['id'])
        self.assertEqual(movie_db.get_json(), data["movie"])

    def test_post_movies_fail_422(self):
        movie = {
            "title": "Avengers",
        }
        res = self.client().post('/movies',
                                 headers={
                                     "Authorization": "Bearer "+EXECUTIVE_TOKEN
                                 }, json=movie)
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(422, res.status_code)

    def test_post_movies_fail_403(self):
        movie = {
            "title": "Avengers",
            "release_date": "2019-01-02",
        }
        res = self.client().post('/movies',
                                 headers={
                                     "Authorization": "Bearer "+ASSISTANT_TOKEN
                                 }, json=movie)
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(403, res.status_code)

    def test_list_movies_fail_401(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    def test_list_movies(self):
        res = self.client().get('/movies',
                                headers={
                                    "Authorization": "Bearer "+ASSISTANT_TOKEN
                                })
        data = json.loads(res.data)
        if res.status_code == 200:
            self.assertTrue(data['success'])
            self.assertNotEqual(len(data['movies']), 0)

    def test_delete_movie(self):
        movie = Movie.query.order_by(Movie.id).first()
        movie_id = movie.id
        res = self.client().delete('/movies/'+str(movie.id),
                                   headers={
            "Authorization": "Bearer "+EXECUTIVE_TOKEN})
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        self.assertEqual(movie_id, int(data['deleted']))

    def test_delete_movie_fail_401(self):
        res = self.client().delete('/movies/1000')
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(401, res.status_code)

    def test_delete_movie_fail_404(self):
        res = self.client().delete('/movies/1000',
                                   headers={
                                       "Authorization": "Bearer "
                                       + EXECUTIVE_TOKEN})
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(404, res.status_code)

    def test_patch_movie_fail_404(self):
        movie = {
            "title": "Avengers",
            "release_date": "2019-01-02",
        }
        res = self.client().patch('/movies/1000',
                                  headers={
                                      "Authorization": "Bearer "
                                      + EXECUTIVE_TOKEN
                                  }, json=movie)

        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(404, res.status_code)

    def test_patch_movie_fail_404(self):
        movie = {
            "title": "Avengers",
            "release_date": "2019-01-02",
        }
        res = self.client().patch('/movies/1000',
                                  headers={
                                      "Authorization": "Bearer "
                                      + EXECUTIVE_TOKEN
                                  }, json=movie)
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(404, res.status_code)

    def test_patch_movie(self):

        movie_patch = {
            "title": "Avengers 2",
            "release_date": "2019-01-02",
        }

        movie = Movie.query.first()
        movie_id = movie.id
        res = self.client().patch('/movies/'+str(movie_id),
                                  headers={
            "Authorization": "Bearer "+DIRECTOR_TOKEN
        }, json=movie_patch)

        data = json.loads(res.data)

        self.assertTrue(data['success'])
        self.assertEqual(200, res.status_code)
        movie = Movie.query.get(movie_id)
        self.assertEqual(movie.get_json(), data['movie'])

# actor tests

    def test_post_actor(self):
        actor = {
            "name": "mod",
            "gender": "male",
            "age": 22,
        }

        res = self.client().post('/actors',
                                 headers={
                                     "Authorization": "Bearer "+EXECUTIVE_TOKEN
                                 }, json=actor)
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        actor_db = Actor.query.get(data['actor']['id'])
        self.assertEqual(actor_db.get_json(), data['actor'])

    def test_post_actors_fail_422(self):
        actor = {
            "name": "rish",
            "gender": "male",
        }
        res = self.client().post('/actors',
                                 headers={
                                     "Authorization": "Bearer "+EXECUTIVE_TOKEN
                                 }, json=actor)
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(422, res.status_code)

    def test_post_actors_fail_403(self):
        actor = {
            "name": "rish",
            "gender": "male",
            "age":  22
        }
        res = self.client().post('/actors',
                                 headers={
                                     "Authorization": "Bearer "+ASSISTANT_TOKEN
                                 }, json=actor)
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(403, res.status_code)

    def test_list_actors_fail_401(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    def test_list_actors(self):
        res = self.client().get('/actors',
                                headers={
                                    "Authorization": "Bearer "+ASSISTANT_TOKEN
                                })
        data = json.loads(res.data)
        if res.status_code == 200:
            self.assertTrue(data['success'])
            self.assertNotEqual(len(data['actors']), 0)

    def test_delete_actors(self):
        testing_actor = Actor(name="MOD", age=23, gender="Alpha Male")
        testing_actor.insert()
        actor = Actor.query.first()
        res = self.client().delete('/actors/'+str(actor.id),
                                   headers={
            "Authorization": "Bearer " + EXECUTIVE_TOKEN})
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        actor = Actor.query.get(data['deleted'])
        self.assertEqual(actor, None)

    def test_delete_actor_fail_401(self):
        res = self.client().delete('/actors/1000')
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(401, res.status_code)

    def test_delete_actor_fail_404(self):
        res = self.client().delete('/actors/1000',
                                   headers={
                                       "Authorization": "Bearer "
                                       + EXECUTIVE_TOKEN})
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(404, res.status_code)

    def test_patch_actor_fail_404(self):
        actor = {
            "name": "gopi",
            "gender": "male",
        }
        res = self.client().patch('/actors/1000',
                                  headers={
                                      "Authorization": "Bearer "+DIRECTOR_TOKEN
                                  }, json=actor)
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(404, res.status_code)

    def test_patch_actor_fail_403(self):
        actor = {
            "name": "gopi",
            "gender": "male",
        }
        res = self.client().patch('/actors/1000',
                                  headers={
                                      "Authorization": "Bearer "
                                      + ASSISTANT_TOKEN
                                  }, json=actor)
        data = json.loads(res.data)
        self.assertFalse(data['success'])
        self.assertEqual(403, res.status_code)

    def test_patch_actor(self):
        actor = {
            "name": "gopi",
            "gender": "male",
        }
        actor_db = Actor.query.order_by(Actor.id).first()
        res = self.client().patch('/actors/'+str(actor_db.id),
                                  headers={
            "Authorization": "Bearer "+DIRECTOR_TOKEN
        }, json=actor)
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        self.assertEqual(200, res.status_code)
        actor_db = Actor.query.get(data['actor']['id'])
        actor_json = actor_db.get_json()
        for key in actor.keys():
            self.assertEqual(actor[key], actor_json[key])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
