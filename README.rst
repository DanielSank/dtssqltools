*******
SQLemon
*******

Suppose we're working on a project that uses Google App Engine, Google Cloud SQL, and sqlalchemy.
In the course of testing, deploying etc., we want to connect to a couple of databases in different ways:

* App Engine project talking to production db

* Local tools (like mysql client or alembic) talking to production db

* Tests talking to local db

* Local tools talking to local db

Getting all the connections strings etc. right is kind annoying.
This package helps solve that problem.

We provide two scripts:

* ``start_cloud_proxy``: Runs the Google Cloud SQL proxy using an authentication token you downloaded when making a service account.

*  ``start_mysql_client``: Runs a client on your machine, connecting either to the production server (through the proxy) or to a local test database.

Whether you're connecting to a cloud instance or a local server, both of these scripts decide which database to connect to by reading the evironment variable ``SQL_PROJECT_NAME``.
This variable must match the name of the database to which you're trying to connect.

We assume you have your project's source on your system at ``PROJECT_ROOT/``, where
``PROJECT_ROOT`` is probably something like ``~/src/<whatever>/``.
The file layout should look something like this:

.. code-block::

    ├── PROJECT_ROOT/
    │    ├── SQL_PROJECT_NAME/  <-- important
    │    │   ├── __init__.py
    │    │   ├── config.yaml    <-- Important
    │    │   ├── alembic.ini
    │    │   ├── alembic/
    │    │   ├── lib/
    │    │   ├── models.py
    │    │   └── main.py
    │    ├── README.md
    │    ├── appengine_config.py
    │    └── app.yaml

You must also have a directory at ``~/.SQL_PROJECT_NAME`` with a couple of files described in the paragraph.

This package assumes there are three particular files to be available in your system:

- ``~/.SQL_PROJECT_NAME/config.yaml``
  ::

    ---
    cloud:
        USER: "root"
        PASSWORD: ...
    local:
        USER: "root"
        PASSWORD: ...
        HOST: "localhost"
        PORT: 3306

- ``~/.SQL_PROJECT_NAME/auth-token.json``: This is your proxy's user account auth token.

- ``PROJECT_ROOT/SQL_PROJECT_NAME/config.yaml``
  ::

      ---
      INSTANCE_CONNECTION_NAME: ...

Installing this package (into a virtualenv!) provides the command line script ``start_cloud_proxy``, which starts the Google Cloud SQL proxy for you.

How to release
**************
::

    $ python setup.py register -r pypi(test)
    $ python setup.py sdist upload -r pypi(test)

