from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class GatewayResult:
    status: str
    gateway_ref: str | None = None
    message: str = ''


def authorize_and_capture(amount: float, timeout_seconds: int = 30, simulate_timeout: bool = False) -> GatewayResult:
    if simulate_timeout:
        return GatewayResult(status='timeout', gateway_ref=None, message=f'Gateway timeout after {timeout_seconds} seconds')
    ref = f'gw-{datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")}'
    return GatewayResult(status='captured', gateway_ref=ref, message='Payment captured successfully')


def status_inquiry(reference: str) -> GatewayResult:
    if not reference:
        return GatewayResult(status='not_found', gateway_ref=None, message='Missing reference')
    return GatewayResult(status='captured', gateway_ref=reference, message='Status inquiry succeeded')
