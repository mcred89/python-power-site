from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def pagecreate():
  return render_template('index.html')


@app.route("/workout", methods=['GET', 'POST'])
def workoutcreate():
  try:
    msq = float(request.form['msq'])
    mbe = float(request.form['mbe'])
    mdl = float(request.form['mdl'])
  except:
    return render_template('error.html')
  mainliftchoice = str(request.form['mainliftchoice'])
  from workout import workoutscript
  outputs = workoutscript(msq, mbe, mdl, mainliftchoice)
  return render_template('output.html', outputs=outputs)

@app.route("/calculators")
def calculators():
  return render_template('calculators.html')

@app.route("/otherprograms")
def otherprograms():
  return render_template('otherprograms.html')

@app.route("/about")
def about():
  return render_template('about.html')

@app.route("/login")
def login():
  return render_template('login.html')

@app.route("/register")
def register():
  return render_template('register.html')


if __name__ == "__main__":
  app.run(debug=True, host='127.0.0.1')
