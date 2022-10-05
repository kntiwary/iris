__author__ = 'kamta'

from flask_restx import Namespace


class SequenceDto:
    api = Namespace('Sequence', description='Sequence related operations')


class IrisDto:
    api = Namespace('Iris', description='Iris related operations')
