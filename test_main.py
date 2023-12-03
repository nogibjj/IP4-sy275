import pytest
from app import app  # import your Flask app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            # initialize here if needed
            pass
        yield client


def test_home_page(client):
    """Test the home page."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"CHAT WITH ME" in response.data
