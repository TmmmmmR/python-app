from project import app
from project.models.Dashboard import *
from flask import render_template, request, send_file, make_response, redirect, session
from xml.dom import minidom
import os

from xml.dom.pulldom import START_ELEMENT, parseString

@app.route("/validator", methods=['GET'])
def validator():
    return render_template("validator/index.html")

@app.route("/validator/upload", methods=['GET', 'POST'])
def XML_validator():
    doc = parseString(request.form['customers'])
    try:
        for event, node in doc:
            if event == START_ELEMENT and node.localName == "customers":
                doc.expandNode(node)
                nodes = node.toxml()
                return render_template("validator/index.html", nodes = nodes)
    except:
        return render_template("validator/index.html", error = "Validation failed")
    


@app.route("/validator/getXML", methods=['GET', 'POST'])
def XML_download():
    fileName = request.form['example_file']
    file = open(fileName, "r") 
    response = make_response(send_file(fileName, attachment_filename=fileName))
    response.headers.set("Content-Type", "text/html; charset=utf-8")
    response.headers.set("Content-Disposition", "attachment; filename="+fileName)
    return response

ALLOWED_EXTENSIONS  = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'html'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/validator/uploads", methods=['GET', 'POST'])
def XML_upload():
    if request.method == 'POST':
        file = request.files['file']
        print(file)
        if file and allowed_file(file.filename):
            filename = file.filename
            print(os.path.join)
            file.save('uploads/'+filename)
            uploaded = "File was uploaded succesfully to the application, the staff members will process this information soon!"
            return render_template("validator/index.html",uploaded = uploaded)
        uploaded = "something went wrong, please try again. If the problem is repetitive please contact an administrator!"
        return render_template("validator/index.html",uploaded = uploaded)
    return render_template("validator/index.html")
    