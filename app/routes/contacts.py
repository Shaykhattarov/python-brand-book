from app import app
from flask import url_for, render_template


@app.route('/contacts', methods=['GET'])
def contacts():
    return render_template('/client/contacts.html')