from numpy import double
import requests
import json
import time
import random
from environs import Env

env = Env()
env.read_env()

chanel = env.list("GAMBLE")
authorization = env.str("AUTHORIZATION")
person_Id = env.str("PERSON_ID")
token = env.str("TOKEN")

command = ['!work', '!coins', '!dice ']
money = 0
header = {
    "Authorization": authorization,
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
}

# data
win = 0
lose = 0
winDouble = 0
winTriple = 0

def getMoney(chanel_id):
    msg = {
        "content": command[command.index('!coins')],
        "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
        "tts": False,
    }
    discord_url = "https://discord.com/api/v9/channels/{}/messages?limit=100".format(chanel_id)
    try:
        res = requests.post(url=discord_url, headers=header, data=json.dumps(msg))
        # print(res)
    except:
        pass

    time.sleep(2)
    res = requests.get(url=discord_url, headers=header)
    result = json.loads(res.content)
    #print(result)
    #res_list = []
    moneyContent = ''
    cmp = '<@!' + person_Id + '>，你有'
    for context in result:
        if len(context['embeds']) != 0:
            if cmp in context['embeds'][0]['description']:
                moneyContent += context['embeds'][0]['description']
                break
                
    #print(moneyContent)
    moneyStartIndex = moneyContent.index('有') + 2
    cmp = ' ' + token
    moneyEndtIndex = moneyContent.index(cmp)
    buf = ''
    for i in range(moneyStartIndex, moneyEndtIndex):
        if moneyContent[i] != ',':
            buf += moneyContent[i]
    
    global money
    money = int(buf)
    #print(buf)
    print('money: ', money)

def content():
    # localtime = time.localtime(time.time())
    # content = "現在時間為: {}:{}:{}".format(localtime.tm_hour, localtime.tm_min, localtime.tm_sec)
    content = "!work"

    return content

def statistics(chanel_id):
    global win, lose, winDouble, winTriple
    discord_url = "https://discord.com/api/v9/channels/{}/messages?limit=100".format(chanel_id)
    res = requests.get(url=discord_url, headers=header)
    result = json.loads(res.content)
    for context in result:
        if ':game_die: Porter' in context['content']:
            if '贏了兩次' in context['content']:
                winDouble += 1
            elif '贏' in context['content']:
                win += 1
            elif '輸' in context['content']:
                lose += 1
        elif ':game_die: :astonished: Porter' in context['content']:
            winTriple += 1


def chat(chanel):
    for chanel_id in chanel:
        getMoney(chanel_id)
        bet = money // 50
        print('bet: ', bet)
        buf = command[command.index('!dice ')]
        buf += str(bet)
        # print(buf)
        for i in range(100):
            msg = {
                "content": buf,
                "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
                "tts": False,
            }
            discord_url = "https://discord.com/api/v9/channels/{}/messages".format(chanel_id)
            try:
                res = requests.post(url=discord_url, headers=header, data=json.dumps(msg))
                # print(res)
            except:
                pass
            time.sleep(random.randrange(10, 15))
            statistics(chanel_id)
    # time.sleep(random.randrange(60, 180))


if __name__ == "__main__":
    while True:
        try:
            # getMoney(chanel[0])
            chat(chanel)
            # sleeptime = 12 #发送间隔时间(秒)
            # time.sleep(sleeptime)
            break
        except:
            break