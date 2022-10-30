import json
import unittest

from battleship.api import app
from battleship.utils.get_coordinates import get_ships_coordinates

app.testing = True


from battleship.validators import BattleshipValidator


class TestBattleshipValidator(unittest.TestCase):

    def setUp(self) -> None:
        self.ships = {
            "ships": [
                {
                    "x": 2,
                    "y": 1,
                    "size": 4,
                    "direction": "H"
                },
                {
                    "x": 7,
                    "y": 4,
                    "size": 3,
                    "direction": "V"
                },
                {
                    "x": 3,
                    "y": 5,
                    "size": 2,
                    "direction": "V"
                },
                {
                    "x": 6,
                    "y": 8,
                    "size": 1,
                    "direction": "H"
                }
            ],
        }

    def test_extract_ships_coordinates(self):
        expected = [(2, 1), (3, 1), (4, 1), (5, 1), (7, 4), (7, 5), (7, 6), (3, 5), (3, 6), (6, 8)]
        result = get_ships_coordinates(self.ships)
        self.assertEqual(result, expected)

    if __name__ == "__main__":
        unittest.main()
