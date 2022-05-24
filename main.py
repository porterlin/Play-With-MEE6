import requests
import json
import time
import random
from environs import Env
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--duration", type=int, help="how many 'hours' to work")
args = parser.parse_args()

#print(args.duration)
# if args.duration == None:
#     print('沒有給參數')
# else:
#     print("工作時間: ", args.duration)
#     localtime = time.localtime(time.time())
#     h = localtime.tm_hour
#     m = localtime.tm_min
#     s = localtime.tm_sec
#     content = "現在時間為: {}:{}:{}".format(h, m, s)
#     print(content)
#     m += 65*int(args.duration)
#     h += m // 60
#     m = m % 60
#     content = "結束時間為: {}:{}:{}".format(h, m, s)
#     print(content)

env = Env()
env.read_env()

def content():
    # localtime = time.localtime(time.time())
    # content = "現在時間為: {}:{}:{}".format(localtime.tm_hour, localtime.tm_min, localtime.tm_sec)
    content = "!work"

    return content


def chat(chanel,authorization):
      header = {
          "Authorization": authorization,
          "Content-Type": "application/json",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
      }
      for chanel_id in chanel:
          msg = {
              "content": content(),
              "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
              "tts": False,
          }
          discord_url = "https://discord.com/api/v9/channels/{}/messages".format(chanel_id)
          try:
              res = requests.post(url=discord_url, headers=header, data=json.dumps(msg))
              print(res.content)
          except:
              pass
          continue
      time.sleep(random.randrange(60, 180))


if __name__ == "__main__":
    chanel = env.list("TEST")
    authorization = env.str("AUTHORIZATION")
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