import json
import unittest

from battleship.api import app

app.testing = True


class TestShot(unittest.TestCase):

    def setUp(self) -> None:
        self.client = app.test_client()

        self.payload = json.dumps({
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
        })

        self.client.post('/battleship', data=self.payload)

    def test_shot_water_result(self):
        payload = json.dumps({
            "x": 5,
            "y": 4
        })
        response = self.client.put('/battleship', data=payload)
        self.assertEqual(response.json.get('result'), 'WATER')

    def test_shot_hit_result(self):
        payload = json.dumps({
            "x": 5,
            "y": 1
        })
        response = self.client.put('/battleship', data=payload)
        self.assertEqual(response.json.get('result'), 'HIT')

    def test_shot_sink_result(self):
        payload = json.dumps({
            "x": 6,
            "y": 8
        })
        response = self.client.put('/battleship', data=payload)
        self.assertEqual(response.json.get('result'), 'SINK')

    if __name__ == "__main__":
        unittest.main()
