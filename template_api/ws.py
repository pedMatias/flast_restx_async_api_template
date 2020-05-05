from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

from template_api.async_endpoint_1.ws import api as endpoint_1_api
from template_api import settings


class CustomApi(Api):
    @property
    def specs_url(self):
        """
        The Swagger specifications absolute url (ie. `swagger.json`)
        :rtype: str
        """
        return url_for(self.endpoint('specs'), _external=False)


app = Flask(__name__)

# Database cursor:
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = settings.DB_URI
db = SQLAlchemy(app)

# Flask Rest X:
api = CustomApi(
    app,
    version=settings.API["version"],
    title=settings.API["name"],
    description=settings.API["description"],
)

# Define available API namespaces
api.add_namespace(endpoint_1_api)
