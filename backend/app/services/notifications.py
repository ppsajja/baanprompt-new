from __future__ import annotations

from app.schemas.booking import Notification


def send_notifications(recipient_customer: str, recipient_technician: str, message_customer: str, message_technician: str) -> list[Notification]:
    return [
        Notification(recipient=recipient_customer, channel='sms', message=message_customer),
        Notification(recipient=recipient_technician, channel='sms', message=message_technician),
    ]
