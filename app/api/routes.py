import settings
from resources.item import ItemsCollectionResource

def add_routes(app):
    app.add_route('/items', ItemsCollectionResource())
