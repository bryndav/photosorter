import logging
import os
import sqlite3

logger = logging.getLogger("sorter")


class Singleton(type):
    """Meta class to ensure that the database class remains a singleton."""
    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        else:
            raise TypeError("Instance is already created at: {}".format(cls._instances.popitem()))


class PhotoDatabase(object):
    """
    Database for indexing photos and information related to that photo.
    """
    __metaclass__ = Singleton

    def __init__(self, root_folder):
        self.root = root_folder
        self.db_name = os.path.join(root_folder, "photo_database.db")
        self.check_db_status()

    def get_connection(self):
        """Returns a connection object to the database, if none exists creates one."""
        return sqlite3.connect(self.db_name)

    def check_db_status(self):
        db_exists = os.path.isfile(self.db_name)

        if not db_exists:
            self._create_table()

    def _create_table(self, conn):
        """Creates a table for new databases."""
        conn = self.get_connection()
        c = conn.cursor()

        c.execute(
            '''CREATE TABLE photos 
                    (ID int, Location text, DateTime text, Name text, PRIMARY KEY (ID))'''
        )

        conn.commit()
        conn.close()

