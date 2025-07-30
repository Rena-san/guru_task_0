import logging

import pytest
from user_data.user_model import get_user


@pytest.fixture(scope="session")
def user_data():
    user = get_user()
    logging.info(f"USER DATA: {user.model_dump_json()}")
    return user