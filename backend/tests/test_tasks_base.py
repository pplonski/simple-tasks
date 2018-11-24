import os
import unittest
import requests


class TestTasksBase(unittest.TestCase):
    def get_server_url(self):
        return os.environ.get("SERVER_URL", "http://0.0.0.0:8000")

    def get_server_ws(self):
        return (
            os.environ.get("SERVER_URL", "http://0.0.0.0:8000").replace("http", "ws")
            + "/websockets/tasks/"
        )

    def create_task(self, arg1, arg2):

        self.assertTrue(self.token)
        data = {"params": {"arg1": arg1, "arg2": arg2}, "parent_organization": 1}
        headers = {"Authorization": "Token " + self.token}
        r = requests.post(
            self.get_server_url() + "/api/dada/tasks", json=data, headers=headers
        )
        if r.status_code != 201:
            print(r.json())
        self.assertEqual(r.status_code, 201)
        return r.json()

    def get_task(self, id):
        self.assertTrue(self.token)
        headers = {"Authorization": "Token " + self.token}
        r = requests.get(
            self.get_server_url() + "/api/tasks/{0}".format(id), headers=headers
        )
        self.assertEqual(r.status_code, 200)
        return r.json()

    def create_user_and_login(self):
        data = {
            "username": "piotrek",
            "email": "piotrek@piotrek.pl",
            "password": "verysecret",
            "organization": "big co",
        }
        r = requests.post(self.get_server_url() + "/users/create", json=data)
        # if r.status_code == 400:
        #    if 'email' in r.json():
        #        # user already exists
        # self.assertEqual(r.status_code, 201)
        r = requests.post(self.get_server_url() + "/auth/token/login", json=data)
        self.assertEqual(r.status_code, 200)

        self.token = r.json().get("auth_token")

        return self.token

    def delete_user(self, token):
        headers = {"Authorization": "Token " + token}
        r = requests.post(self.get_server_url() + "/users/delete", headers=headers)
        self.assertEqual(r.status_code, 204)
