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
        "CHAT_ID", "-1001892721748").split()]
    SESSION_STRING = os.environ.get("SESSION_STRING", "BQGMcpgAvvJSBwKA03kkMoLAnkuZjW_AnBxa3FKycw9p0u8YpgDX_PqQt6hHseUjV0R9m_viuLLOUbUBEft0uCF5IhChEH-qO5viDebwoY7wl44zbuYuuOgG6tAedMHvZ1Gq-3lyFA8wL9COduFag1wo6EMBzQRgy-YZqojEC0i_kfnKB50VFv9MYdwL8xcAH4y3OGgL7LcZGC6HTjevzHOoH3T5TT1Db5s0Ypf8Ijat9Eh7j6qI_fQX1CzuZHuisDhByrpbMVK6HOLE02ZNBKF4r9u3YUDwfQ3DtTlWg7X-qyupxtdfxp6gtf3FSMTctbDMfaad4lYONs_0fH01v67g1ikJ2QAAAAF7bZGqAA")
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://m0921594:Rohit11@cluster0.i7dsnm5.mongodb.net/?retryWrites=true&w=majority")
    MONGO_DB_NAME = os.environ.get("MONGO_DB_NAME", "Telegram")


class Script(object):
    START_MESSAGE = os.environ.get("START_MESSAGE", "Start message")
    ACCEPT_MESSAGE = os.environ.get(
        "ACCEPT_MESSAGE", "Hello {m.from_user.mention}!\nYour Request To Join Was Approved") 
