import sqlite3

DB_PATH = "students.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT NOT NULL,
                          num TEXT NOT NULL)''')
        conn.commit()

def save(name, num):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, num) VALUES (?, ?)", (name, num))
        conn.commit()

def get_all_students():

     with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        return cursor.fetchall()

def delete_student(student_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()

