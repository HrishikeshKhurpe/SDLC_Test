import os
from flask import Flask
from src.calculator.routes import calculator_bp

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(calculator_bp, url_prefix='/calculator')

    # Configuration
    app.config['DEBUG'] = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")

    @app.route("/")
    def index():
        return "Calculator API is running!"

    return app

app = create_app()

if __name__ == "__main__":
    # Use Gunicorn or another production-ready server in production
    app.run(host="0.0.0.0", port=5000)
