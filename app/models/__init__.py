#!/usr/bin/python3

from app import db
from app.models.user import User
from app.models.message import Message
from app.models.friendship import Friendship

# If there are any relationships between models, they can be defined here or within the model files themselves

# You can also add a function to create all the tables if needed
def create_all():
    db.create_all()


# Export the models for easier access
__all__ = ['User', 'Message', 'Frienship']
