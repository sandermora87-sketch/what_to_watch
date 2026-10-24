from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from settings import Config


app = Flask(__name__)

app.config.from_object(Config)
# app.config['SECRET_KEY'] = 'SECRET KEY'

db = SQLAlchemy(app)

migrate = Migrate(app, db)


from . import views, models, error_handlers, cli_commands, forms  # noqa: E402

# def create_app(config_object=Config):
#     app = Flask(__name__)
#     app.config.from_object(config_object)
#     db.init_app(app)
#     migrate.init_app(app, db)
#     from . import cli_commands, error_handlers, forms, models, views
#     return app


if __name__ == '__main__':
    app.run()
