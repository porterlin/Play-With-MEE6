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
test = env.str('TOKEN')
print(test)