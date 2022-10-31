import http
import json

import flask
from flask import request


from battleship.validators import BattleshipValidator
from controllers.ships import SHIP
from utils.get_coordinates import get_ship_coordinates_for_shot
from utils.update_ship_model import update_ship_model

app = flask.Flask(__name__)

@app.route('/battleship', methods=['POST'])
def create_battleship_game():
    ships = list()
    ships_posted = json.loads(request.data)
    is_valid = BattleshipValidator.validate_ship_post(ships_posted)
    if is_valid:
        ships_saved = SHIP.create_ship(ships_posted)
        return flask.jsonify(ships_posted), http.HTTPStatus.CREATED
    return flask.jsonify(ships_posted), http.HTTPStatus.BAD_REQUEST


@app.route('/battleship', methods=['PUT'])
def shot():
    shot = json.loads(request.data)

    # Validate if the shot is outside of the board
    is_valid = BattleshipValidator.validate_shot(shot)
    if not is_valid:
        return flask.jsonify(shot), http.HTTPStatus.BAD_REQUEST

    result = ""

    shot_x_coordinate = shot.get('x')
    shot_y_coordinate = shot.get('y')
    shot_coordinates = (shot_x_coordinate, shot_y_coordinate)

    result = SHIP().get_shot(shot_coordinates)

    response = {"result": result}
    return flask.jsonify(response), http.HTTPStatus.OK


@app.route('/battleship', methods=['DELETE'])
def delete_battleship_game():
    ships = SHIP().delete_ships()
    return flask.jsonify(ships), http.HTTPStatus.OK
