from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/',methods = ['GET'])
def index():
    return render_template("survey.html")

@app.route('/submitted', methods=['POST']) #
def create_user():
    #print("Got Post Info")
    session['valid_user'] =True
    session['email'] = request.form['email']
    session['f_name'] = request.form['first_name']
    session['l_name'] = request.form['last_name']
    birthdate = request.form['month']+'/'+request.form['day']+'/'+request.form['year']
    password = request.form['password']
    pass_confirm = request.form['pass_confirm']
    if len(session['email'])<1:
        flash('please put an email')
        session['valid_user'] =False
    elif not EMAIL_REGEX.match(session['email']):
        flash("Invalid Email Address!")
        session['valid_user'] =False
    if len(session['f_name'])<1:
        flash('please enter your name')
        session['valid_user'] =False
    elif session['f_name'].isalpha() == False:
        flash('first name invalid')
        session['valid_user'] =False
    if len(session['l_name'])<1:
        flash('please enter your name')
        session['valid_user'] =False
    elif session['l_name'].isalpha() == False:
        flash('last name invalid')
        session['valid_user'] =False
    if len(password)<8:
        flash('password must be more than 8 characters')
        session['valid_user'] =False
    if (password.islower() == True) and (password.isalpha() == True):
        flash('password must contain an uppercase and numerical value')
        session['valid_user']==False
    if len(pass_confirm)<1:
        flash('please confirm your password')
        session['valid_user'] =False
    if password != pass_confirm:
        flash('passwords do not match')
        session['valid_user'] = False
    if session['valid_user'] == True:
        flash('successfully submitted form!')
        return render_template("code.html",password=password,pass_confirm=pass_confirm,birthdate=birthdate)
    else:
        return redirect('/')
@app.route('/danger')
def back():
    print("STAY OUT")
    return redirect('/')
if (__name__=="__main__"):
    # run our server
    app.run(debug=True)