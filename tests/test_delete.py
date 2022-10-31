import json
import unittest

from battleship.api import app

app.testing = True


class TestDelete(unittest.TestCase):

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

    def test_delete_sucessfull(self):
        delete_response = self.client.delete('/battleship')
        self.assertEqual(delete_response.status_code, 200)

    if __name__ == "__main__":
        unittest.main()
