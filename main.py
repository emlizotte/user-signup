from flask import Flask, request, redirect, render_template
import cgi   
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('user_form.html')


@app.route('/validate', methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''


    if len(username) < 3:
        username_error = 'Not a valid username.'
        username = ''
    if len(username) > 20:
        username_error = 'Not a valid username.'
        username = ''

    if len(password) < 3:
        password_error = 'Not a valid password.'
    if len(password) > 20:
        password_error = 'Not a valid password.'
        password = ''
    if " " in password:
        password_error = 'Not a valid password.'
        password = ''

    if password != verify_password: 
        verify_password_error = 'This password is not the same as the previous.'
        verify_password = ''
    
    ##
    if len(email) > 0:
        if len(email) > 20 or len(email) < 3:
            email_error = 'Not a valid email.'
    if " " in email:
        email_error = 'Not a valid password.'
        email= ''
    if "@" not in email:
        email_error = 'Not a valid password.'
        email = ''
    if "." not in email:
        email_error = 'Not a valid password.'
        email = ''

    # The user provides an email, but it's not a valid email. Note: the email field may be left empty, but if there 
    # is content in it, then it must be validated. The criteria for a valid email address in this assignment are that 
    # it has a single @, a single ., contains no spaces, and is between 3 and 20 characters long.

    if (not username_error) and (not password_error) and (not verify_password_error) and (not email_error):
        return welcome()
    else:
        return render_template('user_form.html', username = username, password = password, verify_password = verify_password, email = email,
        username_error = username_error, password_error = password_error, verify_password_error = verify_password_error, 
        email_error = email_error)



@app.route("/welcome" , methods = ['POST'])
def welcome():
    username = request.form['username']
    return render_template('welcome.html', username = username)

app.run()