import requests
import json
import time
import random
from environs import Env

env = Env()
env.read_env()

chanel = env.list("TEST")
authorization = env.str("AUTHORIZATION")
money = 0
header = {
    "Authorization": authorization,
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
}

def getMoney(chanel_id):
    discord_url = "https://discord.com/api/v9/channels/{}/messages?limit=100".format(chanel_id)
    res = requests.get(url=discord_url, headers=header)
    result = json.loads(res.content)
    print(result)
if __name__ == "__main__":
    getMoney(chanel[0])