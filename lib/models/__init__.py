import sqlite3

CONN = sqlite3.connect("data/quiz_sphere_database.db")
CURSOR = CONN.cursor()
