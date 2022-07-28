from flask import jsonify, current_app, g
from pyms.flask.app import Microservice
from database import db

ms = Microservice()
app = ms.create_app()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


if __name__ == '__main__':
    app.run()
    db.init_app(app)
    db.create_all()
