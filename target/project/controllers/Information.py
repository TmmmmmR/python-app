# -*- coding: utf-8 -*-

from project import app
from project.models.Dashboard import *
from flask import render_template, request
import pickle
from io import StringIO  # Python3
import sys
import yaml
import base64

@app.route("/information/<input>", methods=['GET'])
def deserialization(input): 
    try: 
            if not input:
                return render_template("information/index.html")
            yaml_file = base64.b64decode(input)
            content = yaml.load(yaml_file)
    except:
            content = "The application was unable to unsserialize object!"
    return render_template("information/index.html", content = content['yaml'])
    
 
