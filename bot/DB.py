import sqlite3
from sqlite3 import Error


def create_connection():
    """Create a database connection or create the database if it doesn't exist"""
    conn = None
    try:
        conn = sqlite3.connect('ansvers.db')
        create_table(conn)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn):
    """Create key-value table if it doesn't exist"""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS ansvers (
        word TEXT,
        translation TEXT
    );
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


def wrightAnsver(key, value):
    """Insert or replace a key-value pair"""
    conn = create_connection()
    if conn is not None:
        try:
            sql = ''' INSERT OR REPLACE INTO ansvers(word, translation)
                      VALUES(?,?) '''
            cur = conn.cursor()
            cur.execute(sql, (key, value))
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()


def readAnsver(key):
    """Read value by key"""
    conn = create_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT translation FROM ansvers WHERE word=?", (key,))
            result = cur.fetchone()
            return result[0] if result else "NoAnswer"
        except Error as e:
            print(e)
        finally:
            conn.close()
    return None