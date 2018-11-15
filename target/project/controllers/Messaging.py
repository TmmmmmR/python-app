from project import app
from project.models.Messaging import *
from flask import render_template, request, redirect, session, make_response
import uuid

@app.route("/messaging", methods=['GET', 'POST'])
def messaging():
    sqli  = Messaging()
    messages = sqli.getMessages()
    return render_template("messaging/index.html", messages = messages)

@app.route("/messaging/new", methods=['GET', 'POST'])
def store_messages():
    name    = request.form.get('name')
    message = request.form.get('message')
    link   = request.form.get('link')
    
    sqli  = Messaging()
    messages = sqli.storeMessages(name, message, link)
    response = make_response(redirect("/messaging"))
    return response