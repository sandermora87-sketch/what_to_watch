from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#from what_to_watch.settings import Config
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from settings import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from . import views, models, error_handlers, cli_commands, forms

if __name__ == '__main__':
    app.run()
