from app import app
from app.models import Case
from flask import render_template, redirect, url_for


@app.route('/cases', methods=['GET'])
@app.route('/cases/', methods=['GET'])
def fncases():
    cs: Case = Case()
    cases: list[Case] = cs.fetchall()
    if cases[0]:
        return render_template('/client/cases.html', cases=cases[1])
    else:
        return redirect(url_for('index'), 302)
    


@app.route('/case/<id>', methods=['GET'])
@app.route('/case/<id>/', methods=['GET'])
def fncase(id: str):
    if not id.isdigit():
        return redirect(url_for('fncases'))

    id: int = int(id)
    cs: Case = Case()
    cs = cs.fetch_by_index(id) 
    if cs[0]:
        return render_template('/client/case/case.html', Case=cs[1])
    else:
        return redirect(url_for('fncases'), 302)
