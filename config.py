import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI: str = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'database.db')
    SECRET_KEY: str = "SsMuQSiVvPYFVpPeydAzjygKYn9W2PON"
    UPLOAD_FOLDER: str = os.path.join(basedir, 'app/static/images')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}