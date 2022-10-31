

SHIPS = list()


class SHIP:

    @staticmethod
    def get_coordinates(ship):
        coordinates = list()
        direction = ship.get('direction')
        initial_x_coordinate = ship.get('x')
        initial_y_coordinate = ship.get('y')
        size = ship.get('size')
        if direction == 'H':
            length_coordinate = size + initial_x_coordinate
            [coordinates.append((coordinate, initial_y_coordinate)) for coordinate in
             range(initial_x_coordinate, length_coordinate)]
        if direction == 'V':
            length_coordinate = size + initial_y_coordinate
            [coordinates.append((initial_x_coordinate, coordinate)) for coordinate in
             range(initial_y_coordinate, length_coordinate)]

        return coordinates

    @classmethod
    def create_ship(cls, ships):
        for ship in ships.get('ships'):
            ship_coordinates = cls.get_coordinates(ship)
            row = ship.get('x')
            column = ship.get('y')
            size = ship.get('size')
            direction = ship.get('direction')
            SHIPS.append({'id': f'{row}{column}', 'coordinates': ship_coordinates, 'size': size, 'direction': direction,
                          'number_hits': 0, 'status': ''})
        return SHIPS

    def delete_ships(self):
        for ship in SHIPS:
            ship.clear()
        return list(SHIPS)

    @classmethod
    def get_shot(self, shot_coordinates: tuple):
        for ship in SHIPS:
            if shot_coordinates in ship.get('coordinates'):

                if ship['status'] == 'SINK':
                    return 'SINK'

                number_hits = ship.get('number_hits')
                ship['number_hits'] = number_hits + 1
                if ship['number_hits'] == ship.get('size'):
                    ship['status'] = 'SINK'
                    return 'SINK'
                ship['status'] = 'HIT'
                return 'HIT'
        return 'WATER'



