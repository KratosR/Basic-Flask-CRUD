from flask import Flask, render_template, request, redirect, url_for
import pymysql
import config

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=config.MYSQL_HOST,
        user=config.MYSQL_USER,
        password=config.MYSQL_PASSWORD,
        database=config.MYSQL_DB,
        port=config.MYSQL_PORT,
        cursorclass=pymysql.cursors.Cursor
    )

# READ
@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', users=users)

# CREATE
@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s)",
        (name, email)
    )
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for('index'))

# DELETE
@app.route('/delete/<int:id>')
def delete_user(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('index'))

# UPDATE (form)
@app.route('/edit/<int:id>')
def edit_user(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id=%s", (id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return render_template('edit.html', user=user)

# UPDATE (save)
@app.route('/update/<int:id>', methods=['POST'])
def update_user(id):
    name = request.form['name']
    email = request.form['email']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET name=%s, email=%s WHERE id=%s",
        (name, email, id)
    )
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()