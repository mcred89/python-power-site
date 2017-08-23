from flask import *
import random

app = Flask(__name__)

@app.route("/")
def pagecreate():
  return render_template('index.html')

@app.route("/workout", methods=['POST'])
def workoutcreate():
  out1 = []
  out2 = []
  out3 = []
  out4 = []
  out5 = []
  out6 = []
  out7 = []
  out8 = []
  out9 = []
  out10 = []
  out11 = []
  out12 = []
  out13 = []
  out14 = []
  out15 = []
  try:
    msq = float(request.form['msq'])
    mbe = float(request.form['mbe'])
    mdl = float(request.form['mdl'])
  except:
    return render_template('error.html')
  if request.form['mainliftchoice'] == 'True':
    mainliftchoice = True
  if request.form['mainliftchoice'] == 'False':
    mainliftchoice = False
  from workout import *
  workoutscript(msq, mbe, mdl, mainliftchoice)
  return render_template('output.html',out1=out1,out2=out2,out3=out3,out4=out4,out5=out5,out6=out6,out7=out7,out8=out8,out9=out9,out10=out10,out11=out11,out12=out12,out13=out13,out14=out14,out15=out15)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

