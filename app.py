from flask import Flask
from views import blueprints


def create_app():
    app = Flask(__name__)
    app.config['WTF_CSRF_SECRET_KEY'] = 'A SECRET KEY'

    for bp in blueprints:
        app.register_blueprint(bp)
        bp.app = app

    return app


def check_maintenance_times(x, y):
    z = []
    for i in range(len(x)):
        for j in range(len(x[i])):
            z.append(x[i][j]) if not x[i][j] in z else ""
    z.sort()
    y.sort()
    return z == y


if __name__ == "__main__":
    app = create_app()
    app.config['SECRET_KEY'] = 'Secret Key'
    app.run()

