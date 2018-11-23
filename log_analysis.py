import psycopg2

conn = psycopg2.connect("news")

cursor = conn.cursor()
cursor.execute("select log from news ")

results = cursor.fetchall()
print(results)
conn.close()