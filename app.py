from flask import Flask
from bluprients.home import home
from bluprients.member import member
from bluprients.data import data

app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(member)
app.register_blueprint(data)