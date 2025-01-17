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
    API_ID = int(os.environ.get("API_ID", "21787593"))
    API_HASH = os.environ.get("API_HASH", "0a5c5e27ce46ad36e19eb91c02affb99")
    BOT_TOKEN = os.environ.get(
        "BOT_TOKEN", "6059695462:AAHHGQk0mQj-Q06Yt7_8yoiBejI-HwCN90k")
    OWNER_ID = int(os.environ.get("OWNER_ID", "5521380948"))
    WEB_SERVER = is_enabled(os.environ.get("WEB_SERVER", "True"), True)
    CHAT_ID = [int(x) for x in os.environ.get(
        "CHAT_ID", "-1001654163482").split()]
    SESSION_STRING = os.environ.get("SESSION_STRING", "BQAf70YAPdpvAVK9niqWU_-60AL9-LpMewTd7vP_3XwFaXGjLQZNDCZP8POOBMolgDi274fe2x4ayWSRYrdr1LKppgoLnIsTRzvhavXfnEOW6imXqu_rGuwLQWykr2xkYIn_xJfs29LPUwD1ChrDAXUAOMmDIwXt8lfyRf-BrHi7HolndDcJkPUHXgTG5TukYA-oVvzaTOuhLP5fXk5Dvs6OIib4yNu-08h65UlctSNksYNj8VBDTwtmp7mIEj0UGrhtUsZx9NNNgoAPxQCtuoSKZW02wP2QuMoObvToM-mPqNgmDcKlZGbF3UOkHrFK7dITstWkBUm21FcC1lXaSS52DVQRHAAAAAF36wJCAA")
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://Rohit33:Rohit33@cluster0.i7dsnm5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME", "Telegram")


class Script(object):
    START_MESSAGE = os.environ.get("START_MESSAGE", "Start message")
    ACCEPT_MESSAGE = os.environ.get(
        "ACCEPT_MESSAGE", "Hello {m.from_user.mention}!\nYour Request To Join Was Approved") 
