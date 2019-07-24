# MY VIEWS

    1-num_views <!--num-views = number of views for each of the eight articles-->

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

    2-author_views

    CREATE VIEW author_views AS SELECT author, num_views.slug ,views FROM ((articles JOIN authors ON articles.author = authors.id) JOIN num_views ON articles.slug=num_views.slug)ORDER BY author;

    news=> SELECT * FROM author_views;

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

    3-authors_data

    CREATE VIEW authors_data AS SELECT name, author, author_views.slug, views FROM author_views JOIN authors ON authors.id=author_views.author;

    news=> SELECT * FROM authors_data;

            name          | author |           slug            | views
    ------------------------+--------+---------------------------+--------
    Ursula La Multa        |      1 | media-obsessed-with-bears |  84383
    Ursula La Multa        |      1 | goats-eat-googles         |  84906
    Ursula La Multa        |      1 | bears-love-berries        | 253801
    Ursula La Multa        |      1 | so-many-bears             |  84504
    Rudolf von Treppenwitz |      2 | candidate-is-jerk         | 338647
    Rudolf von Treppenwitz |      2 | trouble-for-troubled      |  84810
    Anonymous Contributor  |      3 | bad-things-gone           | 170098
    Markoff Chaney         |      4 | balloon-goons-doomed      |  84557


    4- errors
    CREATE VIEW errors AS SELECT date(time) AS date,COUNT(*) AS errs FROM log WHERE status = '404 NOT FOUND' GROUP BY date ORDER BY date;

    news=> SELECT * FROM errors;
        date   |  errs
    ------------+------
    2016-07-01 |  274
    2016-07-02 |  389
    2016-07-03 |  401
    2016-07-04 |  380
    2016-07-05 |  423
    2016-07-06 |  420
    2016-07-07 |  360
    2016-07-08 |  418
    2016-07-09 |  410
    2016-07-10 |  371
    2016-07-11 |  403
    2016-07-12 |  373
    2016-07-13 |  383
    2016-07-14 |  383
    2016-07-15 |  408
    2016-07-16 |  374
    2016-07-17 | 1265
    2016-07-18 |  374
    2016-07-19 |  433
    2016-07-20 |  383
    2016-07-21 |  418
    2016-07-22 |  406
    2016-07-23 |  373
    2016-07-24 |  431
    2016-07-25 |  391
    2016-07-26 |  396
    2016-07-27 |  367
    2016-07-28 |  393
    2016-07-29 |  382
    2016-07-30 |  397
    2016-07-31 |  329


    5-reqs
    CREATE VIEW reqs AS SELECT date(time), COUNT('num OF reqs') AS requists FROM log GROUP BY date(time) ORDER BY date(time);

    news=> SELECT * FROM reqs;
       date    | requists
    ------------+----------
    2016-07-01 |    38705
    2016-07-02 |    55200
    2016-07-03 |    54866
    2016-07-04 |    54903
    2016-07-05 |    54585
    2016-07-06 |    54774
    2016-07-07 |    54740
    2016-07-08 |    55084
    2016-07-09 |    55236
    2016-07-10 |    54489
    2016-07-11 |    54497
    2016-07-12 |    54839
    2016-07-13 |    55180
    2016-07-14 |    55196
    2016-07-15 |    54962
    2016-07-16 |    54498
    2016-07-17 |    55907
    2016-07-18 |    55589
    2016-07-19 |    55341
    2016-07-20 |    54557
    2016-07-21 |    55241
    2016-07-22 |    55206
    2016-07-23 |    54894
    2016-07-24 |    55100
    2016-07-25 |    54613
    2016-07-26 |    54378
    2016-07-27 |    54489
    2016-07-28 |    54797
    2016-07-29 |    54951
    2016-07-30 |    55073
    2016-07-31 |    45845


    '''CREATE VIEW ratio AS SELECT reqs.date ,(100.0*errors.errs / reqs.requists) as percent FROM reqs, errors WHERE reqs.date=errors.date ORDER BY reqs.date;''' 

