from flask import Blueprint

# Create a Blueprint instance for the main routes
main = Blueprint('main', __name__)


# Import route modules to register their routes with the blueprint
from app.routes import user_routes, chat_routes, notification_routes

# Register routes from each module with the blueprint
# These modules will use the 'main' blueprint for their routes
user_routes.register(main)
chat_routes.register(main)
notification_routes.register(main)

# The Blueprint 'main' will then be registered with the app in app/__init__.py
