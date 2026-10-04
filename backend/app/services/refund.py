from __future__ import annotations

from app.models.booking import Refund
from app.rules.refund_policy import calculate_refund


def issue_refund(booking_id: str, deposit_amount: float, cancelled_reason: str, technician_departed: bool = False) -> Refund:
    refund_amount = calculate_refund(deposit_amount, cancelled_reason, technician_departed=technician_departed)
    return Refund(
        id=f'refund-{booking_id}',
        booking_id=booking_id,
        amount=refund_amount,
        rule='BR-01',
        status='processed' if refund_amount > 0 else 'pending',
    )
