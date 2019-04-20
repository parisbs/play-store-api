import pytest

from config import Test
from play_store_api import create_api


@pytest.fixture(scope='session', name='app')
def fixture_app():
    app = create_api(Test)
    context = app.app_context()
    context.push()
    yield app
    context.pop()
