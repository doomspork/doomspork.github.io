#!/usr/bin/env python

import os

from app import app, assets
from flask.ext.script import Manager, Server
from flask.ext.assets import ManageAssets
from flask.ext.script.commands import ShowUrls, Clean

# default to dev config because no one should use this in
# production anyway
env = os.environ.get('APP_ENV', 'dev')


manager = Manager(app)
assets.environment = app.jinja_env.assets_environment
manager.add_command('assets', ManageAssets(assets))
manager.add_command('server', Server())
manager.add_command('show-urls', ShowUrls())
manager.add_command('clean', Clean())


if __name__ == '__main__':
    manager.run()
