import requests
import json
import time
import random
from environs import Env
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--time", required=True, type=lambda d: datetime.strptime(d, '%H:%M:%S'), help="What time do you want to receive your daily reward (format: H:M:S)")
args = parser.parse_args()

env = Env()
env.read_env()
chanel = env.list("DAILY")
authorization = env.str("AUTHORIZATION")

def chat(chanel,authorization):
    header = {
        "Authorization": authorization,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    }
    for chanel_id in chanel:
        msg = {
            "content": "!daily",
            "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
            "tts": False,
        }
        discord_url = "https://discord.com/api/v9/channels/{}/messages".format(chanel_id)
        try:
            res = requests.post(url=discord_url, headers=header, data=json.dumps(msg))
        except:
            pass
    time.sleep(1)


if __name__ == "__main__":  
    h = args.time.time().hour
    m = args.time.time().minute
    s = args.time.time().second
    print("daily time: {}:{}:{}".format(h, m, s))
    while True:
        try:
            localtime = time.localtime(time.time())
            if localtime.tm_hour == h and localtime.tm_min == m and localtime.tm_sec == s:
                chat(chanel,authorization)
        except:
            break