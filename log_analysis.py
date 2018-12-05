#!/usr/bin/env python
import psycopg2

conn = psycopg2.connect("dbname = news")
cursor = conn.cursor()


def get_most_pupular():
    cursor.execute(
        """
        select substring,count(substring)
        as num from log_fist
        join articles  on log_fist.substring = articles.slug
        group by log_fist.substring order by num desc limit 3 ;
        """)
    results = cursor.fetchall()

    print("\nmost popular three articles of all time?")
    for i in results:
        em_dash = i[0].replace('-', ' ')
        print(em_dash + " -- " + str(i[1]) + ' views')


def get_pupular_authors():
    cursor.execute("""
    select name ,count(name) as num
    from authors_second join log_fist
    on authors_second.slug =
    log_fist.substring group by name order by num desc
    """)
    results = cursor.fetchall()
    print("\nmost popular article authors of all time?")
    for i in results:
        em_dash = i[0].replace('-', ' ')
        print(em_dash + " -- " + str(i[1]) + ' views')


def calculate_percentage():
    cursor.execute("""
    select day, perc from (
    select day, round((sum(req)/(select count(*) from log where
    substring(cast(log.time as text), 0, 11) = day) * 100), 2) as
    perc from (select substring(cast(log.time as text), 0, 11) as day,
    count(*) as req from log where status like '%404%' group by day)
    as log_sum group by day order by perc desc) as resulat
    where perc >= 1
    """)
    results = cursor.fetchall()
    print("\nOn which days did more than 1% of requests lead to errors?")
    for i in results:
        print("{} ---- {}%".format(i[0], i[1]))

if __name__ == '__main__':
    get_most_pupular()
    get_pupular_authors()
    calculate_percentage()

