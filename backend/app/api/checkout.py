from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.integrations.payment_gateway import GatewayResult
from app.services.payment import process_payment, resolve_payment_result

router = APIRouter(prefix='/api/v1')


@router.post('/checkout')
def submit_payment(booking_id: str, amount: float, simulate_timeout: bool = False, reference: str | None = None) -> dict:
    if amount <= 0:
        raise HTTPException(status_code=400, detail='amount must be greater than zero')

    result: GatewayResult = (
        resolve_payment_result(reference, timeout_seconds=30, simulate_timeout=simulate_timeout)
        if simulate_timeout or reference
        else process_payment(amount, timeout_seconds=30, simulate_timeout=False)
    )

    return {
        'booking_id': booking_id,
        'amount': amount,
        'gateway_status': result.status,
        'gateway_ref': result.gateway_ref,
        'message': result.message,
    }
