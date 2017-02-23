from django.conf import settings
from django import VERSION as DJANGO_VERSION
try:
    from django.db.models.signals import post_migrate, post_syncdb
except ImportError:
    from django.db.models.signals import post_migrate

from .postgres_migration import PostgresBackend
from .mssql_migration import MSSQLBackend


DATABASE_ENGINE = settings.DATABASES['default']['ENGINE']


def do_updates(m):
    if DATABASE_ENGINE == 'scarlet.versioning.postgres_backend':
        klass = PostgresBackend()
    elif DATABASE_ENGINE == 'scarlet.versioning.mssql_backend':
        klass = MSSQLBackend()
    return klass.do_updates(m)


def update_schema(sender=None, **kwargs):
    if sender:
        for m in sender.get_models():
            if getattr(m._meta, '_view_model', None):
                do_updates(m._meta._view_model)


def update_syncdb_schema(app, created_models, verbosity, **kwargs):
    for m in created_models:
        do_updates(m)

if DJANGO_VERSION < (1, 7):
    post_syncdb.connect(update_syncdb_schema, dispatch_uid='update_syncdb_schema')
else:
    post_migrate.connect(update_schema, dispatch_uid='update_schema')
