from datetime import datetime

from flask import redirect, render_template, session, url_for
from flask.globals import request

#from .forms import NameForm
from .. import db
from . import main

#from ..models import User


#@main.route('/', methods=['GET', 'POST'])
#def index():
#    form = NameForm()
#    if form.validate_on_submit():

#        return redirect(url_for('.index'))
#    return render_template('index.html',
#                            form=form, name=session.get('name'),
#                            known=session.get('known', False),
#                            current_time=datetime.utcnow())
@main.route('/')
@main.route('/index')
def index():
    """Renders the home page."""
    data = {
        'template_name': 'base.html',
        'title': 'Home Page',
        'year': datetime.now().year,
    }
    return render_template(
        data['template_name'],
        data=data,
    )


@main.route('/info')
def info():
    data = {
        'template_name': 'info.html',
        'title': 'Info_main',
        'user_agent': request.headers.get('User-Agent'),
        'current_time': datetime.utcnow()
    }
    return render_template(data['template_name'],
                            data=data,)


@main.route('/api/data')
def get_data():
    content = main.send_static_file('data.json')
    return content
