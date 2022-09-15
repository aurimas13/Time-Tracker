import pytest
from dotenv import load_dotenv

load_dotenv(".env.testing")

import app
from app.models import Story


def add_data_fixtures():
    fixture_story = Story(
        estimated_points=10,
        story_name='0',
        status=True,
        description='0'
    )

    app.db.session.add(fixture_story)
    app.db.session.commit()


@pytest.fixture(scope="module", autouse=True)
def test_client():
    add_data_fixtures()
    testing_client = app.app.test_client()
    ctx = app.app.app_context()
    ctx.push()

    yield testing_client

    with app.app.app_context():
        app.db.session.remove()
        app.db.drop_all()

    ctx.pop()


# @pytest.fixture()
# def client(test_client):
#     return test_client.test_client()
#
#
# @pytest.fixture()
# def runner(test_client):
#     return test_client.test_cli_runner()