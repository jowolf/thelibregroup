
DEBUG = True

TEST_RUNNER = 'django.test.simple.DjangoTestSuiteRunner'

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

# # # # # JJW

ADMINS = (
    ('Joe Admin', 'joe@thelibregroup.com'),
)
MANAGERS = ADMINS

SITE_ID = 2

#ALLOWED_HOSTS = ['127.0.0.1']

FABRIC = {
    "HOSTS": ["thelibregroup.com"], # List of hosts to deploy to
    #"REQUIREMENTS_PATH": "requirements.txt",
    #"REPO_URL": "git://github.com/stephenmcd/mezzanine.jupo.org.git",
    #SSH_USER: def getuser
    'PROJECT_NAME': 'thelibregroup',  # proj_name, def last dir!
    # gunicorn_port - def 8000
    # live_host def hosts [0]
    # proj_path - derived fm above
}
