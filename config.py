import os

from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
SESSION_STRING = getenv("SESSION_STRING", "AQCh_HmNiYrGMOVUfoQOXcHf57QJZ7LJ3eDuwJyHkK92SOHNGLUwbdLa0niP1eLFZepwA0oYItPWvba6myf2UDE1spKo5wulvuSCmpkFFIBvfaxBqxl7bFChXMh7e9T7y_w72xTP99BPqfbyt-TlEgobeRwqbuTGQahBsrwqchAnD87dO_WMxu2Fg9LT5G_Ekm2xwuRYvqSDJPUySdchKaeCxHa0Y8dnP7fTIu3xIBETsY7YcoODtEPiIuklZ6FemL2loZO2KaA3dL66tdlEkNOnr-WkEMCaRDAucjveFSd1DigQnJ-fSAQOh87XRERJoS04VJQSy-dkCIHD1mN-uDPuAAAAAVyIB7AA")
GROUP_ID = int(getenv("GROUP_ID", "-1001801801469"))
CHANNEL_OR_GROUP_ID = int(getenv("CHANNEL_OR_GROUP_ID", "-1001827333320"))
MESSAGE_ID = int(getenv("MESSAGE_ID", "10"))
CHANNEL_NAME = getenv("CHANNEL_NAME", "ʙᴏᴛs ᴜᴘᴅᴀᴛᴇ")
TIME_ZONE = getenv("TIME_ZONE", "Asia/Kolkata")
BOT_LIST = list(getenv("BOT_LIST", "MrsNatashaBot AnonMusicBot NixaRobot").split())
BOT_ADMIN_IDS = list(map(int, getenv("BOT_ADMIN_IDS", "5616461719").split()))
