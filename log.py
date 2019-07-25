import psycopg2


question1 = '1. What are the most popular three articles of all time?'

query1 = '''SELECT * FROM num_views LIMIT 3;'''

question2 = '2. Who are the most popular article authors of all time?'
query2 = '''SELECT name, SUM(views) FROM authors_data GROUP BY name, author ORDER BY author;'''

question3 = "3. On which days did more than 1% of requests lead to errors?"
query3 = '''SELECT date, percent FROM ratio WHERE percent > 1;'''
def QueryExecute(querys):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(querys)
    results = c.fetchall()
    db.close()
    print(results)


def results(querys):
    if querys == query3:
        print(question3)
    elif querys == query2:
        print(question2)
    else:
        print(question1)
    QueryExecute(querys)

results(query1)
results(query2)
results(query3)

