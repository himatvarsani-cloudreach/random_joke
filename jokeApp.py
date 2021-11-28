#!//Users/himat.varsani/.pyenv/shims/python

import random
import json

from flask import Flask, request, Response, render_template

app = Flask(__name__)

#Database
#Dictionaires

jokes_db = {
    "1": {"joke" : "What does Thor call his underpants? Thunderpants!"},
    "2": {"joke" : "I hate Russian dolls...they are so full of themselves…"},
    "3": {"joke" : "If Apple made a car, what would it be missing? Windows"},
    "4": {"joke" : "Terrible night. I dream't something bit me on the neck. Got up to check, but the mirror wasn't working."},
    "5": {"joke" : "Dont ask SQL Developers to help you move furniture, they drop tables"},
}


# @ is a decorator - way to wrap a function and modify it's behavior
@app.route("/")
def index():
    #for j in jokes_db:
    #print (random.choice(jokes_db.values))
    #html_response = "<p>"
    #for j in jokes_db:
        #print(jokes_db[j])
     #   html_response += jokes_db[j]["joke"]
     #   html_response += "</p>"
        #return render_template ("index.html", jokes=jokes_db[random.choice(j)] ["joke"])
    j = random.choice(list(jokes_db.keys()))
    return render_template ("index.html", jokes=jokes_db[j]["joke"]) 

@app.route("/jokes")
def jokes():
    html_response = "<ul>"
    for j in jokes_db:
        html_response += "<li>" + "<a href='/jokes/" + j + " '>" + jokes_db[j]["joke"] + "</a>" + "</li>"
    html_response += "</ul>"
    html_response += "<a href='/'>Homepage</a>" 
    return html_response

#READ - GET
@app.route("/jokes/<joke_id>")
def get_joke(joke_id):
    return json.dumps([jokes_db[joke_id]])

@app.route("/jokes/add", methods=['POST'])
def add_joke():
    req_data = request.get_json()
    joke = req_data['joke']
    
    new_joke = {"6": joke}
    jokes_db.update(new_joke)
    return "A joke was added successfully"


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)
    
#CRUD
#Create - post
#Read - GET
#Update - put
#Delete - Get