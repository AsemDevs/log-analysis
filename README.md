# Project: Logs Analysis - news website

## Project Overview

- - - -
The task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

## the questions the report answers

- - - -
*1. What are the most popular three articles of all time?*
*2. Who are the most popular article authors of all time?*
*3. On which days did more than 1% of requests lead to errors?*

## Requirements

- - - -
To start on this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze which is included below.
[Python 3](https://www.python.org/download/releases/3.0/) - The code uses ver 3.6.4\
[Vagrant](https://www.vagrantup.com/) - A virtual environment builder and manager\
[VirtualBox](https://www.virtualbox.org/) - An open source virtualiztion product.\
[Git](https://git-scm.com/) - An open source version control system

## How to run this project'?'

- - - -
Follow the steps below to access the code of this project:

 1. If you don't already have the latest version of python download it from the link in requirements.
 2. Download and install Vagrant and VirtualBox.
 3. Download this Udacity [folder](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip) with preconfigured vagrant settings.
 4. Clone this repository.
 5. Download [this](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) database.
 6. Navigate to the Udacity folder in your bash interface and inside that cd into the vagrant folder.
 7. Open Git Bash and launch the virtual machine with`vagrant up`
 8. Once Vagrant installs necessary files use `vagrant ssh` to continue.
 9. The command line will now start with vagrant. Here cd into the /vagrant folder.
 10. Unpack the  database folder contents downloaded above over here. You can also copy the contents of this repository here.
 11. To load the database type `psql -d news -f newsdata.sql`
 12. To run the database type `psql -d news`
 13. You must run the commands from the **VIEWS LIST** section below to run the python program successfully.
 14. Use command `python log.py` to run the python program that will fetch every query result.

## Explore the data

- - - -
Once you have the data loaded into your database, connect to your database using `psql -d` news and explore the tables using the \dt and \d table commands and select statements.

* \dt — display tables — lists the tables that are available in the database.
* \d table — (replace table with the name of a table) — shows the database schema for that particular table.

## Connecting from your code

- - - -
The database that you're working with in this project is running PostgreSQL, like the forum database that you worked with in the course. So in your code, you'll want to use the psycopg2 Python module to connect to it, for instance:

`db = psycopg2.connect("dbname=news")`

## VIEWS LIST

- - - -

### 1-num_views
<!--Number of views for each of the eight articles-->

    CREATE VIEW num_views AS SELECT title, COUNT(*) AS views FROM articles, log WHERE SUBSTRING(log.path, 10)=articles.slug GROUP BY title ORDER BY views DESC;

    news=> SELECT * FROM num_views;

                   title               | views
    ------------------------------------+--------
    Candidate is jerk, alleges rival   | 338647
    Bears love berries, alleges bear   | 253801
    Bad things gone, say good people   | 170098
    Goats eat Google's lawn            |  84906
    Trouble for troubled troublemakers |  84810
    Balloon goons doomed               |  84557
    There are a lot of bears           |  84504
    Media obsessed with bears          |  84383

### 2-article_views
<!--Number of views for each article and its author -->

    CREATE VIEW article_views AS SELECT author, num_views.title ,views FROM ((articles JOIN authors ON articles.author = authors.id) JOIN num_views ON articles.title=num_views.title)ORDER BY views DESC;

    news=> SELECT * FROM article_views;

     author |               title                | views
    --------+------------------------------------+--------
        2   | Candidate is jerk, alleges rival   | 338647
        1   | Bears love berries, alleges bear   | 253801
        3   | Bad things gone, say good people   | 170098
        1   | Goats eat Google's lawn            |  84906
        2   | Trouble for troubled troublemakers |  84810
        4   | Balloon goons doomed               |  84557
        1   | There are a lot of bears           |  84504
        1   | Media obsessed with bears          |  84383

### 3-authors_data
<!-- Name of each author with his articles and its number of views -->

     CREATE VIEW authors_data AS SELECT name, author, article_views.title, CAST(views AS INT) FROM article_views JOIN authors ON authors.id=article_views.author ORDER BY views DESC;

    news=> SELECT * FROM authors_data;

              name          | author |               title                | views
    ------------------------+--------+------------------------------------+--------
    Rudolf von Treppenwitz  |      2 | Candidate is jerk, alleges rival   | 338647
    Ursula La Multa         |      1 | Bears love berries, alleges bear   | 253801
    Anonymous Contributor   |      3 | Bad things gone, say good people   | 170098
    Ursula La Multa         |      1 | Goats eat Google's lawn            |  84906
    Rudolf von Treppenwitz  |      2 | Trouble for troubled troublemakers |  84810
    Markoff Chaney          |      4 | Balloon goons doomed               |  84557
    Ursula La Multa         |      1 | There are a lot of bears           |  84504
    Ursula La Multa         |      1 | Media obsessed with bears          |  84383

### 4- errors
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

### 5-reqs
<!-- Total of requists for each day -->

    CREATE VIEW reqs AS SELECT date(time), COUNT(*) AS requists FROM log GROUP BY date(time) ORDER BY date(time);

    news=> SELECT * FROM reqs ORDER BY requists DESC LIMIT 5;
      date     | requists
    ------------+----------
    2016-07-17 |    55907
    2016-07-18 |    55589
    2016-07-19 |    55341
    2016-07-21 |    55241
    2016-07-09 |    55236

### 6-ratio
<!-- The ratio of errors in each day -->

    CREATE VIEW ratio AS SELECT CAST(reqs.date AS text) ,CAST(ROUND((100.0*errors.errs / reqs.requists), 3) AS float(4)) as percent FROM reqs,errors WHERE reqs.date=errors.date ORDER BY reqs.date;

    news=> SELECT * FROM ratio ORDER BY percent DESC LIMIT 5;
        date   | percent
    ------------+---------
    2016-07-17 |   2.263
    2016-07-24 |   0.782
    2016-07-19 |   0.782
    2016-07-05 |   0.775
    2016-07-06 |   0.767

- - - -
This project is made by *Asem Hamdi Abdu*, *assemhamdi1997@gmail.com*, [my github](https://github.com/AsemDevs)
