from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Literal


@dataclass
class TimeSlot:
    id: str
    technician_id: str
    start: datetime
    end: datetime
    status: Literal['available', 'locked', 'booked'] = 'available'
    lock_expires_at: datetime | None = None


@dataclass
class Booking:
    id: str
    customer_id: str
    technician_id: str
    service_type: str
    address_id: str
    slot_start: datetime
    slot_end: datetime
    deposit_amount: float
    status: str = 'pending_confirmation'
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass
class Payment:
    id: str
    booking_id: str
    amount: float
    status: Literal['pending', 'authorized', 'captured', 'timeout', 'failed'] = 'pending'
    gateway_ref: str | None = None
    timeout_seconds: int = 30


@dataclass
class Refund:
    id: str
    booking_id: str
    amount: float
    rule: str
    status: Literal['pending', 'processed'] = 'pending'


@dataclass
class Job:
    id: str
    booking_id: str
    status: str = 'confirmed'
    scheduled_start: datetime | None = None
    deposit_amount: float = 0.0
    history: list[dict] = field(default_factory=list)

    def add_history(self, event: str, at: datetime | None = None) -> None:
        ts = at or datetime.now(timezone.utc)
        self.history.append({'event': event, 'at': ts.isoformat()})
