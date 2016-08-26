import json
from falcon import HTTPError
from falcon_utils import utils


class ItemsCollectionResource:

    def on_get(self, req, resp):
        resp.body = {
            "metadata": {
                "resultset": {
                    "count": 227,
                    "offset": 0,
                    "limit": 10,
                }
            },
            "results": [
                {
                    "id": "1234",
                    "type": "magazine",
                    "title": "Public Water Systems",
                    "tags": [
                        {"id": "125", "name": "Environment"},
                        {"id": "834", "name": "Water Quality"}
                    ],
                    "created": "2015-06-30T11:29:05"
                },
                {
                    "id": 2351,
                    "type": "magazine",
                    "title": "Public Schools",
                    "tags": [
                        {"id": "125", "name": "Elementary"},
                        {"id": "834", "name": "Charter Schools"}
                    ],
                    "created": "2015-06-30T11:29:05"
                },
                {
                    "id": 2351,
                    "type": "magazine",
                    "title": "Public Schools",
                    "tags": [
                        {"id": "125", "name": "Pre-school"},
                    ],
                    "created": "2015-06-30T11:29:05"
                }
            ]
        }
        # raise utils.HTTPException(404,
        #     "Resource not Found",
        #     "Resource not Found")

    def on_post(self, req, resp):
        resp.body = {"item": "demo"}
