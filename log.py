import psycopg2

db = psycopg2.connect("dbname=news")
c = db.cursor()
c.execute("")
