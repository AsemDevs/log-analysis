import itertools
from numbers import Number

import psycopg2

question1 = '1. What are the most popular three articles of all time?'

query1 = '''SELECT * FROM num_views LIMIT 3;'''

question2 = '2. Who are the most popular article authors of all time?'
query2 = '''SELECT name, SUM(views) FROM authors_data
 GROUP BY name, author ORDER BY author;'''

question3 = "3. On which days did more than 1% of requests lead to errors?"
query3 = '''SELECT date, CAST(percent AS numeric)
 FROM ratio WHERE percent > 1;'''


# Connect to database and execute queries
def results(queries):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(queries)
    results = c.fetchall()
    db.close()
    return results


# Get the results of each query
r1 = results(query1)
r2 = results(query2)
r3 = results(query3)


# Output function To unpack the list of the tuples
# and get only plain text for the first two queries
def report_results(q):
    out = list(itertools.chain(*q))
    for i in range(len(out)):
        if i % 2 == 0:
            slug = out[i]
        else:
            num = out[i]
            print("\n" + "\t" + "%s - %d" % (slug, num) + " views")
            print("\n")


# Output function To unpack the list of the tuples
# and get only plain text for the third query and specific edits
def report_results_q3(q):
    out = list(itertools.chain(*q))
    for i in range(len(out)):
        if i % 2 == 0:
            slug = out[i]
        else:
            num = out[i]
            x = format(num/100, '%')
            print("\n" + "\t" + slug + " - " + x + " errors")


# printing the questions and calling output functions
print(question1)
report_results(r1)
print(question2)
report_results(r2)
print(question3)
report_results_q3(r3)
