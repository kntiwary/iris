__author__ = 'kamta'


from flask_restx import Api
from flask import Blueprint

from .main.controller.case1_controller import api as seq
from .main.controller.case2_controller import api as iris

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTX API ',
          version='1.0',
          description='a restx web service'
          )
api.add_namespace(seq, path='/sequence')
api.add_namespace(iris, path='/iris')
