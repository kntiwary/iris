__author__ = 'kamta'

from flask_restx import Resource

from app.main.service.case1 import create_seq, find_longest
from app.main.util.dto import SequenceDto


api = SequenceDto.api


@api.route('/elem/<int:n>')
@api.param('n', 'Number')
@api.response(404, 'Some went wrong.')
class GenerateSequence(Resource):
    @api.doc('create sequence')
    def get(self, n):
        """number n"""
        seq = create_seq(n)
        if not seq:
            api.abort(404)
        else:
            return seq


@api.route('/longest/<int:n>')
@api.param('n', 'Number')
@api.response(404, 'Some went wrong.')
class GenerateSequence(Resource):
    @api.doc('create sequence')
    def get(self, n):
        """Returns the value smaller than n, that has the longest chain."""
        max_len, val = find_longest(n)
        if not (max_len and val):
            api.abort(404)
        else:
            resp_longest = {'response': val,
                            'maxlength': max_len
                            }
            return resp_longest
