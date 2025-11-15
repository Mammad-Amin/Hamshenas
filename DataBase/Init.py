import sqlite3

conn = sqlite3.connect(r'G:\Daneshgah\W\HamShenas\DataBase\\HamShenas.db')
db = conn.cursor()

db.execute('''
CREATE TABLE IF NOT EXISTS core (
    id INTEGER PRIMARY KEY,
    username VARCHAR(15),
    name NVARCHAR(64),
    website VARCHAR(320),
    bio TEXT,
    following_count INTEGER,
    follower_count INTEGER,
    post_count INTEGER,
    date_created VARCHAR(10),
    avatar TEXT,
    cores TEXT,
    tags TEXT
)
''')


db.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username VARCHAR(15),
    name NVARCHAR(64),
    website VARCHAR(320),
    bio TEXT,
    following_count INTEGER,
    follower_count INTEGER,
    post_count INTEGER,
    date_created VARCHAR(10),
    avatar TEXT,
    cores TEXT,
    tags TEXT, 
    points INTEGER, 
    parent INTEGER
)
''')




conn.commit()
conn.close()
