from datetime import datetime
from flask.globals import request

from flask import render_template, session, redirect, url_for

from . import main
#from .forms import NameForm
from .. import db
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
        'template_name': 'base.html'
    }
    return render_template(
        data['template_name'],
        title='Home Page',
        year=datetime.now().year,
    )


@main.route('/info')
def info():

    data = {
        'template_name': 'info.html',
        'title': 'Info',
        'user_agent': request.headers.get('User-Agent'),
        'current_time': datetime.utcnow()
    }
    return render_template(data['template_name'],
                            data = data,)