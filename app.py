from flask import Flask, redirect, render_template, request, flash
from surveys import surveys


app = Flask(__name__)
app.secret_key = '5199de0f44a42e59a95c8984354ab177'

responses = []

@app.route('/')
def welcome():
  return render_template('welcome.html',survey = surveys['satisfaction'])

@app.route('/questions/<num>')
def question(num):
  if len(responses) == len(surveys['satisfaction'].questions):
    flash("You are trying to access an invalid question!")
    return redirect('/thankyou')

  if int(num) == len(responses):
    return render_template('question.html',survey = surveys['satisfaction'], num = int(num))
  else: 
      num = len(responses)
      flash("You are trying to access an invalid question!")
      return render_template('question.html',survey = surveys['satisfaction'], num = int(num))

@app.route('/answer/<num>', methods=['GET', 'POST'])
def answer(num):
  responses.append(request.form['answer'])
  new_num = int(num) + 1 
  if new_num < len(surveys['satisfaction'].questions):
    return redirect(f"/questions/{str(new_num)}")
  else: return redirect('/thankyou')

@app.route('/thankyou')
def thankyou():
  return render_template('thankyou.html')