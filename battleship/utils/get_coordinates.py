def get_ships_coordinates(ships: dict):
    coordinates = list(list())
    for ship in ships.get('ships'):
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
