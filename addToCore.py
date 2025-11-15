import sqlite3
from apiCaller import get_user_info_by_username
from dotenv import load_dotenv
import os


load_dotenv()

def add_to_core(username):
    res = get_user_info_by_username(username)

    sql = ''' INSERT INTO core
    (id, username, name, website, avatar, bio, following_count, follower_count, post_count, date_created, cores, tags)
              VALUES (?,?,?,?,?,?,?,?,?,?,?,?) '''
    
    info = (
    res["data"]["id"],
    res["data"]["username"],
    res["data"]["name"],
    res["data"]["website"],
    res["data"]["avatar"],
    res["data"]["bio"],
    res["data"]["followingCount"],
    res["data"]["followerCount"],
    res["data"]["tweetCount"],
    res["data"]["createdAt"][:10],
    None,
    None
    )
    db.execute(sql, info)   
    

conn = sqlite3.connect(r'G:\Daneshgah\W\HamShenas\DataBase\\HamShenas.db')
db = conn.cursor()

add_to_core(os.getenv("core_username"))

conn.commit()
conn.close()