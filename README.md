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

CREATE VIEW author_views AS SELECT author, num_views.slug ,views FROM ((articles JOIN authors ON articles.author = authors.id) JOIN num_views ON  
articles.slug=num_views.slug)ORDER BY author;

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
