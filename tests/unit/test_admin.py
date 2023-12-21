#!flask/bin/python
import unittest
import os
from flask_migrate import Migrate

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from config import basedir
from app import app, db
from app.models import Admin


class AdminTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()
        self.db = db

    def tearDown(self):
        self.db.session.rollback()

    def test_login(self):
        # Проверка на доступность страницы
        rv = self.app.get('/admin/login')
        self.assertEqual(rv.status_code, 200)

    def test_created_admin(self):
        # Создаем пользователя admin и проверяем его на доступность
        admin = Admin(login='test_admin', password='test_admin')
        self.db.session.add(admin)
        self.db.session.commit()

        admin = self.db.session.get(Admin, 1)
        self.assertEqual(admin.password, 'admin')

    def test_index(self):
        """ Доступ без авторизации """
        rv = self.app.get('/admin/index')
        self.assertEqual(rv.status_code, 404)