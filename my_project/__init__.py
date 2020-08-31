# my_project/__init__.py

####################################
######### SETTING UP FLASK ####
####################################

from flask import Flask

application = Flask(__name__)
application.config['SECRET_KEY'] = 'mysecret'


####################################
######### SETTING UP BLUEPRINTS ####
####################################

from my_project.core.views import core

application.register_blueprint(core)