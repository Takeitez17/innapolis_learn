from flask import Flask, render_template
import sqlite3 as sq

app = Flask(__name__)


@app.route('/')
@app.route('/index')

def index():
    with sq.connect('test.db') as con:
        cur = con.cursor()
        cur.execute("""SELECT * FROM equipment""")
        data = cur.fetchall()
    return render_template('test.html', data=data)


if __name__ == '__main__':
    app.run()