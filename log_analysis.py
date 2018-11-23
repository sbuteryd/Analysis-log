import psycopg2

conn = psycopg2.connect("dbname=news")

cursor = conn.cursor()
cursor.execute("select * from articles ")

results = cursor.fetchall()
print(results)
conn.close()