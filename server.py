from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
# our index route will handle rendering our form
@app.route('/',methods = ['GET'])
def index():
    return render_template("survey.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/submitted', methods=['POST']) #
def create_user():
    #print("Got Post Info")
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['lang'] = request.form['coding_language']
    session['comment'] = request.form['comment']
    if len(session['name'])<1:
        flash('empty name')
        return redirect('/')
    elif len(session['comment'])<1:
        flash('empty comment')
        return redirect('/')
    elif len(session['comment'])>120:
        flash('comment too long, shorten to 120 characters')
        return redirect('/')
    else:
        flash('successfully submitted form!')
        return render_template("code.html")
@app.route('/danger')
def back():
    print("STAY OUT")
    return redirect('/')
if (__name__=="__main__"):
    # run our server
    app.run(debug=True)