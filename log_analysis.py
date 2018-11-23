import psycopg2

conn = psycopg2.connect("dbname=news")

cursor = conn.cursor()
# cursor.execute("select title from articles ")
cursor.execute("select path from log limit 10")


results = cursor.fetchall()
for i in results:
    remove_dir_root = i[0]
    if len(remove_dir_root) >1:
        remove_dir_art = remove_dir_root[9:]
        remove_dash = remove_dir_art.replace('-',' ')
        print(remove_dash)

conn.close()