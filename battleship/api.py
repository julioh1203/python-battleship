import http
import json

import flask
from flask import request

from battleship.validators import BattleshipValidator

app = flask.Flask(__name__)


global SHIPS

@app.route('/battleship', methods=['POST'])
def create_battleship_game():
    global ships
    ships = []
    ships_posted = json.loads(request.data)
    is_valid = BattleshipValidator.validate_ship_post(ships_posted)
    if is_valid:
        ships = ships_posted
        return flask.jsonify(ships), http.HTTPStatus.CREATED
    return flask.jsonify(ships), http.HTTPStatus.BAD_REQUEST


@app.route('/battleship', methods=['PUT'])
def shot():
    shot = json.loads(request.data)

    # Validate if the shot is outside of the board
    is_valid = BattleshipValidator.validate_shot(shot)
    if not is_valid:
        return flask.jsonify(shot), http.HTTPStatus.BAD_REQUEST
    for ship in ships.get('ships'):
        indice_x = ship.get('x')
        indice_y = ship.get('y')
        size = ship.get('size')

    return flask.jsonify({}), http.HTTPStatus.NOT_IMPLEMENTED


@app.route('/battleship', methods=['DELETE'])
def delete_battleship_game():
    ships.clear()
    return flask.jsonify(ships), http.HTTPStatus.OK
