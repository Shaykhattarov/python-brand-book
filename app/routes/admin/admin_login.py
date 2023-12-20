from app import app
from app.forms import LoginForm
from app.models import Admin
from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user


@app.route('/admin/login', methods=['GET', 'POST'])
@app.route('/admin/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin(login=form.login.data, password=form.password.data)
        is_exist: tuple= admin.is_exists()
        if is_exist[0]:
            login_user(is_exist[1])
            return redirect(url_for('admin_index'))
        else:
            if is_exist[1] is None:
                flash('Неправильное имя или email')
            else:
                flash('Произошла ошибка авторизации')
            return redirect(url_for('login'))
    
    return render_template('/admin/authorization.html', form=form)


@app.route('/admin/logout', methods=['GET', 'POST'])
@app.route('/admin/logout/', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))

