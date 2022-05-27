import requests
import json
import time
import random
from environs import Env
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--duration", type=int, help="How many 'hours' to work")
args = parser.parse_args()

env = Env()
env.read_env()
chanel = env.list("WORK")
authorization = env.str("AUTHORIZATION")

def chat(chanel,authorization):
    header = {
        "Authorization": authorization,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    }
    for chanel_id in chanel:
        msg = {
            "content": "!work",
            "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
            "tts": False,
        }
        discord_url = "https://discord.com/api/v9/channels/{}/messages".format(chanel_id)
        try:
            res = requests.post(url=discord_url, headers=header, data=json.dumps(msg))
        except:
            pass
    time.sleep(random.randrange(60, 180))


if __name__ == "__main__":
    index = 0
    while True:
        try:
            chat(chanel,authorization)
            index += 1

            if args.duration != None:
                if index == args.duration:
                    break

            sleeptime = 3660 #間隔時間(秒)
            time.sleep(sleeptime)
        except:
            break