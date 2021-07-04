"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask.globals import request
from fapl import app


def rec_lnk(req):
    with open('fapl/dt/lnks.txt', 'a') as lnks:
        print(req, file=lnks)


@app.route('/')
@app.route('/index')
def index():
    """Renders the home page."""
    return render_template(
        'base.html',
        title='Home Page',
        year=datetime.now().year,
    )

# app.add_url_rule('/', 'index', index)

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,  {}!</h1>'.format(name)

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.jade',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
    
@app.route('/viewlog')
def view_the_log()-> 'html':
    #with open('vsearch.log') as log:
    #    contents = log.read()
    #return escape(contents)
    contents=[]
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form data', 'Remote addr', 'User agent', 'Results')
    #return str(contents)
    return render_template('viewlog.html', 
                                the_title='View Log',
                                the_row_titles = titles,
                                the_data = contents,)


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')

@app.route('/lnk', methods=['POST'])
def lnk_add_rec() -> 'html':
    link = request.form['link']
    rec_lnk(link)
    with open('fapl/dt/lnks.txt', 'r') as lnks:
        contents = lnks.readlines()
    return render_template('lnk-add.html',
                           the_title='add link',
                           the_link = link,
                           the_links=contents,)

@app.route('/lnk')
def lnk_add() -> 'html':
    return render_template('lnk-add.html',)                  

@app.route('/wrk')
def wrk_show() -> 'html':
    with open('../devops/wrk/tdserebro/data.txt') as wrk:
        contents = wrk.read()
    return render_template('wrk.html',
                            the_title='Notes',
                            content = contents,)

@app.route('/info')
def info():
    user_agent = request.headers.get('User-Agent')
    data = {
        'title': 'Info_1',
        'user_agent': user_agent,
    }
    return render_template('info.html',
                            data = data,
                            current_time=datetime.utcnow())

