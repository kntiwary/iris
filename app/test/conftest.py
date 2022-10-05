__author__ = 'kamta'

import pytest

# from app.main import create_app
from manage import app


@pytest.fixture(scope='module')
# @pytest.fixture(scope='session')
def test_client():
    app.config.from_object('app.main.config.TestingConfig')

    # Create a test client using the Flask application configured for testing
    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            yield testing_client  # this is where the testing happens!

