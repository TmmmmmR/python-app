from project import app
from project.models.Messaging import *
from flask import render_template, request, redirect, session, make_response
import os

@app.route("/monitoring", methods=['GET'])
def monitor():
    return render_template("monitoring/index.html")

@app.context_processor
def utility_processor():
    def system_call(command):
        output = os.popen(command).read()
        return output
    return dict(system_call=system_call)