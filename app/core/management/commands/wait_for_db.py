"""
Django command to wait for the database to be available.
"""
import time

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for the databse"""

    def handle(self, *args, **options):
        """Entry point of the command"""
        self.stdout.write("Waiting for database...")
        db_up = False
        while not db_up:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("Database unavailable, wating 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
