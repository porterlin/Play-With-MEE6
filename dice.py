import requests
import json
import time
import random
from environs import Env
import argparse

parser = argparse.ArgumentParser(epilog="If you don't use -b and -d. The bet will be money divide by 50")
parser.add_argument("-t", "--times", type=int, default=200, help="How many times to play dice (default = 200)")
group = parser.add_mutually_exclusive_group()
group.add_argument("-b", "--bet", type=int, help="How much money do you want to bet")
group.add_argument("-d", "--divide", type=int, help="Your bet will be money divide by number")
args = parser.parse_args()

env = Env()
env.read_env()
chanel = env.list("GAMBLE")
authorization = env.str("AUTHORIZATION")
person_Id = env.str("PERSON_ID")
token = env.str("TOKEN")
name = env.str("NAME")

money = 0
header = {
    "Authorization": authorization,
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
}

number = args.times

datas = [0] * 6 # [ times, win, lose, equal, winDouble, winTriple ]

def getMoney(chanel_id):
    msg = {
        "content": "!coins",
        "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
        "tts": False,
    }
    discord_url = "https://discord.com/api/v9/channels/{}/messages?limit=100".format(chanel_id)
    try:
        res = requests.post(url=discord_url, headers=header, data=json.dumps(msg))
    except:
        pass

    time.sleep(2)
    res = requests.get(url=discord_url, headers=header)
    result = json.loads(res.content)
    moneyContent = ''
    cmp = '<@!' + person_Id + '>，你有'
    for context in result:
        if len(context['embeds']) != 0:
            if cmp in context['embeds'][0]['description']:
                moneyContent += context['embeds'][0]['description']
                break
                
    moneyStartIndex = moneyContent.index('有') + 2
    cmp = ' ' + token
    moneyEndtIndex = moneyContent.index(cmp)
    buf = ''
    for i in range(moneyStartIndex, moneyEndtIndex):
        if moneyContent[i] != ',':
            buf += moneyContent[i]
    
    global money
    money = int(buf)
    print('money: ', money)

def statistics(chanel_id):
    global datas
    discord_url = "https://discord.com/api/v9/channels/{}/messages?limit=100".format(chanel_id)
    res = requests.get(url=discord_url, headers=header)
    result = json.loads(res.content)
    time.sleep(1)
    for context in result:
        if (':game_die: ' + name) in context['content']:
            if '下注了兩次' in context['content']:
                datas[4] += 1
                break
            elif '這是平局' in context['content']:
                datas[3] += 1
                break
            elif '贏' in context['content']:
                datas[1] += 1
                break
            elif '輸' in context['content']:
                datas[2] += 1
                break
        elif (':game_die: :astonished: ' + name) in context['content']:
            datas[5] += 1
            break

def chat(chanel):
    global datas
    for chanel_id in chanel:
        getMoney(chanel_id)
        
        if (args.bet == None) and (args.divide == None):
            bet = money // 50
        elif args.bet == None:
            bet = money // args.divide
        elif args.divide == None:
            bet = args.bet
        
        print('bet: ', bet)
        buf = '!dice '
        buf += str(bet)
        for i in range(number):
            msg = {
                "content": buf,
                "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
                "tts": False,
            }
            discord_url = "https://discord.com/api/v9/channels/{}/messages".format(chanel_id)
            try:
                res = requests.post(url=discord_url, headers=header, data=json.dumps(msg))
                datas[0] += 1
            except:
                pass
            time.sleep(random.randrange(10, 15))
            statistics(chanel_id)

def readData():
    global datas
    with open('result.txt', 'r') as f:
        temp = f.readlines()

    cmp = ' = '
    for i in range(len(temp)):
        buf = ''
        start = temp[i].index(cmp) + 3
        end = temp[i].index('\n')
        for j in range(start, end):
            buf += temp[i][j]
        datas[i] = int(buf)

    print(temp)

def writeData():
    data = ['times = ', 'win = ', 'lose = ', 'eaual = ', 'winDouble = ', 'winTriple = ']
    for i in range(len(data)):
        data[i] += str(datas[i])
        data[i] += '\n'
    
    print(data)
    with open('result.txt', 'w') as f:
        f.writelines(data)


if __name__ == "__main__":
    while True:
        try:
            readData()
            chat(chanel)
            writeData()
            break
        except:
            break