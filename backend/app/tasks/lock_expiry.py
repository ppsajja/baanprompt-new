from __future__ import annotations

from app.services.booking_lock import is_lock_valid, release_lock


def expire_lock_if_needed(slot_id: str) -> bool:
    if not is_lock_valid(slot_id):
        release_lock(slot_id)
        return True
    return False
