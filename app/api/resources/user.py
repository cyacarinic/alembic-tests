import json
from falcon import HTTPError
from falcon_utils import utils


class UsersCollectionResource:

    def on_get(self, req, resp):
        resp.body = {
            "gg": "wp"
        }

    def on_post(self, req, resp):
        resp.body = {"item": "demo"}
