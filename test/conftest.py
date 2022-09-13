import pytest
import sys
sys.path.insert(0, "/app")
from app import app

@pytest.fixture()
def app():
    app = a
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()