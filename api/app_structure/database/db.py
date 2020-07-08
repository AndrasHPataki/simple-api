from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def run_db(app):
    db.init_app(app)
    
