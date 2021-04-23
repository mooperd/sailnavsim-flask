"""Initialize app."""
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    """Construct the core app object."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from . import api
        from . import pages
        from . import auth
        from .assets import compile_static_assets
        from .import_data import import_boats, import_users

        # Register Blueprints
        
        app.register_blueprint(api.api_bp)
        app.register_blueprint(pages.pages_bp)
        app.register_blueprint(auth.auth_bp)
        
        
        # Create Database Models
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///meow.db"
        print("creating database about now")
        db.create_all()

        # Import some test data
        try:
            import_boats()
        except:
            print("There was an error importing boat types. Data probably already exists")
        try:
            import_users()
        except:
            print("There was an error importing users. Data probably already exists")

        # Compile static assets
        print("running compile_static_assets")
        compile_static_assets(app)

        return app
