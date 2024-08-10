from pydantic import BaseModel, Field


class User(BaseModel):
    first_name: str = Field(..., alias="firstName")
    second_name: str = Field(..., alias="secondName")
    email: str = Field(..., alias="email")
    contact_no: str = Field(..., alias="contactNo")
    address_line_1: str = Field(..., alias="addressLine1")
    address_line_2: str = Field(..., alias="addressLine2")
    pincode: str = Field(..., alias="pincode")
    city: str = Field(..., alias="city")
    state: str = Field(..., alias="state")
    country: str = Field(..., alias="country")
