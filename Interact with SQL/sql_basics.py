import sqlite3


# 1st step connect to DB
# 2nd step create a cursor object
# 3rd step Write an SQL query
# 4rd step Commit changes
# 5th step Close database connection

def create_table():
    conn = sqlite3.connect('lite.db')
    curs = conn.cursor()
    curs.execute("""CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)""")
    conn.commit()
    conn.close()


def insert_to_db(item, quantity, price):
    conn = sqlite3.connect('lite.db')
    curs = conn.cursor()
    curs.execute("""INSERT INTO store VALUES(?,?,?)""", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('lite.db')
    curs = conn.cursor()
    curs.execute("""SELECT * FROM store""")
    rows = curs.fetchall()
    conn.close()
    return rows


def delete_from_db(item):
    conn = sqlite3.connect('lite.db')
    curs = conn.cursor()
    curs.execute("""DELETE FROM store WHERE item=?""", (item,))
    conn.commit()
    conn.close()


def update_db(quantity, price, item):
    conn = sqlite3.connect('lite.db')
    curs = conn.cursor()
    curs.execute("""UPDATE store SET quantity=?, price=? WHERE item=?""", (quantity, price, item))
    conn.commit()
    conn.close()


print(view())
