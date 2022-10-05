__author__ = 'kamta'

import os
import unittest

from app import blueprint
from app.main import create_app

app = create_app(os.getenv('APP_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()


def run():
    app.run()


def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    run()
