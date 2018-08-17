from flask import Blueprint
import logging
from flask_restplus import Api

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}
log = logging.getLogger(__name__)
blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint, authorizations=authorizations, version='1.0', title='stackoverflow-lite restplus api',
          description=(
            "It an api for stackoverflow-lite .\n\n"
            "It uses jwt"
             ),
    )
