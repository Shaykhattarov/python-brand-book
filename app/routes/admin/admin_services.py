from app import app, db
from app.forms import ServiceForm
from app.models import Service
from flask import render_template, redirect, url_for, flash
from flask_login import login_required



@app.route('/admin/services')
@app.route('/admin/services/')
@login_required
def admin_services():
    service: Service = Service()
    services = service.fetchall()
    if services[0]:
        return render_template('/admin/admin_services.html', services=services[1])
    else:
        return redirect(url_for('admin_index'), 302)
    

@app.route('/admin/service/create', methods=['GET', 'POST'])
@app.route('/admin/service/create/', methods=['GET', 'POST'])
@login_required
def admin_create_service():
    
    return render_template('/admin/admin_add_service.html')



@app.route('/admin/service/update/<id>', methods=['GET', 'POST'])
@app.route('/admin/service/update/<id>/', methods=['GET', 'POST'])
@login_required
def admin_update_service(id: str):
    if id is None or not id.isdigit():
        return redirect(url_for('admin_services'))
    
    id: int = int(id)
    form = ServiceForm()
    
    if not form.validate_on_submit():
        service: tuple(bool, Service) = Service().fetch_by_index(id)
        if service[0]:
            service: Service = service[1]
            form.name.data = service.name
            form.description.data = service.description
            form.essence.data = service.essence
            form.development_stages.data = service.development_stages
            form.cost_description.data = service.cost_description
            form.cost.data = service.cost
            form.demand.data = service.demand
        else:
            return redirect(url_for('admin_services'))
        return render_template('/admin/admin_update_service.html', form=form)
    
    if form.validate_on_submit():
        service: tuple(bool, Service) = Service().update_by_index(id, form)
        if service[0]:
            flash("Данные успешно изменены")
        else:
            flash('При изменении данных произошла ошибка')
        
        return render_template('/admin/admin_update_service.html', form=form)
    

    

