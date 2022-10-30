import unittest

from battleship.api import app

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

    def test_empty_ship_post_return_false(self):
        ships_dict = {
            "ships": []
        }
        result = BattleshipValidator.validate_ship_post(ships_dict)
        self.assertFalse(result)

    def test_validate_ship_post_return_true(self):
        result = BattleshipValidator.validate_ship_post(self.ships)
        self.assertTrue(result)

    def test_validate_ship_post_return_false(self):
        ships_dict = {
            "ships": [
                {
                    "x": 2,
                    "y": 1,
                    "size": 4,
                    "direction": "H"
                },
                {
                    "x": 8,
                    "y": 1,
                    "size": 4,
                    "direction": "H"
                }

            ]
        }
        result = BattleshipValidator.validate_ship_post(ships_dict)
        self.assertFalse(result)

    def test_validate_shipment_overlap_return_false(self):
        ships_dict = {
            "ships": [
                {
                    "x": 5,
                    "y": 5,
                    "size": 4,
                    "direction": "H"
                },
                {
                    "x": 7,
                    "y": 4,
                    "size": 3,
                    "direction": "V"
                }
            ]
        }
        result = BattleshipValidator.validate_ship_post(ships_dict)
        self.assertFalse(result)

    if __name__ == "__main__":
        unittest.main()
