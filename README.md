# VIEWS LIST

## 1-num_views
<!--Number of views for each of the eight articles-->

    CREATE VIEW num_views as SELECT SUBSTRING(path,10) AS slug, COUNT(*) as views FROM log WHERE path LIKE '%-%' GROUP BY path ORDER BY views DESC LIMIT 8;

    news=> SELECT * FROM num_views;

            slug            | views
    ---------------------------+--------
    candidate-is-jerk         | 338647
    bears-love-berries        | 253801
    bad-things-gone           | 170098
    goats-eat-googles         |  84906
    trouble-for-troubled      |  84810
    balloon-goons-doomed      |  84557
    so-many-bears             |  84504
    media-obsessed-with-bears |  84383

## 2-article_views
<!--Number of views for each article and its author -->

    CREATE VIEW article_views AS SELECT author, num_views.slug ,views FROM ((articles JOIN authors ON articles.author = authors.id) JOIN num_views ON articles.slug=num_views.slug)ORDER BY author;

    news=> SELECT * FROM article_views;

    author |           slug            | views
    --------+---------------------------+--------
        1 | so-many-bears             |  84504
        1 | bears-love-berries        | 253801
        1 | goats-eat-googles         |  84906
        1 | media-obsessed-with-bears |  84383
        2 | trouble-for-troubled      |  84810
        2 | candidate-is-jerk         | 338647
        3 | bad-things-gone           | 170098
        4 | balloon-goons-doomed      |  84557

## 3-authors_data
<!-- Name of each author with his articles and its number of views -->

     CREATE VIEW authors_data AS SELECT name, author, article_views.slug, CAST(views AS INT) FROM article_views JOIN authors ON authors.id=article_views.author;

    news=> SELECT * FROM authors_data;

            name           | author |           slug            | views
    ------------------------+--------+---------------------------+--------
    Ursula La Multa        |      1 | media-obsessed-with-bears |  84383
    Ursula La Multa        |      1 | goats-eat-googles         |  84906
    Ursula La Multa        |      1 | bears-love-berries        | 253801
    Ursula La Multa        |      1 | so-many-bears             |  84504
    Rudolf von Treppenwitz |      2 | candidate-is-jerk         | 338647
    Rudolf von Treppenwitz |      2 | trouble-for-troubled      |  84810
    Anonymous Contributor  |      3 | bad-things-gone           | 170098
    Markoff Chaney         |      4 | balloon-goons-doomed      |  84557

## 4- errors
<!-- Total number of errors for each day -->

    CREATE VIEW errors AS SELECT date(time) AS date,COUNT(*) AS errs FROM log WHERE status = '404 NOT FOUND' GROUP BY date ORDER BY date;

    news=> SELECT * FROM errors ORDER BY errs DESC LIMIT 5;
      date     | errs
    ------------+------
    2016-07-17 | 1265
    2016-07-19 |  433
    2016-07-24 |  431
    2016-07-05 |  423
    2016-07-06 |  420

## 5-reqs
<!-- Total of requests for each day -->

    CREATE VIEW reqs AS SELECT date(time), COUNT(*) AS requists* FROM log GROUP BY date(time) ORDER BY date(time);

    news=> SELECT * FROM reqs ORDER BY requists DESC LIMIT 5;
      date     | requists
    ------------+----------
    2016-07-17 |    55907
    2016-07-18 |    55589
    2016-07-19 |    55341
    2016-07-21 |    55241
    2016-07-09 |    55236

## 6-ratio
<!-- The ratio of errors in each day -->

    '''sql
    CREATE VIEW ratio AS SELECT CAST(reqs.date AS text) ,CAST(ROUND((100.0*errors.errs / reqs.requists), 3) AS float(4)) as percent FROM reqs,errors WHERE reqs.date=errors.date ORDER BY reqs.date;'''

    news=> SELECT * FROM ratio ORDER BY percent DESC LIMIT 5;
        date   | percent
    ------------+---------
    2016-07-17 |   2.263
    2016-07-24 |   0.782
    2016-07-19 |   0.782
    2016-07-05 |   0.775
    2016-07-06 |   0.767
