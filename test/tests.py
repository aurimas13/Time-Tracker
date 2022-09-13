import pytest
from app import app

@pytest.fixture()
def app():
    app = app()
    app.config.update({
        "TESTING": True,
    })

    yield app

# @pytest.fixture()
# def client(app):
#     return app.test_client()
#
#
# @pytest.fixture()
# def runner(app):
#     return app.test_cli_runner()