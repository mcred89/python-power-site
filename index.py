from flask import *

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
  from workout import *
  outputs = workoutscript(msq, mbe, mdl, mainliftchoice)
  return render_template('output.html', outputs=outputs)


if __name__ == "__main__":
  app.run(host='0.0.0.0')
