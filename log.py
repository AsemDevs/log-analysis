import psycopg2


question1 = '1. What are the most popular three articles of all time?'

query1 = '''SELECT * FROM num_views LIMIT 3;'''

question2 = '2. Who are the most popular article authors of all time?'
query2 = '''SELECT name, SUM(views) AS total_views FROM authors_data WHERE author BETWEEN 1 AND 4 GROUP BY name, author ORDER BY author;'''

question3 = "3. On which days did more than 1% of requests lead to errors?"
query3 = '''SELECT date, percent FROM ratio WHERE percent > 1;'''
def QueryExecute(querys):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(querys)
    results = c.fetchall()
    db.close()
    print(results)


print(question1)
QueryExecute(query1)
print(question2)
QueryExecute(query2)
print(question3)
QueryExecute(query3)


