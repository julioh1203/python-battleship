def get_ships_coordinates(ships: dict):
    coordinates = list(list())
    for ship in ships:
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


def get_ship_coordinates_for_shot(ships: dict):
    ships_coordinates = list()
    for ship in ships:
        indice_x = ship.get('x')
        indice_y = ship.get('y')
        size = ship.get('size')
        direction = ship.get('direction')
        if direction == 'H':
            if size == 1:
                ships_coordinates.append([(indice_x, indice_y)])
            else:
                length_coordinate = size + indice_x
                ships_coordinates.append([(coordinate, indice_y) for coordinate in range(indice_x, length_coordinate)])
        if direction == 'V':
            if size == 1:
                ships_coordinates.append([(indice_x, indice_y)])
            else:
                length_coordinate = size + indice_y
                ships_coordinates.append([(indice_x, coordinate) for coordinate in range(indice_y, length_coordinate)])

    return ships_coordinates
