import os

import boto3
from flask import Flask, render_template, request, url_for, flash, redirect, session
from flask_wtf.csrf import CSRFProtect
from forms import RegistrationForm, LoginForm, MaxesForm
from utils import get_secret_key, DynamoDB

app = Flask(__name__)

# Set variables for secret key retrieval from secrets manager
secret_name = os.getenv('ENV_SECRET_NAME')
secret_key = os.getenv('ENV_SECRET_KEY')
# AWS region variable
region = os.getenv('ENV_REGION')
# Name of DyanmoDB user table
usertable = os.getenv('USER_TABLE')

# Initialize table object
db = DynamoDB(table_name=usertable)

# Get flask secret key
if usertable == 'LOCAL':
    app.config['SECRET_KEY'] = "123456789"
else:
    app.config['SECRET_KEY'] = get_secret_key(secret_name, secret_key, region)
# Not 100% sure why this is here commenting out for now
#    app.secret_key = get_secret_key(secret_name, secret_key, region)

@app.route("/", methods=['GET', 'POST'])
def home():
  form = MaxesForm()
  return render_template('maxinput.html', form=form)


@app.route("/workout", methods=['GET', 'POST'])
def workoutcreate():
  form = MaxesForm(request.form)
  try:
    msq = float(form.msq.data)
    mbe = float(form.mbe.data)
    mdl = float(form.mdl.data)
    mainliftchoice = form.mainliftchoice.data
    if mainliftchoice == 'None':
      mainliftchoice = "high"
  except:
    return render_template('error.html')
  from workout import workoutscript
  outputs = workoutscript(msq, mbe, mdl, mainliftchoice)
  return render_template('output.html', outputs=outputs, form=form)

@app.route("/calculators")
def calculators():
  return render_template('calculators.html')

@app.route("/about")
def about():
  return render_template('about.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = db.get_user(email=form.email.data)
    if form.email.data == user['email'] and form.password.data == user['password']:
      flash('You have been logged in!', 'success')
      return redirect(url_for('home'))
    else:
      flash('Login Failed', 'danger')
  return render_template('login.html', form=form)

@app.route("/myprogram")
def myprogram():
  return render_template('myprogram.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    email = form.email.data
    password = form.password.data
    db.create_user(email=email, password=password)
    flash(f'Account created for {form.email.data}', 'success')
    return redirect(url_for('home'))
  return render_template('register.html', form=form)


if __name__ == "__main__":
  # Configure for DynamoDB local
  client = boto3.client('dynamodb', endpoint_url='http://localhost:8000')
  tables = client.list_tables()
  # Create table if it doesn't exist
  if 'LOCAL' not in tables['TableNames'][0]:
    client.create_table(
      TableName='LOCAL',
      AttributeDefinitions=[
        {
          'AttributeName': 'email',
          'AttributeType': 'S'
        }
      ],
      KeySchema=[
        {
          'AttributeName': 'email',
          'KeyType': 'HASH'
        }
      ],
      ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
      }
    )
  app.run(debug=True, host='127.0.0.1')
