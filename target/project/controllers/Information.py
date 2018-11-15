# -*- coding: utf-8 -*-
#eWFtbDogISFweXRob24vb2JqZWN0L2FwcGx5Om9zLnN5c3RlbSBbInNsZWVwIDEwIl0= || yaml: !!python/object/apply:os.system ["sleep 10"]
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
            yaml_file = base64.b64decode(input)
            content = yaml.load(yaml_file)
    except:
            content = "The application was unable to unsserialize object!"
    return render_template("information/index.html", content = content['yaml'])
 
