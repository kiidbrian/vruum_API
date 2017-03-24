from flask import jsonify
from config import config
from threading import Thread
from flask_restplus import Namespace, Resource, fields
from werkzeug.utils import secure_filename
from datetime import datetime
from app.__init__ import db
from app.__init__ import ns1
from models import *

import re
import json
import requests

user_fields = ns1.model('User', {
    'firstName': fields.String(required=True, description="First name of user"),
    'lastName': fields.String(required=True, description="Last name of user"),
    'occupation': fields.String(required=True, description="Occupation of user"),
    'homeAddress': fields.String(required=False, description="Home address of user"),
    'workAddress': fields.String(required=False, description="Work address of user"),
    'gender': fields.Boolean(required=False, description="Gender of user"),
    'email': fields.String(required=True, description="Email of user"),
    'msisdn': fields.String(required=False, description="Phone number of user"),
    'password': fields.String(required=True, description="First name of user")
})

@ns1.route('/')
class UserList(Resource):
    '''Creates and shows a list of users'''
    @ns1.doc('list_users')
    def get(self):
        '''List all users '''
        return {'hello': 'world'}

    @ns1.doc('create_user')
    @ns1.expect(user_fields)
    @ns1.marshal_with(user_fields)
    def post(self):
        '''Create a new user'''
        return "New user created"


@ns1.route('/<int:id>')
class User(Resource):
    '''Show a single user item, update and delete'''
    @ns1.doc('list_users')
    def get(self, id):
        '''Fetch a given resource'''
        return {'hello': 'world'}

    @ns1.doc('update_user')
    @ns1.expect(user_fields)
    @ns1.marshal_with(user_fields)
    def put(self, id):
        '''Update user given its identifier'''
        return "Updated user with id"
    
    @ns1.doc('delete_user')
    @ns1.response(204, 'User deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        return "",204
