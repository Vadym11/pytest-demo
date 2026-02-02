import os

import requests
from utils.load_settings import settings
from dotenv import load_dotenv

load_dotenv()

class APIHandler:

    def __init__(self):
        self.base_url = settings['api-url']
        self.email = os.environ.get("EMAIL")
        # self.email = settings['email']
        # print(self.email)
        self.password = os.environ.get("PASSWORD_")
        # self.password = settings['password']
        # print(self.password)
        self.token = ''

    def authenticate(self):
        response = requests.post(
            f'{self.base_url}/users/login',
            json={'email': self.email, 'password': self.password },
            )

        body = response.json()

        if not response.ok:
            print(response.status_code)
            raise Exception(body.get('message'))

        self.token = body.get('access_token')

        print('APIHandler: Admin authenticated successfully.')


    def get(self, endpoint, data, headers):
        response = requests.request("GET", self.base_url + endpoint, data=data, headers=headers)
        if response.status_code != 200:
            raise Exception(response.text)

        return response.json()

    def post(self, endpoint, data, headers):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer ${self.token}'
        } | (headers or {})

        response = requests.request("POST", self.base_url + endpoint, data=data, headers=headers)

        if not response.ok:
            raise Exception(response.text)

        return response.json()

    def delete(self, endpoint, headers=None):

        headers = {
          'Content-Type': 'application/json',
          'Authorization': f'Bearer {self.token}'
        } | (headers or {})

        response = requests.request("DELETE", self.base_url + endpoint, params={}, headers=headers)

        if not response.ok:
            raise Exception(response.text)

        if response.status_code == 204:
            return response.status_code

        return response.json()


