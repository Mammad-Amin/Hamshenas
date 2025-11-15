from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
api_key = os.getenv("API_KEY")


session = requests.Session()
session.headers.update({'X-API-Key': api_key})


def get_followings(user_id):

    followings = []
    nextCursor = "0"

    while True:
        res = session.get(
        'https://api.tweetapi.com/tw-v2/user/following-list',
        params={'userId': user_id, "count" : "100","cursor" : nextCursor},
        )

        if res.status_code != 200:
            print("GettingFollowingList: Request Failed")
            continue
        res = res.json()

        for item in res["data"]:
            followings.append(
                (
                item["id"],
                item["username"],
                item["name"],
                item["website"],
                item["avatar"],
                item["bio"],
                item["followingCount"],
                item["followerCount"],
                item["tweetCount"],
                item["createdAt"][:10],
                None, 
                None
                )
            )


        nextCursor = res["pagination"]["nextCursor"]
        if(nextCursor == "0"):
            break
    return followings


def get_user_info_by_username(username):
    while True:
        res = session.get(
            'https://api.tweetapi.com/tw-v2/user/by-username',
            params={'username': username},
        )
        if res.status_code != 200:
            print("GettingUserInfo: Request Failed")
            continue
        else:
            break
    return res.json()



def get_user_info_by_ID(userID):
    while True:
        res = session.get(
            'https://api.tweetapi.com/tw-v2/user/by-username',
            params={'username': username},
        )
        if res.status_code != 200:
            print("GettingUserID: userID Failed")
            continue
        else:
            break
    return res.json()



def get_user_ID(username):
    while True:
        res = session.get(
            'https://api.tweetapi.com/tw-v2/user/by-username',
            params={'username': username},
        )
        if res.status_code != 200:
            print("GettingUserInfo: Request Failed")
            continue
        else:
            break
    return res.json()["data"]["id"]



__all__ = ["get_user_ID","get_followings", "get_user_info_by_ID", "get_user_info_by_username"]