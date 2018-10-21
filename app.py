# encoding: utf-8
#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import os
import urllib
import flask
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from forms import *
import services

import logging
from logging import Formatter, FileHandler

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    return render_template('pages/placeholder.home.html')


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


@app.route('/questions')
def questions():
    form = QuestionsForm(request.form)

    # if request.method == "GET":
    #     return render_template('forms/questions.html', form=form)

    # form is being submitted, so do the analysis and redirect to results
    qs = urllib.urlencode({
        'user_name': "Fulano",
        'district_ids': "3,4,5"
    })
    return flask.redirect('/results?{}'.format(qs))


@app.route('/results')
def results():

    if len(request.args) > 0:
        user_name = request.args['user_name']
        district_ids = [int(did) for did in request.args['district_ids'].split(',')]
        district_names = services.fetch_district_names(district_ids)

    return render_template(
        'pages/map_results.html',
         user_name=user_name or None,
         selected_districts=district_names or None
    )


# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
