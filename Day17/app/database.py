import sqlite3
def get_db_connection():
    conn=sqlite3.connect('database.py')
    conn.row_factory=sqlite3.Row
    return conn
def init_db():
    conn=get_db_connection()
    conn.execute('''
    Create table if not exists items(
    id integer primary key autoincrement,
    name text not null,
    description text
    ''')
    conn.commit()
    conn.close()
