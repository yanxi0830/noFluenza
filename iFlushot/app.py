# -*- coding: utf-8 -*-

from scripts import tabledef
from scripts import forms
from scripts import helpers
from scripts import db as db
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


# ======== Main ============================================================== #
if __name__ == "__main__":
    app.secret_key = os.urandom(12)  # Generic key for dev purposes only
    app.run(debug=True, use_reloader=True)
