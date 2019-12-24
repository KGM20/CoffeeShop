import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)


@app.after_request  # CORS Headers
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET, PATCH, POST, DELETE, OPTIONS')
    return response


@app.route('/drinks', methods=['GET'])
def retrieve_drinks():

    drinks = db.session.query(Drink).order_by(Drink.id).all()
    short_drinks = [drink.short() for drink in drinks]

    return jsonify({
        'success': True,
        'drinks': short_drinks
    }), 200


@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def retrieve_drinks_detail(jwt):

    drinks = db.session.query(Drink).order_by(Drink.id).all()
    long_drinks = [drink.long() for drink in drinks]

    return jsonify({
        'success': True,
        'drinks': long_drinks
    }), 200


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def create_drink(jwt):
    body = request.get_json()

    title = body.get('title', None)
    recipe = json.dumps(body.get('recipe', None))

    drink = Drink(title=title, recipe=recipe)
    long_drink = drink.long()

    try:
        drink.insert()

        return jsonify({
            'success': True,
            'drinks': long_drink
        }), 200

    except:
        abort(422)


@app.route('/drinks/<int:drink_id>', methods=['PATCH'])
@requires_auth('post:drinks')
def update_drink(jwt, drink_id):
    body = request.get_json()

    title = body.get('title', None)
    recipe = json.dumps(body.get('recipe', None))

    drink = db.session.query(Drink).get(drink_id)

    if drink is None:
        abort(404)

    try:
        drink.title = title
        drink.recipe = recipe

        drink.update()
        long_drink = drink.long()

        return jsonify({
            'success': True,
            'drinks': long_drink
        }), 200

    except:
        abort(422)


@app.route('/drinks/<int:drink_id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(jwt, drink_id):

    drink = db.session.query(Drink).get(drink_id)

    if drink is None:
        abort(404)

    try:
        drink.delete()

        return jsonify({
            'success': True,
            'delete': drink_id
        }), 200

    except:
        abort(422)


@app.errorhandler(422)
def unprocessable_entity(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "Unprocessable Entity"
    }), 422


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Resource Not Found"
    }), 404


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response
