import os


from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

import click
from  flask_migrate import Migrate
from app import create_app, db
from app.models.user import User
from app.models.order import Order
from app.models.restaurant import Restaurant

app = create_app(os.getenv("FLASK_CONFIG") or "default")
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Order=Order, Restaurant=Restaurant)




@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run unit test """
    import unittest

    if test_names:
        """
        flask test tests.test_dataset_model
        """
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests',pattern='test*.py')

    result =  unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1
