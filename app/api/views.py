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


@ns1.route('/')
class User(Resource):
    @ns1.doc('get_user')
    def get(self):
        return {'hello': 'world'}