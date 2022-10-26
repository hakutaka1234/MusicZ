import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "17278438"))
    API_HASH = os.environ.get("API_HASH", "7886b64c08117902bf1aaff07280b512")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5401131082:AAGIo3rJAahobY9vK9tAF7p6rAvzWBfVpko")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "HakutakaRobot")
    SUPPORT = os.environ.get("SUPPORT", "pblovely") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "pblovely") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1807928922")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
