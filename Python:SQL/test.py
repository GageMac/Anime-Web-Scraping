import sqlite3

con = sqlite3.connect('anime.db')
cur = con.cursor()
cur.execute("DROP TABLE anime")
cur.execute("CREATE TABLE anime(title, rank, rating)")

res = cur.execute("SELECT name FROM sqlite_master")
res.fetchone()
cur.execute("DROP TABLE anime")