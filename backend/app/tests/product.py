import unittest

from pydantic import ValidationError

from backend.app.core.models.product import Product


class TestProductPayload(unittest.TestCase):
    def setUp(self) -> None:
        self.test_payload: dict = {
            "name": "Root Canal Treatement",
            "description": "This is the description of Root Canal Treatment(RCT).",
            "price": 8500.0,
            "duration": 60
        }

    def test_valid_data(self):
        try:
            product: Product = Product.parse_obj(self.test_payload)
            self.assertEqual(True, True)  # add assertion here
        except ValidationError as e:
            self.assertEqual(True, False)

    def test_invalid_data(self):
        try:
            self.test_payload.pop("description")
            product: Product = Product.parse_obj(self.test_payload)
            self.assertEqual(True, False)
        except ValidationError as e:
            self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
