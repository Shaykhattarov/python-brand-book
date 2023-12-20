from app import app
from flask import render_template
from flask_login import login_required


@app.route('/admin', methods=['GET', 'POST'])
@app.route('/admin/', methods=['GET', 'POST'])
@login_required
def admin_index():
    return render_template('/admin/admin.html')