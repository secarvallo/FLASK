from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        from app.models.model_catalog import Producto
        db.create_all()

        from app.views.view_catalog import catalog_bp as c_bp
        app.register_blueprint(c_bp)

    return app                                                                        