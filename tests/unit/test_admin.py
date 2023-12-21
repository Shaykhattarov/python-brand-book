#!flask/bin/python
import unittest
import os

from config import basedir
from app import app, db
from app.models import Admin


class AdminTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'tests/test.db')
        app.app_context().push()
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_login(self):
        # Проверка на доступность страницы
        rv = self.app.get('/admin/login')
        self.assertEqual(rv.status_code, 200)

    def test_created_admin(self):
        # Создаем пользователя admin и проверяем его на доступность
        admin = Admin(login='admin', password='admin')
        db.session.add(admin)
        db.session.commit()

        admin = db.session.get(Admin, 1)
        self.assertEqual(admin.password, 'admin')

    def test_index(self):
        """ Доступ без авторизации """
        rv = self.app.get('/admin/index')
        self.assertEqual(rv.status_code, 200)