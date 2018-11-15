# -*- coding: utf-8 -*-
from project import app
from project.models.Dashboard import *
from flask import render_template, request, render_template_string, make_response, redirect, session
import uuid

@app.route("/login", methods=['GET', 'POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if(password == "admin" and username == "admin"):
        random = uuid.uuid1()
        response = make_response(redirect('/confidential'))
        session['loggedin'] = random
        return response
    if request.method == 'POST':
        if(password == "admin" or username != "admin"):
            return render_template("login/index.html", error = "invalid username")
        if(password != "admin" or username == "admin"):
            return render_template("login/index.html", error = "invalid password for username")
    else:
        return render_template("login/index.html")