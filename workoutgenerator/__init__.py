import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
from workoutgenerator.utils import get_secret_key, DynamoDB

app = Flask(__name__)

# AWS region variable
region = os.getenv('ENV_REGION')
# Name of DyanmoDB user table
usertable = os.getenv('USER_TABLE')

# Initialize table object
db = DynamoDB(table_name=usertable)

# Used for password encryption
bcrypt = Bcrypt(app)

# Get flask secret key
if usertable == 'LOCAL':
    app.config['SECRET_KEY'] = "123456789"
else:
    secret_name = os.getenv('ENV_SECRET_NAME')
    secret_key = os.getenv('ENV_SECRET_KEY')
    app.config['SECRET_KEY'] = get_secret_key(secret_name, secret_key, region)

from workoutgenerator import routes