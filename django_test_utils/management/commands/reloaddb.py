from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = ("Drop and recreate the entire database from scratch. This is a " +
            "more comprehensive alternative to the `flush` command. Currently " +
            "supports mysql (without options file) and sqlite databases.")
    
    def handle(self, *args, **options):
        try:
            for db in settings.DATABASES:
                engine = db['ENGINE']
                self.handle_db(engine, db)
        except KeyError:
            print "The database is incorrectly configured or uses an options file."
    
    def handle_db(self, engine, db):
        if engine == 'django.db.backends.sqlite3' or engine == 'sqlite3':
            self._handle_sqlite(db)
        elif engine == 'django.db.backends.mysql':
            self._handle_mysql(db)
        else:
            print "Only sqlite and mysql (without an options file) is currently supported."
    
    def _handle_sqlite(self, db):
        pass
    
    def _handle_mysql(self, db):
        pass