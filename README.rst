*******
SQLemon
*******

Suppose we're working on a project that uses Google App Engine, Google Cloud SQL, and sqlalchemy.
In the course of testing, deploying etc., we want to connect to a couple of databases in different ways:

* App Engine project talking to production db

* Local tools (like mysql client or alembic) talking to production db

* Local tools (like mysql client or alembic) talking to local db


Getting all the connections strings etc. right is kind annoying.
This package helps solve that problem.

Scripts
*******

Installing `SQLemon` puts two scripts into your virtualenv's `bin/` directory:

* ``start_cloud_proxy``: Run the Google Cloud SQL proxy using an authentication token you downloaded when making a service account. See below for details about where that authentication token should be stored.

*  ``start_mysql_client``: Run MySQL client on your machine, connecting either to the production server (through the proxy) or to a local test database.

Files
*****

We assume you have your project's source on your system at ``PROJECT_ROOT/``, where
``PROJECT_ROOT`` is probably something like ``~/src/<whatever>/``.
The file layout should look something like this:

.. code-block::

    ├── PROJECT_ROOT/
    │    ├── SQLEMON_PROJECT_NAME/  <-- important
    │    │   ├── __init__.py
    │    │   ├── alembic.ini
    │    │   ├── alembic/
    │    │   ├── lib/
    │    │   ├── models.py
    │    │   └── main.py
    │    ├── README.md
    │    ├── appengine_config.py
    |    ├── secrets.py             <-- important, GITIGNORE THIS FILE!
    │    └── app.yaml               <-- important

You must also have a directory at ``~/.SQL_PROJECT_NAME`` with a couple of files described below.
Here are the required layouts of the required files:

- ``~/.SQL_PROJECT_NAME/config.yaml``
  ::

    ---
    cloud:
        PASSWORD: <Cloud SQL user password>
    local:
        USER: <Local database user name, e.g. "root">
        PASSWORD: <Local database root password, e.g. "">
        HOST: "localhost"
        PORT: 3306

- ``~/.SQL_PROJECT_NAME/auth-token.json``: This is your proxy's user account auth token.

- ``PROJECT_ROOT/app.yaml``
  ::

      env_variables:
        INSTANCE_CONNECTION_NAME: ...
        CLOUD_SQL_USER: <Cloud SQL user name>

- ``PROJECT_ROOT/secrets.py``
  ::

      CLOUD_SQL_PASSWORD = <Cloud SQL user password>

How to release
**************
::

    $ python setup.py register -r pypi(test)
    $ python setup.py sdist upload -r pypi(test)

