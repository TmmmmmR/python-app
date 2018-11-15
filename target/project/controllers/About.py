# -*- coding: utf-8 -*-
#eWFtbDogISFweXRob24vb2JqZWN0L2FwcGx5Om9zLnN5c3RlbSBbInNsZWVwIDEwIl0= || yaml: !!python/object/apply:os.system ["sleep 10"]
from project import app
from project.models.Dashboard import *
from flask import render_template, request
import _pickle as cPickle
import pickle
from io import StringIO  # Python3
import sys
import yaml
import base64
import json

@app.route("/about/<input>")
def about(input):
        inputstring = base64.b64decode(input)
      
        with open('filename.pickle', 'wb') as handle:
            pickle.dump(inputstring, handle, protocol=pickle.HIGHEST_PROTOCOL)
        with open('filename.pickle', 'rb') as handle:
            final = cPickle.loads(base64.b64decode(input))
            a = final.decode("utf-8")
        return render_template("about/index.html", content = a)


@app.route("/about/<input>", methods=['POST'])
def aboutUpdate():
        with open("pickle.hacker", "wb+") as file:
            att = request.form['data_obj']
            attack = bytes.fromhex(att)
            file.write(attack)
            file.close()
        with open('pickle.hacker', 'rb') as handle:
            a = pickle.load(handle)
            print(attack)
            return render_template("about/index.html", content = a)