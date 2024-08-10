import datetime

from pydantic import BaseModel, Field


class Appointment(BaseModel):
    customer_id: int = Field(..., alias="customerId")
    product_id: int = Field(..., alias="productId")
    clinic_id: int = Field(..., alias="clinicId")
    appointment_start: datetime.datetime = Field(..., alias="appointmentStart")
    appointment_end: datetime.datetime = Field(..., alias="appointmentEnd")
