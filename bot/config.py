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
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get(
        "BOT_TOKEN", "")
    OWNER_ID = int(os.environ.get("OWNER_ID", "5897793065"))
    WEB_SERVER = is_enabled(os.environ.get("WEB_SERVER", "True"), True)
    CHAT_ID = [int(x) for x in os.environ.get(
        "CHAT_ID", "-1001939503680").split()]
    SESSION_STRING = os.environ.get("SESSION_STRING", "")
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb://localhost:27017")
    MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME", "telegram")


class Script(object):
    START_MESSAGE = os.environ.get("START_MESSAGE", "Start message")
    ACCEPT_MESSAGE = os.environ.get(
        "ACCEPT_MESSAGE", "You have been accepted to the channel.")
