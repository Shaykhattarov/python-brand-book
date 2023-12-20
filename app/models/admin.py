from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash


@login_manager.user_loader
def load_user(admin):
    return db.session.query(Admin).get(int(admin))


class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    login = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def is_exists(self):
        try:
            admin = db.session.query(Admin).filter_by(login=self.login).first()
        except Exception as err:
            print(err)
            return (False, err)
        if admin is not None and check_password_hash(admin.password, self.password):
            return (True, admin)
        else:
            return (False, None)
       
    def __repr__(self) -> str:
        return f'<Admin - {self.login}>'
