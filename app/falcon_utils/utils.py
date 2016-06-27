import os
import json
from api import settings
from falcon.routing import CompiledRouter


class HTTPException(Exception):

    def __init__(self, status_code, dev_msg="", user_msg="", error_code="",
                 more_info=""):
        self.status_code = status_code
        self.dev_msg = dev_msg
        self.user_msg = user_msg
        self.error_code = error_code
        self.more_info = more_info

    @staticmethod
    def handle(ex, req, resp, params):
        response = { "status": ex.status_code }
        if ex.dev_msg:
            response.update({ "devMessage": ex.dev_msg })
        if ex.user_msg:
            response.update({ "userMessage": ex.user_msg })
        if ex.error_code:
            response.update({ "errorCode": ex.error_code })
        if ex.more_info:
            response.update({ "moreInfo": ex.more_info })

        resp.body = response
        resp.status = str(ex.status_code)


class CustomRouter(CompiledRouter):

    def add_route(self, uri_template, method_map, resource):
        uri_template = '/v%s%s' % (settings.VERSION, uri_template)
        return super(CustomRouter, self).add_route(uri_template, method_map, resource)

    def find(self, uri):
        path, ext = os.path.splitext(uri)
        return super(CustomRouter, self).find(path)
