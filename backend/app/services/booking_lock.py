from __future__ import annotations

from datetime import datetime, timedelta, timezone

_LOCKS: dict[str, dict] = {}


def acquire_lock(slot_id: str, expires_in_minutes: int = 10) -> dict:
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=expires_in_minutes)
    _LOCKS[slot_id] = {'slot_id': slot_id, 'expires_at': expires_at.isoformat()}
    return _LOCKS[slot_id]


def is_lock_valid(slot_id: str) -> bool:
    lock = _LOCKS.get(slot_id)
    if not lock:
        return False
    expires_at = datetime.fromisoformat(lock['expires_at'])
    if expires_at.tzinfo is None:
        expires_at = expires_at.replace(tzinfo=timezone.utc)
    return expires_at > datetime.now(timezone.utc)


def release_lock(slot_id: str) -> None:
    _LOCKS.pop(slot_id, None)
