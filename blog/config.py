import os

class Config :
    SECRET_KEY='a3ab9ba58d166b8064117b6f628da7a7'
    SQLALCHEMY_DATABASE_URI= 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
