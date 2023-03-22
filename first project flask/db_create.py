import sqlite3 as sq

con = sq.connect('test.db')
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS equipment(
   id INT PRIMARY KEY,
   name TEXT,
   quantity INTEGER,
   price INTEGER);
""")

sql = 'INSERT INTO equipment (name, quantity, price) values(?, ?, ?)'

data = [
    ('стол', 2, 3000),
    ('стул', 5, 1000),
    ('табурет', 1, 500)
]

with con:
    con.executemany(sql, data)

con.commit()