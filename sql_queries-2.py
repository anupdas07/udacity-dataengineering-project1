# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS fact_songplays ;"
user_table_drop = "DROP TABLE IF EXISTS  dim_users ;"
song_table_drop = "DROP TABLE IF EXISTS  dim_songs ;"
artist_table_drop = "DROP TABLE IF EXISTS  dim_artists ;"
time_table_drop = "DROP TABLE IF EXISTS  dim_time ;"

# CREATE TABLES

songplay_table_create = "CREATE TABLE IF NOT EXISTS fact_songplays ( start_time timestamp NOT NULL, user_id varchar NOT NULL, level varchar, song_id varchar, artist_id varchar, session_id int NOT NULL, location varchar, user_agent varchar, PRIMARY KEY(user_id,session_id));"
user_table_create = "CREATE TABLE IF NOT EXISTS dim_users (user_id varchar NOT NULL PRIMARY KEY, first_name varchar, last_name varchar, gender varchar, level varchar);"
song_table_create = "CREATE TABLE IF NOT EXISTS dim_songs (song_id varchar NOT NULL PRIMARY KEY, title varchar, artist_id varchar, year int, durationInSec int);"
artist_table_create = "CREATE TABLE IF NOT EXISTS dim_artists (artist_id varchar NOT NULL PRIMARY KEY, name varchar, location varchar, latitude varchar, longitude varchar);"
time_table_create = "CREATE TABLE IF NOT EXISTS dim_time (start_time timestamp NOT NULL, hour int, day int, week int, month int, year int, weekday int);"

# INSERT RECORDS

songplay_table_insert = (
    """INSERT INTO fact_songplays ( start_time , user_id , level , song_id , artist_id , session_id , location , user_agent ) VALUES ( %s, %s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING;
    """
)

user_table_insert = (
    """
    INSERT INTO dim_users (user_id , first_name , last_name , gender , level ) VALUES (%s, %s, %s,%s,%s) ON CONFLICT(user_id) DO UPDATE SET level = EXCLUDED.level;
    """
)
song_table_insert = (
    """
    INSERT INTO dim_songs (song_id , title , artist_id , year , durationInSec ) VALUES (%s, %s, %s,%s,%s) ON CONFLICT DO NOTHING;
    """
)
artist_table_insert = (
    """
    INSERT INTO dim_artists (artist_id , name , location , latitude , longitude ) VALUES (%s, %s, %s,%s,%s) ON CONFLICT DO NOTHING;
    """
)
time_table_insert = (
    """
    INSERT INTO dim_time (start_time , hour , day , week , month , year , weekday ) VALUES (%s, %s, %s,%s,%s,%s,%s) ON CONFLICT DO NOTHING;
    """
)

# FIND SONGS

song_select = (
    """
SELECT ds.song_id,ds.artist_id 
FROM dim_songs as ds 
JOIN dim_artists as da 
ON ds.artist_id = da.artist_id
WHERE ds.title = %s and da.name = %s and ds.durationInSec=%s;
    """ 
)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]