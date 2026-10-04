from __future__ import annotations

from datetime import datetime, timedelta

from app.schemas.booking import AvailabilitySlot


def get_available_slots(service_type: str, date: str | None = None) -> list[AvailabilitySlot]:
    base_day = datetime.fromisoformat(date) if date else datetime.utcnow()
    slots: list[AvailabilitySlot] = []
    for index in range(6):
        start = base_day.replace(hour=9, minute=0) + timedelta(hours=index * 2)
        end = start + timedelta(hours=1)
        slots.append(
            AvailabilitySlot(
                slot_id=f'{service_type}-{index}',
                technician_id=f'tech-{(index % 3) + 1}',
                start=start,
                end=end,
                available=True,
            )
        )
    return slots
