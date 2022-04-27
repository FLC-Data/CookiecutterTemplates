from config import Config
from flask import Flask


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Blueprint Api
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
