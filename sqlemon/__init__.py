import os

import sqlemon.connection_strings as sqlcs
import yaml

__version__ = "0.6.0"
__project_name__ = "sqlemon"


class IPythonPrettyPrintable(object):
    """Mixin for sqlalchemy models to make IPython printing nice."""
    def _repr_pretty_(self, p, cycle):
        p.text(str(self) if not cycle else "...")


def get_sql_configuration(project_name, db_config):
    config_file_name = os.path.join(
            os.path.expanduser('~'),
            '.{}/config.yaml'.format(project_name))
    with open(config_file_name, 'r') as stream:
        parameters = yaml.load(stream)[db_config]
    return parameters


def get_app_configuration():
    with open('./app.yaml', 'r') as stream:
        config = yaml.load(stream)
    return config


def get_auth_token_filepath(project):
    return os.path.expanduser('~/.{}/auth-token.json'.format(project))


def production_mode():
    """Return True if running in production mode."""
    mode = os.getenv('SERVER_SOFTWARE')
    if mode is not None and mode.startswith('Google App Engine/'):
        return True
    else:
        return False


def get_sqlalchemy_url_for_client(project, db_config=None):
    """Get sqlalchemy connection string for client scripts, i.e. alembic.

    Args:
        project (str):
        db_config (str): 'local' or 'cloud'.
    """
    if production_mode():
        raise RuntimeError('Should not get here in production')
    if db_config is None:
        db_config = os.environ['SQLEMON_DB_CONFIG']
    config = get_sql_configuration(project, db_config)
    app_config = get_app_configuration()
    if db_config == 'cloud':
        return sqlcs.LOCAL_TOOLS_CLOUD.format(
                app_config['env_variables']['CLOUD_SQL_USER'],
                config['PASSWORD'],
                project,
                app_config['env_variables']['INSTANCE_CONNECTION_NAME'])
    elif db_config == 'local':
        return sqlcs.LOCAL_TOOLS_LOCAL.format(
                config['USER'],
                config['PASSWORD'],
                config['HOST'],
                config['PORT'],
                project)
    else:
        raise ValueError("db_config {} not known".format(db_config))


def get_sqlalchemy_url_for_server(project, password=None):
    """Get the sqlalchemy connection URL for the server.

    If we detect that we're running in the Cloud on App Engine, then we get
    the required connection iformation from environment variables which should
    be specified in app.yaml. Those variables are:
        CLOUD_SQL_USER
        INSTANCE_CONNECTION_NAME

    If we detect that we're not in the Cloud, then we assume we're running in a
    local dev server. In that case, we assume the developer has a MySQL server
    running locally and that they've put the appropriate connection information
    in their home directory. See get_sql_configuration.
    """
    if production_mode():
        return sqlcs.APP_ENGINE_CLOUD.format(
                os.environ['CLOUD_SQL_USER'],
                password,
                project,
                os.environ['INSTANCE_CONNECTION_NAME'])
    else:
        return r'mysql+pymysql://root@localhost/{}'.format(project)
        """
        It would be better to parametrize the the username etc. but I'm not sure
        how to get the dev server to read from the local file system. We don't
        want to store local MySQL connection info in app.yaml so I'm not sure
        how to procede. One option would be to make a .gitignore'd file with the
        local connection info.
        """
