from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class AvailabilitySlot(BaseModel):
    slot_id: str
    technician_id: str
    start: datetime
    end: datetime
    available: bool = True


class BookingCreateRequest(BaseModel):
    customer_id: str = Field(..., min_length=1)
    service_type: str = Field(..., min_length=1)
    address_id: str = Field(..., min_length=1)
    technician_id: str = Field(..., min_length=1)
    slot_start: datetime
    slot_end: datetime
    deposit_amount: float = Field(default=0.0, ge=0)


class BookingResponse(BaseModel):
    id: str
    customer_id: str
    technician_id: str
    service_type: str
    address_id: str
    slot_start: datetime
    slot_end: datetime
    deposit_amount: float
    status: str


class PaymentRequest(BaseModel):
    booking_id: str = Field(..., min_length=1)
    amount: float = Field(..., gt=0)
    gateway_ref: str | None = None


class CancelRequest(BaseModel):
    booking_id: str = Field(..., min_length=1)
    reason: str = 'customer_cancelled'


class Notification(BaseModel):
    recipient: str
    channel: Literal['sms', 'email']
    message: str
