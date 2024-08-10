import unittest

from pydantic import ValidationError

from backend.app.core.models.client import Client


class TestClientPayload(unittest.TestCase):
    def setUp(self) -> None:
        self.test_payload: dict = {
            "firstName": "Shashank",
            "lastName": "Dwivedi",
            "email": "shashank22.1994@gmail.com",
            "contactNo": "9461249753",
            "addressLine1": "House Number 1902",
            "addressLine2": "RunwaL Bliss",
            "addressLine3": "Kanjurmarg East",
            "pincode": "400042",
            "city": "Mumbai",
            "state": "Maharashtra",
            "country": "India"
        }

    def test_valid_data(self):
        try:
            client: Client = Client.parse_obj(self.test_payload)
            self.assertEqual(True, True)  # add assertion here
        except ValidationError as e:
            self.assertEqual(True, False)

    def test_invalid_data(self):
        try:
            self.test_payload.pop("firstName")
            client: Client = Client.parse_obj(self.test_payload)
            self.assertEqual(True, False)
        except ValidationError as e:
            self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
