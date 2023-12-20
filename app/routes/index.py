from app import app
from flask import url_for, render_template



@app.route('/', methods=['GET'])
def index():
    return render_template('/client/index.html')