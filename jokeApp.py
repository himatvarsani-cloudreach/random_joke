#!//Users/himat.varsani/.pyenv/shims/python

import random

from flask import Flask, request, Response, render_template

app = Flask(__name__)

#Database
#Dictionaires

jokes_db = {
    1: {"joke" : "What does Thor call his underpants? Thunderpants!"},
    2: {"joke" : "I hate Russian dolls...they are so full of themselves…"},
    3: {"joke" : "If Apple made a car, what would it be missing? Windows"},
    4: {"joke" : "Terrible night. I dream't something bit me on the neck. Got up to check, but the mirror wasn't working."},
    5: {"joke" : "Dont ask SQL Developers to help you move furniture, they drop tables"},
}


# @ is a decorator - way to wrap a function and modify it's behavior
@app.route("/")
def index():
    return render_template ("index.html") 


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
    
#CRUD
#Create - post
#Read - GET
#Update - put
#Delete - Get