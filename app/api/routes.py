import settings
from resources.item import ItemsCollectionResource
from resources.user import UsersCollectionResource

def add_routes(app):
    app.add_route('/items', ItemsCollectionResource())
    app.add_route('/users', UsersCollectionResource())
