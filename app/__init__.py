from flask import Flask

def create_app():
    app = Flask(__name__, template_folder="../templates")  # 👈 specify the templates folder path

    from .routes import bp
    app.register_blueprint(bp)

    return app
