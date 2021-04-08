import requests
from .. import utils

def get_user(user_id):
    url = utils.create_users_resource_url() + user_id
    response = requests.request('GET', url, headers=utils.create_headers())

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )

    return response.json()