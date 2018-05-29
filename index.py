from flask import *

app = Flask(__name__)


@app.route("/")
def pagecreate():
  return render_template('index.html')


@app.route("/workout", methods=['POST'])
def workoutcreate():
  try:
    msq = float(request.form['msq'])
    mbe = float(request.form['mbe'])
    mdl = float(request.form['mdl'])
  except:
    return render_template('error.html')
  if request.form['mainliftchoice'] == 'True':
    mainliftchoice = "hivol"
  if request.form['mainliftchoice'] == 'False':
    mainliftchoice = "lowvol"
  from workout import *
  workoutscript(msq, mbe, mdl, mainliftchoice)
  return render_template('output.html', outputs)


if __name__ == "__main__":
  app.run(host='0.0.0.0')
