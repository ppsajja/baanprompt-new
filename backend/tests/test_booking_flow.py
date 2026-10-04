from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_availability_endpoint() -> None:
    response = client.get('/api/v1/availability', params={'service_type': 'repair', 'date': '2026-10-05T00:00:00'})
    assert response.status_code == 200
    payload = response.json()
    assert 'slots' in payload and len(payload['slots']) >= 1


def test_booking_and_checkout_workflow() -> None:
    booking_response = client.post(
        '/api/v1/bookings',
        json={
            'customer_id': 'cust-01',
            'service_type': 'repair',
            'address_id': 'addr-01',
            'technician_id': 'tech-1',
            'slot_start': '2026-10-05T09:00:00',
            'slot_end': '2026-10-05T10:00:00',
            'deposit_amount': 1500.0,
        },
    )
    assert booking_response.status_code == 200
    booking_id = booking_response.json()['id']

    payment_response = client.post('/api/v1/checkout', params={'booking_id': booking_id, 'amount': 1500.0})
    assert payment_response.status_code == 200
    assert payment_response.json()['gateway_status'] in {'captured', 'timeout'}

    cancellation_response = client.post(f'/api/v1/bookings/{booking_id}/cancel', params={'reason': 'customer_cancelled'})
    assert cancellation_response.status_code == 200
    assert 'refund_amount' in cancellation_response.json()
