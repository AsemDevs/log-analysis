import itertools
from numbers import Number

import psycopg2

question1 = '1. What are the most popular three articles of all time?'

query1 = '''SELECT * FROM num_views LIMIT 3;'''

question2 = '2. Who are the most popular article authors of all time?'
query2 = '''SELECT name, SUM(views) FROM authors_data GROUP BY name, author ORDER BY author;'''

question3 = "3. On which days did more than 1% of requests lead to errors?"
query3 = '''SELECT date, CAST(percent AS numeric) FROM ratio WHERE percent > 1;'''
def results(querys):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(querys)
    results = c.fetchall()
    db.close()
    return results

r1=results(query1)
r2=results(query2)
r3=results(query3)

def report_results(q):
    # out = list(zip(*q))
    out = list(itertools.chain(*q))
    for i in range(len(out)):
        if i % 2 == 0:
            slug = out[i]
        else:
            num = out[i]
            print("\t" + "%s - %d" % (slug, num) + " views")
            print("\n")

def report_results_q3(q):
    out = list(itertools.chain(*q))
    for i in range(len(out)):
        if i % 2 == 0:
            slug = out[i]
        else:
            num = out[i]
            x = format(num/100,'%')
            print("\t" + slug +" - "+ x + " errors")


print(question1)
report_results(r1)
print(question2)
report_results(r2)
print(question3)
report_results_q3(r3)
