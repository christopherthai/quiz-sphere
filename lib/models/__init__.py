import sqlite3

CONN = sqlite3.connect('data/quiz_sphere.db')
CURSOR = CONN.cursor()
