import os
import sys
from falcon import API
from falcon_utils import helpers, middlewares, utils
from api.routes import add_routes

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, 'api'))

application = API(
    router=utils.CustomRouter(),
    middleware=[
        middlewares.RequireJSON(),
        middlewares.ParseMediaType(),
    ]
)

application.add_error_handler(utils.HTTPException)

add_routes(application)
