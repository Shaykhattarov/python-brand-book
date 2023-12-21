#!flask/bin/python
import unittest
import os

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from config import basedir
from app import app, db


class ClientTestCase(unittest.TestCase):

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

    def test_index(self):
        page = self.app.get('/')
        self.assertEqual(page.status_code, 200)

    def test_discussion_form(self):
        pass

    def test_services(self):
        page = self.app.get('/services')
        if page.status_code != 302:
            self.assertEqual(page.status_code, 200)
        else:
            self.assertEqual(page.status_code, 302)

    def test_cases(self):
        page = self.app.get('/cases')
        if page.status_code != 302:
            self.assertEqual(page.status_code, 200)
        else:
            self.assertEqual(page.status_code, 302)

    def test_contacts(self):
        page = self.app.get('/contacts')
        self.assertEqual(page.status_code, 200)

    