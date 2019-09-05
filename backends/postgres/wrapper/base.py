from django.db.backends.postgresql_psycopg2.base import DatabaseWrapper as DaWr
from django.core.cache import caches
from django.conf import settings


class DatabaseWrapper(DaWr):
    """Custom database backend version for GSSAPI auth
    get user creds from Kerberos and get ticket"""
    def __init__(self, *args, **kwargs):
        super(DatabaseWrapper, self).__init__(*args, **kwargs)

    def get_connection_params(self):
        conn_params = super(DatabaseWrapper, self).get_connection_params()
        if settings.GSSAPI_ENABLED_OPTION:
            local = caches['local']
            principal = local.get(settings.GSSAPI_USER_PRINCIPAL_KEY)
            conn_params['user'] = principal
        return conn_params
