
from contextlib import contextmanager
from mysql.connector.pooling import MySQLConnectionPool
from mysql.connector.cursor import MySQLCursor
from typing import Generator
from prettytable import PrettyTable

 
class DB:
    
    pool: MySQLConnectionPool = None
    
    @classmethod
    def getPool(cls) -> MySQLConnectionPool:
        
        if not cls.pool:
            cls.pool = MySQLConnectionPool(
                pool_size = 3,
                pool_reset_session = True,
                host = "localhost",
                user = "root",
                password = "",
                database = "journal",
                auth_plugin = "mysql_native_password",
            )
            
        return cls.pool
            
    @classmethod
    @contextmanager
    def cursor(cls, isDict=False, isAutoCommit=True) -> Generator[MySQLCursor, None, None]:
        '''Use like this: with DB_KC.cursor() as crs: ...'''
        con = cls.getPool().get_connection()
        con.autocommit = isAutoCommit
        try:
            yield con.cursor(dictionary=isDict)
        finally:
            con.commit()
            con.close()
            
    @classmethod
    def execute(cls, sql, params=None) -> int:
        '''execute and return last inserted id'''
        with cls.cursor() as crs:
            crs.execute(sql, params)
            return crs.lastrowid
    
    @classmethod
    def select(cls, sql, params=(), isDict = False) -> list:
        with cls.cursor(isDict=isDict) as crs:
            crs.execute(sql, params)
            return crs.fetchall()
    
    @classmethod
    def printRows(cls, rows):
        if not rows:
            print('No records found')
            return
        table = PrettyTable()
        table.field_names = rows[0].keys()
        for row in rows:
            table.add_row(row.values())
        print(table)
       
    