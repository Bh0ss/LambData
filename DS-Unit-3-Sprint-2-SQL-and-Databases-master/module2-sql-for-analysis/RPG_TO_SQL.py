!pip install psycopg2-binary

import psycopg2
import rpg_db.sqlite3
import sqlite3

# these are the credentials from elephantsql
dbname = 'ncdaxkur'
user = 'ncdaxkur'
password = 'JhT0PJcr1B7b6uuPknq_glB0431_oGkg'
host = 'topsy.db.elephantsql.com'


pg_conn = psycopg2.connect(dbname=dbname,
                           user=user,
                           password=password,
                           host=host)

pg_curs = pg_conn.cursor()

create_table_statement = """
CREATE TABLE test_table(
  id SERIAL PRIMARY KEY,
  name varchar(40) NOT NULL,
  data JSONB
);
"""
pg_curs.execute(create_table_statement)


insert_statement = """
INSERT INTO test_table (name,data) VALUES
(
  'Carl',
  null
),
(
  'Carl but with a JSON',
  null
);
"""
pg_curs.execute(insert_statement)


copied_path = "rpg_db.sqlite3"
sl_conn = sqlite3.connect(copied_path)
sl_curs = sl_conn.cursor()

row_count = "SELECT COUNT(*) FROM charactercreator_character"
sl_curs.execute(row_count).fetchall()
get_characters = "SELECT * FROM charactercreator_character"
characters = sl_curs.execute(get_characters).fetchall()
sl_curs.execute("PRAGMA table_info(charactercreator_character);").fetchall()
create_character = """
CREATE TABLE charactercreator_character(
  character_id SERIAL PRIMARY KEY,
  name VARCHAR(30),
  level int,
  exp int,
  hp int,
  strength int,
  intelligence int,
  dexterity int,
  wisdom int
);
"""

pg_curs.execute(create_character)
pg_conn.commit()

example_insert = """
INSERT INTO charactercreator_character
(name, level, exp, hp, strength, intelligence, dexterity, wisdom)
VALUES""" + str(characters[0][1:]) + ';'
print(example_insert)

for character in characters:
  insert_character = """
  INSERT INTO charactercreator_character
  (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
  VALUES""" + str(characters[0][1:]) + ';'
  
  pg_curs.execute(insert_character)
  
pg_conn.commit()