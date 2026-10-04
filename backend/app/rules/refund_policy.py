from __future__ import annotations


def calculate_refund(deposit_amount: float, cancelled_reason: str, technician_departed: bool = False) -> float:
    if technician_departed:
        return 0.0
    if cancelled_reason == 'customer_cancelled':
        return deposit_amount
    return 0.0
