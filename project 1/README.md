# Project Description
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

In this project, we'll apply data modeling with Postgres and build an ETL pipeline using Python. There are fact and dimension tables for a star schema for a particular analytic focus, and  an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

# Project Structure and Schema
The Python project has 3 python files
1. sql_queris.py : this python file has sql queries to drop, create, insert and find songs.
2. create_tables.py : this python file creates a database connection and execute the drop and create queries written in sql queries.
3. etl.py : this python file sets up the ETL pipeline by parsing the data files for song and user usage logs being produced by Sparkify app. This class is responsible to insert data into below fact and dimensiopn tables.

There are 5 tables: 1 fact table and 4 dimesion table following a star schema
1. fact_songplays : fact table for sogns.
2. dim_users : dimension table containing users data.
3. dim_songs : dimension table containg songs data.
4. dim_artists : dimesnion table containing artists data.
5. dim_time : dimension table containg time data.

## fact_songplays

DB Field     | Data Type
------------ | -------------
 songplay_id | SERIAL
 start_time  | timestamp
 user_id     | int
 level       | varchar
 song_id     | varchar
 artist_id   | varchar
 session_id  | int
 location    | varchar
 user_agent  | varchar
 
 
## dim_users

DB Field     | Data Type
------------ | -------------
 user_id     | int
 first_name  | varchar
 last_name   | varchar
 gender      | varchar
 level       | varchar
 user_agent  | varchar
 
 

## dim_songs

DB Field     | Data Type
------------ | -------------
 song_id     | varchar
 artist_id   | varchar
 year        | int
 title       | varchar
 durationInSec  | int
 
 
## dim_artists


DB Field     | Data Type
------------ | -------------
 name        | varchar
 artist_id   | varchar
 longitude   | varchar
 location    | varchar
 latitude    | varchar
 

## dim_time


DB Field     | Data Type
------------ | -------------
 start_time  | timestamp
 hour     | int
 day       | int
 week     | int
 month   | int
 year  | int
 weekday    | int
 user_agent  | varchar
 
 
 
