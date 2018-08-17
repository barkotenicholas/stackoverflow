import logging.config
import os
from flask import Flask
from flask_jwt_extended import JWTManager
from Stackoverflowlite import settings
from Stackoverflowlite.api.flaskrestplus import blueprint, api
from Stackoverflowlite.api.v1.questions.routes import ns as question_namespace

# logging_conf_path = os.path.normpath(os.paimpoth.join(os.path.dirname(__file__), '../logging.conf'))
# logging.config.fileConfig(logging_conf_path)

def configure_app(flask_app):
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
    flask_app.config['JWT_SECRET_KEY'] = settings.JWT_SECRET_KEY
    flask_app.config['JWT_BLACKLIST_ENABLED'] = settings.JWT_BLACKLIST_ENABLED
    flask_app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = settings.JWT_BLACKLIST_TOKEN_CHECKS
    flask_app.config['TESTING'] = settings.TESTING

def initialize_app(flask_app):
    configure_app(flask_app)
    jwt = JWTManager(flask_app)

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        from stackoverflow.api.v1.models import BlackListToken
        nic = decrypted_token['nic']
        return BlackListToken.check_blacklist(nic)

    jwt._set_error_handler_callbacks(api)
    flask_app.register_blueprint(blueprint)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)
    initialize_app(app)


    return app
