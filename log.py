import psycopg2


question1 = '1. What are the most popular three articles of all time?'

query1 = '''SELECT SUBSTRING(path,10) AS slug,
 COUNT(*) as views FROM log
 WHERE path LIKE '%-%'
 GROUP BY path ORDER BY views DESC LIMIT 3;'''

question2 = '2. Who are the most popular article authors of all time?'
query2 = '''SELECT name, SUM(views) AS total_views FROM authors_data WHERE author BETWEEN 1 AND 4 GROUP BY name, author ORDER BY author;'''

def QueryExecute(querys):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(querys)
    results = c.fetchall()
    db.close()
    print(results)


print(question2)
QueryExecute(query2)

