from flask import jsonify
from config import config
from threading import Thread
from werkzeug.utils import secure_filename
from . import api
from datetime import datetime
from app import db
from models import *

import re
import json
import requests

@api.route('/login', methods=['POST'])
def login(Resource):
    pass