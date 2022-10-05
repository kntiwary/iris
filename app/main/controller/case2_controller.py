__author__ = 'kamta'

from flask_restx import Resource

from app.main.service.case2 import iris_stats, sepcies_maxlength
from app.main.util.dto import IrisDto

api = IrisDto.api


@api.route('/describe')
@api.response(404, 'Some went wrong.')
class DescribeIris(Resource):
    @api.doc('Iris detailed stats')
    def get(self):
        """Returns the basic statistics about the columns in data set, like min, max, count, mean etc."""
        resp = iris_stats()
        if not resp:
            api.abort(404)
        else:
            return resp


@api.route('group/sepal_length/<int:max>')
@api.param('max', 'Number')
@api.response(404, 'Some went wrong.')
class GenerateSequence(Resource):
    @api.doc('create sequence')
    def get(self, max):
        """Returns the number of each species with the maximum sepal_length of {max}."""

        resp = sepcies_maxlength(max)
        if not resp:
            api.abort(404)
        else:
            return resp
