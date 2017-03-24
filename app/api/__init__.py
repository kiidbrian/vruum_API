from flask import Blueprint
from flask_restplus import Namespace, Resource, fields

ns1 = Namespace('users', description='Users related operations')

from . import views