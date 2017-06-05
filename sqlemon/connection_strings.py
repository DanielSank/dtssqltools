"""
Invoke MySQL client, connecting either to local or cloud databases. These
commands connect to the server, but not a specific database.
"""
MYSQL_CLIENT_CLOUD = "mysql --user={} --password={} -S /tmp/cloudsql/{}"
# MySQL client through proxy to cloud
# Args: user, password, instance connection name

MYSQL_CLIENT_LOCAL = "mysql --user={} --password={} --host={} --port={}"
# MySQL client local
# Args: user, password, host, port

"""
SQLAlchemy connection URL's for local and cloud databases, connecting either
from test server or local tools. These all point to the the specific database
used by your project.
"""
APP_ENGINE_CLOUD = ("mysql+mysqldb://{}:{}@/{}"
                    "?unix_socket=/cloudsql/{}"
                    "?charset=utf8")
# App Engine to Cloud
# Args: user, password, database, instance connection name

LOCAL_TOOLS_CLOUD = ("mysql+pymysql://{}:{}@/{}"
                     "?unix_socket=/tmp/cloudsql/{}"
                     "?charset=utf8")
# e.g. Alembic to Cloud
# Args: user, password, database, instance connection name

LOCAL_TOOLS_LOCAL = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8"
# e.g. Alembic to local database
# Args: user, password, host, port, database
