from battleship.utils.get_coordinates import get_ships_coordinates


class BattleshipValidator:

    @staticmethod
    def check_indices_board(coordinates: list):
        for ship in coordinates:
            indice_x = ship[0]
            indice_y = ship[1]
            if indice_x < 0 or indice_x > 9:
                return False
            if indice_y < 0 or indice_y > 9:
                return False
        return True

    @staticmethod
    def check_shipments_overlap(coordinates: list):
        set_coordinates = set(coordinates)
        if len(coordinates) != len(set_coordinates):
            return False
        return True

    @classmethod
    def validate_ship_post(cls, ships: dict):
        coordinates = get_ships_coordinates(ships.get('ships'))
        if not coordinates:
            return False
        is_valid_board_indices = cls.check_indices_board(coordinates)
        if is_valid_board_indices:
            does_not_exist_overlap = cls.check_shipments_overlap(coordinates)
            if does_not_exist_overlap:
                return True
        return False

    @classmethod
    def validate_shot(cls, shot: dict):
        indice_x = shot.get('x')
        indice_y = shot.get('y')
        if indice_x < 0 or indice_x > 9:
            return False
        if indice_y < 0 or indice_y > 9:
            return False
        return True

