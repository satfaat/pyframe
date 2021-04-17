from flask import Flask
from flask_moment import Moment


app = Flask(__name__)
moment = Moment(app)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
app.config['SECRET_KEY'] = mykey

from fapl import views