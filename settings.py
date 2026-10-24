import sys
import importlib
from what_to_watch.settings import Config
settings_module = importlib.import_module('what_to_watch.settings')
sys.modules['opinions_app.settings'] = settings_module

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
