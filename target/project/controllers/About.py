# -*- coding: utf-8 -*-

from project import app
from project.models.Dashboard import *
from flask import request, url_for, render_template, redirect
import pickle, sys, yaml
from io import StringIO  # Python3

@app.route("/about")
def start():
        about_sys = {'system_state': 'Synchronized with App2'}
        with open('../filename.pickle', 'wb') as handle:
            pickle.dump(about_sys, handle, protocol=pickle.HIGHEST_PROTOCOL)
        with open('../filename.pickle', 'rb') as handle:
            a = pickle.load(handle)
        return render_template("about/index.html", content = a)

@app.route("/about/sync", methods=['POST'])
def deserialization_pickle():
    try:
        with open("../pickle.hacker", "wb+") as file:
            att = request.form['data_obj']
            attack = bytes.fromhex(att)
            file.write(attack)
            file.close()
        with open('../pickle.hacker', 'rb') as handle:
            a = pickle.load(handle)
            print(attack)
            return render_template("about/index.html", content = a)
    except:
        return render_template("about/index.html")
    return render_template("about/index.html")