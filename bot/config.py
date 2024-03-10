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
    API_ID = int(os.environ.get("API_ID", "28726816"))
    API_HASH = os.environ.get("API_HASH", "45edf74203ecf6ff14b394a9e47dca34")
    BOT_TOKEN = os.environ.get(
        "BOT_TOKEN", "6059695462:AAHHGQk0mQj-Q06Yt7_8yoiBejI-HwCN90k")
    OWNER_ID = int(os.environ.get("OWNER_ID", "5521380948"))
    WEB_SERVER = is_enabled(os.environ.get("WEB_SERVER", "True"), True)
    CHAT_ID = [int(x) for x in os.environ.get(
        "CHAT_ID", "-1001654163482").split()]
    SESSION_STRING = os.environ.get("SESSION_STRING", "BQGkDLEAhbmv4nkwbt0IYrMUMVS1YGbdh97lLuo2KYRE5ZYUl3W__lXahM5LszZEcimRwWNvKNDxd1klIJvFtDLSc8PTTJWll8sINZQHrXXOYO3iLN7KMFTfPGnJCMTrPCrTUOQH-EtMQjsbc3Kb_s1YqL8nzVC3PU5S-MsQkkRSpdZqX2RcSx0ZZHXwFz1_1Vty11qn67P-rmtH0jG5oBQtRjUaOArgSjTfUil7Z1mG4r55_iCLEpfe4Lr851wBsEW8OWOzA3-70zboUoXu0in1slyZs1MveoYsr-KoHvXstegRJzo0IeI3Yam7R9mTI4RqcsbKxIPaH71xV_oCaJWaomDX9QAAAAGawFWaAQ")
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://m0921594:Rohit11@cluster0.i7dsnm5.mongodb.net/?retryWrites=true&w=majority")
    MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME", "Telegram")


class Script(object):
    START_MESSAGE = os.environ.get("START_MESSAGE", "Start message")
    ACCEPT_MESSAGE = os.environ.get(
        "ACCEPT_MESSAGE", "Hello {m.from_user.mention}!\nYour Request To Join Was Approved") 
