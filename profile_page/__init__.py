from flask import Flask
from flask_session import Session


def create_app(config="profile_page.config.Config"):
    app = Flask(__name__)

    with app.app_context():
        app.config.from_object(config)

        from profile_page.models import db, User, Schedule
        sess = Session()

        db.init_app(app)
        sess.init_app(app)

        from profile_page.utils.initialization import init_template_globals

        init_template_globals(app)

        if app.config.get("DEBUG"):
            User.create_mock_users()
            Schedule.create_mock_schedules()

        from profile_page.auth import auth

        app.register_blueprint(auth)

        return app
