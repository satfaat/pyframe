import os

from fapl import create_app
#from fapl.models import User, Role
#from flask_migrate import Migrate


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
#migrate = Migrate(app, db)

#@app.shell_context_processor
#def make_shell_context():
#    return dict(User=User, Role=Role)