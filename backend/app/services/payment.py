from __future__ import annotations

from app.integrations.payment_gateway import GatewayResult, authorize_and_capture, status_inquiry


def process_payment(amount: float, timeout_seconds: int = 30, simulate_timeout: bool = False) -> GatewayResult:
    return authorize_and_capture(amount, timeout_seconds=timeout_seconds, simulate_timeout=simulate_timeout)


def resolve_payment_result(reference: str | None, timeout_seconds: int = 30, simulate_timeout: bool = False) -> GatewayResult:
    if reference and not simulate_timeout:
        return status_inquiry(reference)
    if not reference and simulate_timeout:
        return process_payment(0, timeout_seconds=timeout_seconds, simulate_timeout=True)
    return process_payment(amount=0, timeout_seconds=timeout_seconds, simulate_timeout=False)
