import yaml

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Config
env_config = None
env = None

# Database
Base = None
engine = None


def setup(environment=''):
    global env_config
    global env
    global Base
    global engine

    with open('config/env.yaml', 'r') as environment_config:
        env_config = yaml.load(environment_config)

    if environment:
        env = env_config['env'][environment]
    else:
        env = env_config['env'][env_config['APP_ENV']]

    Base = declarative_base()
    engine = create_engine('sqlite:///{}'.format(env['database']), echo=True)
