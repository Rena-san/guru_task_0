import logging
import requests

from utils.utiles import Api


def user_registration(user_data):
    url = f"{Api.HOST}/api/register"

    headers = {
        "x-api-key": "reqres-free-v1"
    }

    body = {
        "email": user_data.email,
        "password": user_data.password,
    }

    logging.info(f"POST->URL::{url}")
    logging.info(f"POST->BODY::{body}")

    response = requests.post(url, headers=headers, json=body)

    logging.info(f"RESPONSE::{response.json()}")

    return response

def get_user_info(user_id):
    url = f"{Api.HOST}/api/users/{user_id}"

    logging.info(f"POST->URL::{url}")

    response = requests.get(url)

    logging.info(f"RESPONSE::{response}")

    return response

def user_login(user_data):
    url = f"{Api.HOST}/api/login"

    headers = {
        "x-api-key": "reqres-free-v1"
    }

    body = {
        # "username": user_data.username,
        "email": user_data.email,
        "password": user_data.password,
    }


    logging.info(f"POST->URL::{url}")
    logging.info(f"POST->BODY::{body}")

    response = requests.post(url, headers=headers, json=body)

    logging.info(f"RESPONSE::{response.json()}")

    return response

def user_logout(user_id):
    url = f"{Api.HOST}/api/logout"

    logging.info(f"POST->URL::{url}")

    response = requests.post(url)

    logging.info(f"RESPONSE::{response}")

    return response
