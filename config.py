import os

from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
SESSION_NAME = getenv("SESSION_NAME", "")
GROUP_ID = int(getenv("GROUP_ID", "-1001801801469"))
CHANNEL_OR_GROUP_ID = int(getenv("CHANNEL_OR_GROUP_ID", "-1001827333320"))
MESSAGE_ID = int(getenv("MESSAGE_ID", "1"))
CHANNEL_NAME = getenv("CHANNEL_NAME", "ʙᴏᴛs ᴜᴘᴅᴀᴛᴇ")
TIME_ZONE = getenv("TIME_ZONE", "Asia/Kolkata")
BOT_LIST = list(getenv("BOT_LIST", "@MrsNatashaBot, @AnonMusicBot, @NixaRobot").split())
BOT_ADMIN_IDS = list(map(int, getenv("BOT_ADMIN_IDS", "5616461719").split()))
