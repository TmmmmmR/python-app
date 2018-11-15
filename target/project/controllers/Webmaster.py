# -*- coding: utf-8 -*-
from project import app
from project.models.Dashboard import *
from flask import render_template, request, render_template_string, make_response, redirect, session
import uuid

@app.route("/webmaster", methods=['GET', 'POST'])
def obscurity():
    search = request.form.get('search')
    random = uuid.uuid1()
    response = make_response(render_template("webmaster/index.html"))
    session['loggedin'] = random
    return response
