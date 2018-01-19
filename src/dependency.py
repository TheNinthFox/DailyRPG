import yaml

from sqlalchemy import create_engine
from .database.models import Base

# Config
env_config = None
env = None

# Database
engine = None


def setup_dependency_container(environment=''):
    global env_config
    global env
    global engine

    with open('config/env.yaml', 'r') as environment_config:
        env_config = yaml.load(environment_config)

    if environment:
        env = env_config['env'][environment]
    else:
        env = env_config['env'][env_config['APP_ENV']]

    debug = True if env['name'] == 'Dev' else False

    engine = create_engine('sqlite:///{}'.format(env['database']), echo=debug)
