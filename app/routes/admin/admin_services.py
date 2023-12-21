from app import app, db
from app.forms import ServiceForm
from app.models import Service
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required
from werkzeug.utils import secure_filename
from werkzeug.datastructures.file_storage import FileStorage
import uuid
import os


def allowed_file(filename: str):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def upload_file(file: FileStorage):
    if file.filename is None or len(file.filename) == 0:
        return (False, None)
    
    if allowed_file(file.filename):
        filename = f"{uuid.uuid4()}.{file.filename.rsplit('.', 1)[1].lower()}"
        with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'wb') as fs:
            fs.write(file.stream.read())
        return (True, filename)

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
    form = ServiceForm()

    if form.validate_on_submit():   
        imagename = upload_file(request.files.get('image'))
        if not imagename[0]:
            flash('Изображение не было загружено')
            return redirect(url_for('admin_create_service'))
        
        service: Service = Service()
        service.name = form.name.data
        service.image = imagename[1]
        service.description = form.description.data
        service.essence = form.essence.data
        service.development_stages = form.development_stages.data
        service.cost_description = form.cost_description.data
        service.cost = form.cost.data
        service.demand = form.demand.data
        try:
            db.session.add(service)
            db.session.commit()
        except Exception as err:
            print(err)
            flash('Такая услуга уже существует')

        flash('Данные успешно сохранены')
    return render_template('/admin/admin_add_service.html', form=form)



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
        imagename = upload_file(request.files.get('image'))
        print(imagename)
        if not imagename[0]:
            form.image.data = None
        else:
            form.image.data = imagename[1]
        service: tuple(bool, Service) = Service().update_by_index(id, form)
        if service[0]:
            flash("Данные успешно изменены")
        else:
            flash('При изменении данных произошла ошибка')
        
        return render_template('/admin/admin_update_service.html', form=form)
    


@app.route('/admin/service/delete/<id>', methods=['GET', 'POST'])
@app.route('/admin/service/delete/<id>/', methods=['GET', 'POST'])
@login_required
def admin_delete_service(id: str):
    if id is None or not id.isdigit():
        return redirect(url_for('admin_services'))
    
    id: int = int(id)
    service: tuple(bool, Service) = Service().fetch_by_index(id)
    if service[0]:
        service: Service = service[1]

        db.session.delete(service)
        db.session.commit()

        return redirect(url_for('admin_services'))
    else:
        return redirect(url_for('admin_index'))

    

