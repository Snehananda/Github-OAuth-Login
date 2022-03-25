from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
from time import time
from random import random
from flask import Flask, render_template, make_response
from flask_dance.contrib.github import make_github_blueprint, github

import os 
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
app.config["SECRET_KEY"]="SECRET_KEY"

github_blueprint = make_github_blueprint(client_id='CLIENT_ID', client_secret='CLIENT_SECRET')

app.register_blueprint(github_blueprint, url_prefix='/github_login')


@app.route('/')
def login():

    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get('/user')
        if account_info.ok:
            account_info_json = account_info.json()
            return "<h1>Successfull Login..</h1><br><h2>Your GitHub name is: {}</h2>".format(account_info_json)
 
    return "Failed to login"

if __name__ == "__main__":
    app.run(debug=True)