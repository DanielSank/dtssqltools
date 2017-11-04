from distutils.core import setup

version = "0.8.0"
project_name = 'sqlemon'

setup(name=project_name,
      packages=[project_name],
      scripts=['bin/start_cloud_proxy',
               'bin/cloud_sql_proxy',
               'bin/start_mysql_client'],
      version=version,
      description="Manage sqlalchemy connections to Google Cloud SQL",
      author='Daniel Sank',
      license='MIT',
      author_email='sank.daniel@gmail.com',
      url='https://github.com/DanielSank/{}'.format(project_name),
      download_url='https://github.com/DanielSank/{}/tarball/{}'.format(
          project_name,
          version),
      keywords=['sql'],
      classifiers=[],
      install_requires=[
          'sqlalchemy',
          'alembic',
          'pyyaml',
          'sqlalchemy-schemadisplay'
          ],
)
