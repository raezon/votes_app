from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def init_db(app):
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}/{}'.format(
        os.getenv('DB_USER', 'test'),
        os.getenv('DB_PASSWORD', 'test'),
        os.getenv('DB_HOST', 'mysql'),
        os.getenv('DB_NAME', 'flask')
    )
    db.init_app(app)
