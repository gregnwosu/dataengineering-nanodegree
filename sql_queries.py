# DROP TABLES


songplay_table_drop = "DROP TABLE IF EXISTS songplays CASCADE;"
user_table_drop = "DROP TABLE IF EXISTS users CASCADE;"
song_table_drop = "DROP TABLE IF EXISTS songs CASCADE;"
artist_table_drop = "DROP TABLE IF EXISTS artists CASCADE;"
time_table_drop = "DROP TABLE IF EXISTS timestamps CASCADE;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id int PRIMARY KEY,
    start_time time,
    user_id int NOT NULL,
    level varchar ,
    song_id int,
    artist_id int,
    session_id int,
    location varchar,
    user_agent varchar);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
user_id int,
first_name varchar,
last_name varchar,
gender varchar,
level varchar
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs  (
song_id varchar PRIMARY KEY,
title varchar,
artist_id varchar,
year int,
duration float
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
artist_id varchar PRIMARY KEY,
name varchar,
location varchar,
latitude float,
longitude float
);
""")

time_table_create = ("""
 CREATE TABLE IF NOT EXISTS time (
 start_time time,
 hour int,
 day int,
 week int,
 month int,
 year int,
 weekday varchar
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES  (%s, %s, %s, %s, %s, %s , %s, %s, %s);
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s);
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration) 
VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES
  (%s, %s, %s, %s, %s);
""")


time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES
  (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS

song_select = ("""
SELECT * FROM (songs JOIN artists ON songs.artist_id = artists.artist_id) WHERE songs.title = %s  AND artists.name =%s AND songs.duration=%s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]