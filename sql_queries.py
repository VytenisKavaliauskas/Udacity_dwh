import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

#KEY=config.get('AWS','key')
#SECRET= config.get('AWS','secret')
#DB_NAME= config.get("CLUSTER","DB_NAME")
#DB_USER= config.get("CLUSTER","DB_USER")
#DB_PASSWORD= config.get("CLUSTER","DB_PASSWORD")
#DB_PORT = config.get("CLUSTER","DB_PORT")
#HOST = config.get("CLUSTER","HOST")
#ARN = config.get("IAM_ROLE","ARN")

#print(DB_NAME,DB_USER,DB_PASSWORD,DB_PORT,HOST,ARN)
#print(*config['CLUSTER'].values())

# DROP TABLES

staging_events_table_drop = "DROP TABLE IF EXISTS staging_events;"
staging_songs_table_drop = "DROP TABLE IF EXISTS staging_songs;"
songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS song;"
artist_table_drop = "DROP TABLE IF EXISTS artist;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

staging_events_table_create= ("""
CREATE TABLE staging_events 
(
  artist           TEXT NULL,
  auth             TEXT NULL,
  firstName        TEXT NULL,
  gender           TEXT NULL,
  IteminSession    INTEGER NULL,
  lastName         TEXT NULL,
  length           NUMERIC(10,5) NULL,
  level            TEXT NULL,
  location         TEXT NULL,
  method           TEXT NULL,
  page             TEXT NULL,
  registration     TEXT NULL,
  sessionid        INTEGER NULL,
  song             TEXT NULL,
  status           INTEGER NULL,
  ts               BIGINT,
  userAgent        TEXT NULL,
  userId           INTEGER NULL
);
""")

staging_songs_table_create = ("""
CREATE TABLE staging_songs 
(
num_songs          INTEGER NULL,
artist_id          TEXT NULL,
artist_latitude    NUMERIC(10,5) NULL,
artist_longitude   NUMERIC(10,5) NULL,
artist_location    TEXT NULL,
artist_name        TEXT NULL,
song_id            TEXT NULL,
title              TEXT NULL,
duration           NUMERIC(10,5) NULL,
year               INTEGER NULL
)
""")

songplay_table_create = ("""
CREATE TABLE songplay 
(
songplay_id     VARCHAR(50) NOT NULL,
start_time      BIGINT,
user_id         INTEGER NULL,
level           VARCHAR(20) NULL,
song_id         VARCHAR(50) NOT NULL,
artist_id       VARCHAR(50) NULL,
session_id      INTEGER NULL,
location        VARCHAR(50) NULL,
user_agent      VARCHAR(50) NULL
)
""")

user_table_create = ("""
CREATE TABLE users 
(
user_id         INTEGER NULL,
first_name      VARCHAR(50) NULL,
last_name       VARCHAR(50) NULL,
gender          VARCHAR(2) NULL,
level           VARCHAR(20) NULL
)
""")

song_table_create = ("""
CREATE TABLE song 
(
song_id         VARCHAR(50) NOT NULL,
title           VARCHAR(100) NOT NULL,
artist_id       VARCHAR(50) NULL,
year            INTEGER NULL,
duration        NUMERIC(10,5) NULL
)
""")

artist_table_create = ("""
CREATE TABLE artist 
(
artist_id       VARCHAR(50) NULL,
name            VARCHAR(50) NULL,
location        VARCHAR(50) NULL,
lattitude       NUMERIC(10,5) NULL,
longitude       NUMERIC(10,5) NULL
)
""")

time_table_create = ("""
CREATE TABLE time 
(
start_time      BIGINT NULL,
hour            INTEGER NULL,
day             INTEGER NULL,
week            INTEGER NULL,
month           INTEGER NULL,
year            INTEGER NULL,
weekday         INTEGER NULL
)
""")

# STAGING TABLES

staging_events_copy = ("""
copy staging_events from 's3://udacity-dend/log_data' 
credentials 'aws_iam_role={}'
format as json 's3://udacity-dend/log_json_path.json'
region 'us-west-2'
timeformat 'epochmillisecs';
""").format("arn:aws:iam::712051812261:role/dwhRole")

staging_songs_copy = ("""
copy staging_songs from 's3://udacity-dend/song_data' 
credentials 'aws_iam_role={}'
format as json 'auto'
region 'us-west-2';
""").format("arn:aws:iam::712051812261:role/dwhRole")

# FINAL TABLES

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
