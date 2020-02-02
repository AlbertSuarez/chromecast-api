import connexion

from flask import Response
from flask_cors import CORS


# Set up OpenAPI specification to Flask Application
from src import DOCS_HTML_FILE_PATH

connexion_app = connexion.FlaskApp(__name__, specification_dir='./openapi/')
flask_app = connexion_app.app
flask_app.config['JSON_AS_ASCII'] = False  # Needed for proper UTF-8 support
connexion_app.add_api('openapi.yaml', arguments={'title': 'Chromecast API'})

# Set up CORS to Flask application
CORS(flask_app)


@flask_app.route('/docs')
def index():
    with open(DOCS_HTML_FILE_PATH, 'r') as html_file:
        html_content = str(html_file.read())
    response = Response(html_content)
    response.headers['Content-Type'] = 'text/html'
    return response, 200
