#!/usr/bin/env python
import psycopg2


conn = psycopg2.connect("dbname=news")
cursor = conn.cursor()


def get_most_pupular():
    cursor.execute("create view log_fist "
                   "as select substring(path,10),status from "
                   "log where status = '200 OK';")
    cursor.execute(
        "select substring,count(substring) "
        "as num from log_fist  "
        "join articles  on log_fist.substring = articles.slug "
        "group by log_fist.substring order by num desc limit 3 ;")
    results = cursor.fetchall()

    print("\nmost popular three articles of all time?")
    for i in results:
        em_dash = i[0].replace('-', ' ')
        print(em_dash + " -- " + str(i[1])+' views')


def get_pupular_authors():
    cursor.execute("create view authors_second as "
                   "select slug,name from articles join "
                   "authors on articles.author = authors.id;")
    cursor.execute("select name ,count(name) as num  "
                   "from authors_second join log_fist "
                   "on authors_second.slug = "
                   "log_fist.substring group by name order by num desc")
    results = cursor.fetchall()
    print("\nmost popular article authors of all time?")
    for i in results:
        em_dash = i[0].replace('-', ' ')
        print(em_dash + " -- " + str(i[1])+' views')


def calculate_percentage():
    cursor.execute("create view calculate_third as select count(*) from log;")
    cursor.execute("select * from calculate_third")
    results = cursor.fetchall()
    sum = results[0]
    return sum


def connect_error(sum_all):
    cursor.execute("create view error_third as select date(time),status "
                   "from log where status = '404 NOT FOUND' ")
    cursor.execute("select date ,count(*) as num from "
                   "error_third group by error_third.date"
                   " order by num desc limit 1;")
    results = cursor.fetchall()
    error_sum = results[0]
    date = results[0][0]
    error_max = error_sum[1]
    print("\nOn which days did more than 1% of requests lead to errors?")
    text_sum = "{},{} errors".format(date, (error_max/sum_all) * 100)
    print(text_sum)


get_most_pupular()

get_pupular_authors()

sum_all = calculate_percentage()
connect_error(sum_all[0])
