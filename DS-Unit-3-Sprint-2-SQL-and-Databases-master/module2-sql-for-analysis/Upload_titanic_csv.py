import 'titanic.csv'
import psycopg2
import sqlite3
import pandas

dbname = 'durazwih'
user = 'durazwih'
password = '81hHOIgJoMWtEre_Rq9HdAh0hZHMwnGf'
host = 'topsy.db.elephantsql.com'


pg_conn = psycopg2.connect(dbname=dbname,
                           user=user,
                           password=password,
                           host=host)


cursor = pg_conn.cursor()


df = pd.read_csv('titanic.csv')
df['Survived'] = df['Survived'].map(lambda x: True if x == 1 else False)
df_tuple = [tuple(x) for x in df.values]
insert_query = "INSERT INTO titanic_passengers (survived, pclass, name, sex, age, sibling_spouse_aboard, parent_children_aboard, fare) VALUES %s"
execute_values(cursor, insert_query, df_tuple)
