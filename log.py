#!/usr/bin/env python3

import itertools
import psycopg2

question1 = '1. What are the most popular three articles of all time?'

query1 = '''SELECT * FROM num_views LIMIT 3;'''

question2 = '2. Who are the most popular article authors of all time?'
query2 = '''SELECT name, SUM(views) AS views FROM authors_data
 GROUP BY name ORDER BY views DESC;'''

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


# Get only plain text from the queries results
def report_results(q):
    tab = "\t"
    if q == r1 or q == r2:
        for row in q:
            print("\n")
            out = '{title} - {count} views'.format(title=row[0], count=row[1])
            print(tab + out)
        print("\n")
    else:
        for row in q:
            print("\n")
            out3 = '{date} - {count}% errors'.format(date=row[0], count=row[1])
            print(tab + out3)
        print("\n")


# printing the questions and calling output functions
if __name__ == '__main__':
    print(question1)
    report_results(r1)
    print(question2)
    report_results(r2)
    print(question3)
    report_results(r3)
