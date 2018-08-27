import boto3
from botocore.exceptions import ClientError
from flask import render_template, request, url_for, flash, redirect, session
from workoutgenerator import app, db, bcrypt
from workoutgenerator.forms import RegistrationForm, LoginForm, MaxesForm

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
  from workoutgenerator.workout import workoutscript
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
    try:
      if form.email.data == user['email'] and bcrypt.check_password_hash(user['password'], form.password.data):
        flash('You have been logged in!', 'success')
        return redirect(url_for('home'))
    except ValueError:
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
    password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    try:
      db.create_user(email=email, password=password)
      flash(f'Account created for {form.email.data}', 'success')
      return redirect(url_for('login'))
    except ClientError as e:
      if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
        flash(f'{form.email.data} is already taken', 'danger')
      else:
        flash(f'Something Went Wrong', 'danger')
        redirect(url_for('register'))
  return render_template('register.html', form=form)