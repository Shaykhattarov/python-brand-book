from app import app
from app.models import Service
from flask import url_for, render_template, redirect, url_for

@app.route('/services')
@app.route('/services/')
def fnservices():
    service: Service = Service()
    services: tuple[Service] = service.fetchall()
    if services[0]:
        return render_template('/client/services.html', services=services[1])
    else:
        return redirect(url_for('index'), 302)
    

@app.route('/service/<id>')
@app.route('/service/<id>/')
def fnservice(id: str):
    if not id.isdigit():
        return redirect(url_for('fnservices'), 302)
    
    id: int = int(id)
    service: Service = Service()
    service = service.fetch_by_index(id)
    if service[0]:
        return render_template('/client/service/service.html', service=service[1])
    else:
        return redirect(url_for('fnservices'), 302)
