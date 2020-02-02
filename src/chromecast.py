import connexion

from flask_cors import CORS


# Set up OpenAPI specification to Flask Application
connexion_app = connexion.FlaskApp(__name__, specification_dir='./openapi/')
flask_app = connexion_app.app
flask_app.config['JSON_AS_ASCII'] = False  # Needed for proper UTF-8 support
connexion_app.add_api('openapi.yaml', arguments={'title': 'Chromecast API'})

# Set up CORS to Flask application
CORS(flask_app)
