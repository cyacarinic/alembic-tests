import falcon
import json
import os
import utils
from dicttoxml import dicttoxml


class RequireJSON(object):

    def process_request(self, req, resp):
        if not req.client_accepts_json and not req.client_accepts_xml:
            raise utils.HTTPException(406,
                "This API only supports responses encoded as JSON or XML",
                "This API only supports responses encoded as JSON or XML")
        if req.method in ('POST', 'PUT'):
            if 'application/json' not in req.content_type:
                raise falcon.HTTPUnsupportedMediaType(
                    'This API only supports requests encoded as JSON.',
                    href='http://docs.examples.com/api/json')


class ParseMediaType(object):

    _parse_type = None

    def process_request(self, req, resp):
        path, ext = os.path.splitext(req.path)
        self._parse_type = ext.lstrip(".") if ext else None

    def process_response(self, req, resp, resource):
        response = resp.body
        content_type = resp.content_type

        # print 'si' if req.client_accepts_json else 'no'

        if req.client_accepts_xml:
            content_type = "application/xml"
            response = dicttoxml(resp.body)

        if req.client_accepts_json or self._parse_type == "json":
            content_type = "application/json"
            response = json.dumps(resp.body)

        if self._parse_type == "xml":
            content_type = "application/xml"
            response = dicttoxml(resp.body)

        resp.content_type = content_type
        resp.body = response
