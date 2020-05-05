from flask_script import Manager

from template_api import settings
from template_api.ws import app

manager = Manager(app)


@manager.command
def run():
    app.run(host=settings.HOST, port=settings.PORT, debug=settings.DEBUG)
    

@manager.command
def test():
    """Runs the unit tests."""
    raise NotImplementedError()


if __name__ == '__main__':
    manager.run()
