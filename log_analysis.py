import psycopg2


conn = psycopg2.connect("dbname=news")
cursor = conn.cursor()


def get_most_pupular():
    cursor.execute("create view log_remove_root_path_fist as select substring(path,10),status from log where status = '200 OK';")
    cursor.execute(
        "select substring,count(substring) as num from log_remove_root_path_fist  join articles  on log_remove_root_path_fist.substring = articles.slug group by log_remove_root_path_fist.substring order by num desc limit 3 ;")
    results = cursor.fetchall()
    print("\nmost popular three articles of all time?")
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


def calculate_percentage(num1,num2):
   # cursor.execute("create view calculate_connect_third as select count(*) from log;")
   # cursor.execute("create view only_date_third as select date(time),status from log where status = '404 NOT FOUND' ")
   # cursor.execute("select date ,count(*) as num from only_date_times group by only_date_times.date order by num desc limit 1;")
       num1 = float(num1)
       num2 = float(num2)
       percentage = '{0:.2f}'.format((num1 / num2 * 100))
       return percentage


get_most_pupular()
get_pupular_authors()
save = calculate_percentage(1234,1677735)
print("\nOn which days did more than 1% of requests lead to errors?")
print("July 17, 2016 "+save+"% error")