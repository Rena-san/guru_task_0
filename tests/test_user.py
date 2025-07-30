import http

import allure
from custom_api.api import get_users, get_user

def test_get_all_users():
    with allure.step("Get all users"):
        response = get_users()
        with allure.step("Assert status code"):
            assert response.status_code == http.HTTPStatus.OK.value
        with allure.step("Assert users quantity"):
            users_quantity = 4
            assert len(response.json().get("data")) == users_quantity, "Incorrect number of users"

def test_get_user():
    with allure.step("Get user"):
        response = get_user(user_id=2)
        with allure.step("Assert status code"):
            assert response.status_code == http.HTTPStatus.OK.value
        with allure.step("Assert user email"):
            assert response.json().get("data").get("email") == "lindsay.ferguson@reqres.in"
