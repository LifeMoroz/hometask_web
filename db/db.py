import sqlite3
import MySQLdb

# from django.conf import settings
#
#
# class Database:
#     db = None
#
#     def __init__(self):
#         self._conn = sqlite3.connect(settings.DATABASES['default']['NAME'])
#         self._cursor = self._conn.cursor()
#
#     @staticmethod
#     def get_database():
#         return Database()
#
#     @staticmethod
#     def execute(sql, params=None, unescape=None):
#         self = Database.get_database()
#         sql = sql.format(unescape) if unescape else sql
#         try:
#             if params:
#                 return self._cursor.execute(sql, params)
#             else:
#                 return self._cursor.execute(sql)
#         finally:
#             self._conn.commit()


class Database:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def get_connection(self):
        pass


class RelationalDB(Database):
    def execute(self, sql, params, unescaped=None):
        pass


class MysqlDatabase(RelationalDB):
    def get_connection(self):
        return MySQLdb.connect(*self.args, **self.kwargs)

    def execute(self, sql, params, unescaped=None):
        conn = self.get_connection()
        return conn.execute(sql, params)


class SqlLite3(RelationalDB):

    def get_connection(self):
        return sqlite3.connect(*self.args, **self.kwargs)

    def execute(self, sql, params, unescaped=None):
        conn = self.get_connection()
        sql = sql.format(unescaped) if unescaped else sql
        try:
            if params:
                return conn.cursor().execute(sql, params)
            else:
                return conn.cursor().execute(sql)
        finally:
            conn.commit()


class DatabaseFactory:
    def get_db(self) -> Database:
        pass


class MysqlFactory(DatabaseFactory):
    def get_db(self, *args, **kwargs) -> MysqlDatabase:
        return MysqlDatabase(*args, **kwargs)


class SqlLiteFactory(DatabaseFactory):
    def get_db(self, *args, **kwargs) -> SqlLite3:
        return SqlLite3(*args, **kwargs)
