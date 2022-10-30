import http
import json

import flask
from flask import request

from battleship.validators import BattleshipValidator

app = flask.Flask(__name__)

SHIPS = dict()


@app.route('/battleship', methods=['POST'])
def create_battleship_game():
    ships = json.loads(request.data)
    is_valid = BattleshipValidator.validate_ship_post(ships)
    if is_valid:
        SHIPS = ships
        return flask.jsonify(ships), http.HTTPStatus.CREATED
    return flask.jsonify(ships), http.HTTPStatus.BAD_REQUEST


@app.route('/battleship', methods=['PUT'])
def shot():
    return flask.jsonify({}), http.HTTPStatus.NOT_IMPLEMENTED


@app.route('/battleship', methods=['DELETE'])
def delete_battleship_game():
    return flask.jsonify({}), http.HTTPStatus.NOT_IMPLEMENTED
