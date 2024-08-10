import datetime
import json
import unittest

from pydantic import ValidationError

from backend.app.core.models.appointment import Appointment


class TestAppointmentPayload(unittest.TestCase):
    def setUp(self) -> None:
        self.test_payload: dict = {
            "customerId": 1,
            "productId": 1,
            "clinicId": 1,
            "appointmentStart": datetime.datetime.utcnow(),
            "appointmentEnd": datetime.datetime.utcnow()
        }

    def test_valid_data(self):
        json_payload: dict = json.loads(json.dumps(self.test_payload, default=str))
        try:
            appointment: Appointment = Appointment.parse_obj(json_payload)
            self.assertEqual(True, True)
        except ValidationError as e:
            self.assertEqual(True, False)

    def test_invalid_data(self):
        self.test_payload.pop("appointmentEnd")
        try:
            json_payload: dict = json.loads(json.dumps(self.test_payload, default=str))
            appointment: Appointment = Appointment.parse_obj(json_payload)
            self.assertEqual(True, False)
        except ValidationError as e:
            self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
