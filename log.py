import psycopg2

db = psycopg2.connect("dbname=news")
c = db.cursor()
query = "SELECT title FROM articles LIMIT 5;"
c.execute(query)
results = c.fetchall()
print(results)
db.close()
