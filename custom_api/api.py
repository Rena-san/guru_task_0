import logging

import requests

from utils.utiles import Api


def get_users():
    url = f"{Api.LOCAL_HOST}/users"

    logging.info(f"GET->URL::{url}")

    response = requests.get(url)

    logging.info(f"RESPONSE::{response.json()}")

    return response


def get_user(user_id):
    url = f"{Api.LOCAL_HOST}/users/{user_id}"

    logging.info(f"GET->URL::{url}")

    response = requests.get(url)

    logging.info(f"RESPONSE::{response.json()}")

    return response
