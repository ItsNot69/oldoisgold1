import os
from dotenv import load_dotenv

load_dotenv()


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


class Config(object):
    API_ID = int(os.environ.get("API_ID", "28122614"))
    API_HASH = os.environ.get("API_HASH", "f7fbfd8ab95975bf42e9e67b33affeb4")
    BOT_TOKEN = os.environ.get(
        "BOT_TOKEN", "6059695462:AAHHGQk0mQj-Q06Yt7_8yoiBejI-HwCN90k")
    OWNER_ID = int(os.environ.get("OWNER_ID", "5521380948"))
    WEB_SERVER = is_enabled(os.environ.get("WEB_SERVER", "True"), True)
    CHAT_ID = [int(x) for x in os.environ.get(
        "CHAT_ID", "-1001811570311").split()]
    SESSION_STRING = os.environ.get("SESSION_STRING", "BQGtHfYAec7-xLDFRHpMbWcuTc0laakaE4goiCLLhQLlRBJ3R596G6cbdRxRXmusvdr4YsS0czQ9FfI3RfcoRO98qoDuhdakuVwEuBNpZTlO9epsFkFBjpmS2d4z4nvuFVz2ES3xURZIcixqdmCznHzKKnWo47eYhXQ_0JEWwbAZoTJoHBJNA7RbpYZ0Pcrv1vxPuJGRuVmiPi397LkqzmoIqCr6c1PBcmHDVxi1UxSYaEpv9uopW2trH6Lh5IP-pTuhZQ35M5oZDHe8QHMiCm3s5wt9dInJf73vP50tLm4S5CkpRmjLrITM-l2HM1lt5s6iDh5BHG27lggbyW3WCqn7LHlJjgAAAAFZz5IaAA")
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://finalaccept:Rohit44@cluster0.ftmhdcc.mongodb.net/?retryWrites=true&w=majority")
    MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME", "telegram")


class Script(object):
    START_MESSAGE = os.environ.get("START_MESSAGE", "Start message")
    ACCEPT_MESSAGE = os.environ.get(
        "ACCEPT_MESSAGE", "Your Request To Join {m.chat.title} Was Approved") 
