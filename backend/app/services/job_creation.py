from __future__ import annotations

from datetime import datetime

from app.models.booking import Booking, Job

_ACTIVE_JOBS: dict[str, Job] = {}


def create_job_from_booking(booking: Booking) -> Job:
    job = Job(
        id=f'job-{booking.id}',
        booking_id=booking.id,
        status='confirmed',
        scheduled_start=booking.slot_start,
        deposit_amount=booking.deposit_amount,
    )
    job.add_history('created')
    _ACTIVE_JOBS[job.id] = job
    return job
