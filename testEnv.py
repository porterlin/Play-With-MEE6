import os
# from dotenv import load_dotenv
# load_dotenv()
from environs import Env
env = Env()
env.read_env()
# serverIP = env.list("CHANEL")
# a = env.str("AUTHORIZATION")
# print(type(serverIP))
# print(serverIP)
# print(type(a))
# print(a)
# test = env.str('TOKEN')
# print(test)

# with open('result.txt', 'w+') as f:
#     temp = f.readlines()

# cmp = ' = '
# for item in temp:
#     buf = ''
#     start = item.index(cmp) + 3
#     end = item.index('\n')
#     for i in range(start, end):
#         buf += item[i]
#     print(buf)
a = 0
for i in range(100):
    a += 1

print(a)
