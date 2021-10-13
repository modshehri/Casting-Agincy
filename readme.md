# Full Stack Casting Agency API Backend

## Casting Agency Specifications

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## Motivation for project

This is the final project for my Full Stack Developer Nanodegree from Udacity.

## Getting Started

### Installing Dependencies

#### Python 3

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


#### PIP Dependencies

Once you have you are in the main directory, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

## Setup

Navigate to setup.sh file and run all commands within it, this will set the environment variables needed to run this project locally.

You have to have postgres running then, the app will use the file database.db as its DB.

## Running the server

In the main directory run the following command, which will configure all environment vaiables and run the server with --reload flag to auto rebuild after any saved changes.

```bash
. ./setup.sh
flask run --reload
```

# Roles

## Casting Assistant
- Can view actors and movies

## Casting Director
- All permissions a Casting Assistant has and…
- Add or delete an actor from the database
- Modify actors or movies

## Executive Producer
- All permissions a Casting Director has and…
- Add or delete a movie from the database


# Project deployed at

https://castingagincy.herokuapp.com

###### To test live APIs.

You can use the provided postman collection to make some tests Casting-Agincy.postman_collection.json. For other test cases you may use curl or postman using the valid tokens.

Assistant Token

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijc3V0lJRlRVQkdDYTZObDJlUFhhUyJ9.eyJpc3MiOiJodHRwczovL2Rldi16bXJpNG9xdi51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTM1MjI3NzIxMTM1NzU2MzcxOTAiLCJhdWQiOiJtb2RhZ2luY3kiLCJpYXQiOjE2MzQwNDA4MDAsImV4cCI6MTYzNDEyNzIwMCwiYXpwIjoibXROM0ZGZWNIaUZQTHA5SVBrNGhYc1J5bTBDeTFadDQiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.dlRVeDr0SPovgQznZSUEPw-_SvLsmoHwz7maHj8gz-tuSqkhYX-3343e8sqoqSP7t-suTCPx8EuOSWbag2FCbazQWZIiZ1nBWPHM8Uz_Q2TfL7vgwAzxlq_KU6HMFf4gSyPp1cO_Uxanb3q15aaldEzOvgMGe61Rs0h-PcUZA2eEpRkACKfcc0nYqQ0g9CTtCkjmIAWbyWL5LotzbaLegPRLR4bCZwAjzKhAiZlvbUGQJUgraWYHHc7OrSacl3Hi7tk66UAwDJ2rYBNXpc6OZ30uTOXpNMrondN-qsxhmaG8Y-hjSFIt4UlO1Vl533YeG9XuC-9dyQxdwq9Z4ZeXqA
```

Director Token

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijc3V0lJRlRVQkdDYTZObDJlUFhhUyJ9.eyJpc3MiOiJodHRwczovL2Rldi16bXJpNG9xdi51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDYzMDkzNTk0OTI0MzMzODc2MTEiLCJhdWQiOiJtb2RhZ2luY3kiLCJpYXQiOjE2MzQwNDA3MTIsImV4cCI6MTYzNDEyNzExMiwiYXpwIjoibXROM0ZGZWNIaUZQTHA5SVBrNGhYc1J5bTBDeTFadDQiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.nRIW2zlOBejSvWmQebVfgG82q2lfy3yhCWVugICbY2GaLWhQS5bpw_9GCQlNkKMF-48bJeq-yjQcmeeC0l3-6px2GL31L8eWS_4HNvDj8uC034Tn6QUy-BnRtzvugsPSdLXCS3BRlLb66fF5DMkzYkxosU5rmRJqMxYVfMBXe2KWP97J12Q6Wmfc3huZB70CxLdksBYgCyxWRF2RLcv0PyXCd3u3nrzCzA9PgKiZbHlJNH96HIlMIhcF36QV6nhxz2n3gkhvcOf1iRpcGZsMvXPheOzmDXQ33KPKGZktFURfwiXTpXvbi27U2-9DvICKzTz0QluPArHos5VUmE5y8A
```

Executive Token

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijc3V0lJRlRVQkdDYTZObDJlUFhhUyJ9.eyJpc3MiOiJodHRwczovL2Rldi16bXJpNG9xdi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE1NGY4N2EzM2Y2OTIwMDcwNDJjZjQzIiwiYXVkIjoibW9kYWdpbmN5IiwiaWF0IjoxNjM0MDQwNjE1LCJleHAiOjE2MzQxMjcwMTUsImF6cCI6Im10TjNGRmVjSGlGUExwOUlQazRoWHNSeW0wQ3kxWnQ0Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3IiLCJkZWxldGU6bW92aWUiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.W_6pFittGJRYckFa502zpMY80Whv9qjLC4KLEvOcvx-ZdU-m6U22xFVrSurY-BQT8niEOpdqND-Vo8suqXooli59vNYOZV_6UBvAu5JowY2stO_4UPvF2uuvWoV0BOZ-nJYL8lcbPW7lZ9HtC6gCYVeBvl7rSHnz7-leCPofFEswtR3ZdV2IoC5JBSPfwR_2qF1bU3QNxDY3Lgx4zaJeu2EwkAC5MvybP75EvC8vx6IMu6U0e4TZpPOjOP-YfUJQIu-Vxld19Zm0hAE0aG12kQd8tAJ_R5FnJZJM6R_e2YpMFwh029d9eGNw90i7Ju-oSN63fwvpWKsyoRLVdlCQvA
```

Valid tokens are provided as environment variables within the setup.sh file.

## To deploy the project at Heroku

- Rgister at Heroku 
- install heroku CLI using the command
```
brew tap heroku/brew && brew install heroku
```
- Login to your Heroku account running the command
```
heroku login
```
- Create a Heroku app using teh command
```
heroku create name_of_your_app
```
- Set up your environment veriables from the file setup.sh at Heroku
- Create a heroku add on for a postgres database using the command
```
heroku addons:create heroku-postgresql:hobby-dev --app name_of_your_application
```
- Push your project to Heroku using the command
```
git push heroku master
```
- Run your application using teh command 
```
heroku run python manage.py db upgrade --app name_of_your_application
```

## Testing locally

To run the tests, run

```
python test_flaskr.py
```

The tests print data returned from the APIs along with API logs.

#### The rests also use the Auth token set in env variables and will give an error if the tokens are expired.

## API Reference

### Error Handling

Errors are returned as JSON objects in the following format:

```
{
    "success": False,
    "error": 400,
    "message": "bad request"
}
```

### Endpoints

- GET '/actors'
- POST '/actors'
- PATCH '/actors/<actor_id>'
- DELETE '/actors/<actor_id>'
- GET '/movies'
- GET '/actors'
- POST '/actors'
- PATCH '/actors/<actor_id>'
- DELETE '/actors/<actor_id>'

#### GET '/movies'
Fetches an array of movies
Required URL Arguments: None
Required Data Arguments: None
Returns: Returns Json data about movies
Success Response:

```
{
    "success": True, 
    "movies": [movies]
}
```

#### GET '/actors'
Fetches an array of actors
Required Data Arguments: None
Returns: Json data about actors
Success Response:

```
{
    "success":True
    "actors":[actors],
}
```

#### DELETE '/movies/<int:movie_id>'
Deletes the movie_id of movie
Required URL Arguments: movie_id: movie_id_integer
Required Data Arguments: None
Returns: deleted movie's ID
Success Response:

```
{   
    'success': True,
    'deleted': 8
}
```

#### DELETE '/actors/<int:actor_id>'
Deletes the actor_id of actor
Required URL Arguments: actor_id: actor_id_integer
Required Data Arguments: None
Returns:the deleted actor's ID
Success Response:

```
{   
    'success': True,
    'deleted': 8
}
```

#### POST '/movies'
Post a new movie in a database.
Required URL Arguments: None
Required Data Arguments: Json data
Success Response:

```
{   
    'success': True,
    'movie': movie
}
```

#### POST '/actors'
Post a new actor in a database.

Required URL Arguments: None

Required Data Arguments: Json data

Success Response:

```
{   
    'success': True,
    'movie': actor
}
```

#### PATCH '/movies/<int:movie_id>'
Updates the movie_id of movie
Required URL Arguments: movie_id: movie_id_integer
Required Data Arguments: None
Returns: Json data about the updated movie
Success Response:

```
{   
    'success': True,
    'movie': movie
}
```

#### PATCH '/actors/<int:actor_id>'
Updates the actor_id of actor
Required URL Arguments: actor_id: actor_id_integer
Required Data Arguments: None
Returns: Json data about the modified actor's ID
Success Response:

```
{   
    'success': True,
    'movie': actor
}
```
