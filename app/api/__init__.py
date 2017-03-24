from flask import Blueprint
from flask_restplus import Namespace, Resource, fields

ns1 = Namespace('users', description='')

from . import views