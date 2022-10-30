import json
import unittest

from battleship.api import app, SHIPS

app.testing = True


class TestPost(unittest.TestCase):

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

    def test_post_sucessfull(self):
        response = self.client.post('/battleship', data=self.payload)
        self.assertEqual(response.status_code, 201)

    def test_post_out_board_limit_return_bad_request(self):
        payload = json.dumps({
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
            ]}
        )
        response = self.client.post('/battleship', data=payload)
        self.assertEqual(response.status_code, 400)

    def test_post_shipment_overlap_return_bad_request(self):
        payload = json.dumps({
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
            ]}
        )
        response = self.client.post('/battleship', data=payload)
        self.assertEqual(response.status_code, 400)

    if __name__ == "__main__":
        unittest.main()
