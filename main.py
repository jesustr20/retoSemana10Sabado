from flask import Flask
from dotenv import load_dotenv
from pathlib import Path
from routes import routeCompany, routeError, routeRole, routeUsers, routeRocous

app = Flask(__name__)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

routeError.error_handler(app)
routeCompany.route(app)
routeRole.route(app)
routeUsers.route(app)
routeRocous.route(app)

if __name__ == '__main__':
    app.run()