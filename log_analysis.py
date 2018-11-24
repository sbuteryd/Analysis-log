import psycopg2


# cursor.execute("select title from articles ")
conn = psycopg2.connect("dbname=news")
cursor = conn.cursor()


def get_most_pupular():
    cursor.execute("create view log_remove_root_path_test as select substring(path,10) from log;")
    cursor.execute(
        "select substring,count(substring) as num from log_remove_root_path join articles  on log_remove_root_path.substring = articles.slug group by log_remove_root_path.substring order by num desc limit 3 ;")
    results = cursor.fetchall()
    for i in results:
        em_dash = i[0].replace('-', ' ')
        print(em_dash + " -- " + str(i[1]))
    conn.close()

get_most_pupular()


