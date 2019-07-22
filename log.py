import psycopg2

def QueryExecute(querys):
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(querys)
    results = c.fetchall()
    print(results)
    db.close()

query1 = '''SELECT path, COUNT(*) as views FROM log WHERE path IN ('/article/bad-things-gone',
    '/article/balloon-goons-doomed'
    ,'/article/bears-love-berries'
    ,'/article/candidate-is-jerk'
    ,'/article/goats-eat-googles'
    ,'/article/media-obsessed-with-bears'
    ,'/article/trouble-for-troubled'
    ,'/article/so-many-bears') GROUP BY path ORDER BY views DESC;'''

QueryExecute(query1)