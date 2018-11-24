import psycopg2

conn = psycopg2.connect("dbname=news")

cursor = conn.cursor()
# cursor.execute("select title from articles ")
cursor.execute("create view log_remove_root_path_test as select substring(path,10) from log;")
cursor.execute("select substring,count(substring) as num from log_remove_root_path join articles  on log_remove_root_path.substring = articles.slug group by log_remove_root_path.substring order by num desc limit 3 ;")

results = cursor.fetchall()
for i in results:
    print(i[0]+" "+str(i[1]))

conn.close()