# -*- coding: utf-8 -*-

# from scripts import tabledef
# from scripts import forms
from scripts import db as db
from scripts import image as image
from flask import Flask, redirect, url_for, render_template, request, session
import json
import sys
import os


app = Flask(__name__)


# ======== Routing =========================================================== #
# -------- Login ------------------------------------------------------------- #
@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

# -------- Settings ---------------------------------------------------------- #
@app.route('/patient', methods=['POST'])
def add_patient():
    req_data = request.get_json()
    db.add_patient(req_data)
    return redirect(url_for('login'))

@app.route('/card', methods=['POST'])
def get_card():
    req_data = request.get_json()
    patient = image.get_card_info(req_data)
    return json.dumps(patient)


# ======== Main ============================================================== #
if __name__ == "__main__":
    app.secret_key = os.urandom(12)  # Generic key for dev purposes only
    app.run(debug=True, use_reloader=True)
