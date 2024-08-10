import unittest

from pydantic import ValidationError

from backend.app.core.models.user import User


class TestUserPayload(unittest.TestCase):
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
            user: User = User.parse_obj(self.test_payload)
            self.assertEqual(True, True)
        except ValidationError as e:
            self.assertEqual(True, False)  # add assertion here

    def test_invalid_data(self):
        try:
            self.test_payload.pop("firstName")
            user: User = User.parse_obj(self.test_payload)
            self.assertEqual(True, False)
        except ValidationError as e:
            self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
