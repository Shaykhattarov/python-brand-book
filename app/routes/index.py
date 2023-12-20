from app import app, db
from app.models import Discussion
from app.forms import DiscussionForm
from flask import url_for, render_template, redirect



@app.route('/', methods=['GET', 'POST'])
def index():
    form = DiscussionForm()
    if form.validate_on_submit():
        discussion: Discussion = Discussion()
        discussion.name = form.name.data
        discussion.email = form.email.data
        discussion.phone = form.phone.data

        db.session.add(discussion)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('/client/index.html', form=form)