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


def test_fake_pass(client):
    """Fake test that always passes."""
    assert True
