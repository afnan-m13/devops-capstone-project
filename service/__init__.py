from flask import Flask
from flask_talisman import Talisman

def create_app():
    app = Flask(__name__)

    # Enable security headers
    Talisman(app)

    @app.route("/")
    def index():
        return {"message": "Accounts service running"}

    return app
