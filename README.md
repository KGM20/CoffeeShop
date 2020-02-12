# Coffee Shop Full Stack

## Full Stack Nano - IAM Final Project

This project is a coffee shop application created with the wish of learning and acquire experience as a full-stack developer. 
Users can do the following actions within the app:

1) Display graphics representing the ratios of ingredients in each drink.
2) Allow public users to view drink names and graphics.
3) Allow the shop baristas to see the recipe information.
4) Allow the shop managers to create new drinks and edit existing drinks.

This is a part of the Full-Stack Web Developer Nanodegree course of Udacity, designed to focus on applying skills to manage the user identity authentication and manage the access depending on the role of the user.

The backend code follows [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/)

## Coffee Shop Full Stack - Frontend

### Getting Setup

#### Installing Dependencies

##### Installing Node and NPM

This project depends on Nodejs and Node Package Manager (NPM). Before continuing, you must download and install Node (the download includes NPM) from [https://nodejs.com/en/download](https://nodejs.org/en/download/).

##### Installing Ionic Cli

The Ionic Command Line Interface is required to serve and build the frontend. Instructions for installing the CLI  is in the [Ionic Framework Docs](https://ionicframework.com/docs/installation/cli).

##### Installing project dependencies

This project uses NPM to manage software dependencies. NPM Relies on the package.json file located in the `frontend` directory of this repository. After cloning, open your terminal and run:

```bash
npm install
```

>_tip_: **npm i** is shorthand for **npm install**

### Running Your Frontend in Dev Mode

Ionic ships with a useful development server which detects changes and transpiles as you work. The application is then accessible through the browser on a localhost port. To run the development server, cd into the `frontend` directory and run:

```bash
ionic serve
```

>_tip_: Do not use **ionic serve**  in production. Instead, build Ionic into a build artifact for your desired platforms.
[Checkout the Ionic docs to learn more](https://ionicframework.com/docs/cli/commands/build)

## Coffee Shop Full Stack - Backend

### Getting Started

#### Installing Dependencies

##### Python 3.8

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

##### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

##### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

### Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

### Testing
To run the tests you need [Postman](https://getpostman.com), after installing import the Postman collection located in `./backend/udacity-fsnd-udaspicelatte.postman_collection.json`

## API Reference

### Base URL

This API runs on your local computer, using the server provided by Flask framework, which the default port to work is the 5000.
```
http://localhost:5000
      or
http://127.0.0.1:5000
```
If you have configured your Flask to run on another port, then you change the '5000' for the port you selected to work on.

### Error Handling

#### Response Codes

All the errors are returned in JSON format with the following structure:
```
{
	'success': False,
	'error': 422,
	'message': 'Unprocessable Entity'
}
```

#### Error types

The API handles the following error codes:
  
- 400: Bad Request
- 401: Unathorized
- 403: Forbidden
- 404: Not Found
- 422: Unprocessable entity
- 500: Internal server error

### Endpoints

- GET '/drinks'
- GET '/drinks-detail'
- POST '/drinks'
- PATCH '/drinks/integer:drink_id'
- DELETE '/drinks/integer:drink_id'

#### GET /drinks

- This is a public endpoint, anyone can access even without login a session. 
- Returns a dictionary with an array of all the drink objects simplified and a success argument.
- Request Arguments: None.
- Sample: `curl http://127.0.0.1:5000/drinks`
 ```
{
  "drinks": [
    {
      "id": 3,
      "recipe": [
        {
          "color": "white",
          "parts": 1
        },
        {
          "color": "#73CE1D",
          "parts": 2
        }
      ],
      "title": "Matcha Latte"
    },
    {
      "id": 5,
      "recipe": [
        {
          "color": "white",
          "parts": 1
        },
        {
          "color": "pink",
          "parts": 2
        }
      ],
      "title": "Strawberry Shake"
    },
    {
      "id": 6,
      "recipe": [
        {
          "color": "white",
          "parts": 3
        },
        {
          "color": "Brown",
          "parts": 1
        }
      ],
      "title": "Flatwhite"
    }
  ],
  "success": true
}
```

#### GET /drinks-detail

- This endpoint is exclusively for sessions with Barista or Manager roles.
- Returns a dictionary with an array of all the drink objects with all its details and a success argument.
- Request Arguments: None.
- Sample: `curl http://127.0.0.1:5000/drinks-detail`
 ```
{
  "drinks": [
    {
      "id": 3,
      "recipe": [
        {
          "color": "white",
          "name": "Milk",
          "parts": 1
        },
        {
          "color": "#73CE1D",
          "name": "Matcha",
          "parts": 2
        }
      ],
      "title": "Matcha Latte"
    },
    {
      "id": 5,
      "recipe": [
        {
          "color": "white",
          "name": "Milk",
          "parts": 1
        },
        {
          "color": "pink",
          "name": "Strawberry Ice Cream",
          "parts": 2
        }
      ],
      "title": "Strawberry Shake"
    },
    {
      "id": 6,
      "recipe": [
        {
          "color": "white",
          "name": "Milk",
          "parts": 3
        },
        {
          "color": "Brown",
          "name": "Coffee",
          "parts": 1
        }
      ],
      "title": "Flatwhite"
    }
  ],
  "success": true
}
```

#### POST /drinks

- This endpoint is exclusively for sessions with Manager role.
- Returns the drink object that was created in JSON format and a success argument.
- Request Arguments: A JSON object with the title of the drink and its recipe.
- Sample: `curl -X POST http://127.0.0.1:5000/drinks -H "Content-Type: application/json" -d '{"title": "Water3", "recipe": { "name": "Water", "color": "blue", "parts": 1}}'`
```
{
  "drinks": {
    "id": 10,
    "recipe": {
      "color": "blue",
      "name": "Water",
      "parts": 1
    },
    "title": "Water3"
  },
  "success": true
}
```

#### PATCH /drinks/integer:drink_id

- This endpoint is exclusively for sessions with Manager role.
- Returns the drink object that was modified given the id on the URL in JSON format and a success argument.
- Request Arguments: A JSON object with the title of the drink and its recipe.
- Sample: `curl -X PATCH http://127.0.0.1:5000/drinks/7 -H "Content-Type: application/json" -d '{"title": "Water5", "recipe": { "name": "Water", "color": "blue", "parts": 1}}'`
```
{
  "drinks": {
    "id": 7,
    "recipe": {
      "color": "blue",
      "name": "Water",
      "parts": 1
    },
    "title": "Water5"
  },
  "success": true
}
```

#### DELETE /drinks/integer:drink_id

- This endpoint is exclusively for sessions with Manager role.
- Deletes a drink that matches the given id on the URL. Returns the id of the deleted drink and a success value.
- Request Arguments: None
- Sample: `curl -X DELETE http://127.0.0.1:5000/drinks/5`
 ```
{
  "delete": 5,
  "success": true
}
```

## Authors

- Frontend by Udacity Developers Team
- Backend by Kevin "KGM20" Cruz