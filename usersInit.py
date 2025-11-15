"""

this file fetch accounts followed by CORE into the user table in DB

"""


import sqlite3
from apiCaller import get_followings

conn = sqlite3.connect(r'G:\Daneshgah\W\HamShenas\DataBase\HamShenas.db')
db = conn.cursor()
db.execute("SELECT id FROM core")
core = db.fetchall()

sql = ''' INSERT INTO users
(id, username, name, website, avatar, bio, following_count, follower_count, post_count, date_created, cores, tags, points, parent)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''


for id_tuple in core:
    followings = get_followings(id_tuple[0])
    for item in followings:

    	db.execute(sql, item +(1,id_tuple[0] ))


conn.commit()
conn.close()