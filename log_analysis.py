import psycopg2


# cursor.execute("select title from articles ")
conn = psycopg2.connect("dbname=news")
cursor = conn.cursor()


def get_most_pupular():
    cursor.execute("create view log_remove_root_path_fist as select substring(path,10),status from log where status = '200 OK';")
    cursor.execute(
        "select substring,count(substring) as num from log_remove_root_path_fist  join articles  on log_remove_root_path_fist.substring = articles.slug group by log_remove_root_path_fist.substring order by num desc limit 3 ;")
    results = cursor.fetchall()
    print("most popular three articles of all time?")
    for i in results:
        em_dash = i[0].replace('-', ' ')
        print(em_dash + " -- " + str(i[1])+' views')




def get_pupular_authors():
    cursor.execute("create view articles_authors_second as select slug,name from articles join authors on articles.author = authors.id;")
    cursor.execute("select name ,count(name) as num  from articles_authors join log_remove_root_path_fist on articles_authors.slug =log_remove_root_path_fist.substring group by name order by num desc")
    results = cursor.fetchall()
    print("\nmost popular article authors of all time?")
    for i in results:
        em_dash = i[0].replace('-', ' ')
        print(em_dash + " -- " + str(i[1])+' views')
    conn.close()

get_most_pupular()
get_pupular_authors()