import os

from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
SESSION_STRING = getenv("SESSION_STRING", "AQAO4fJXBdUpd7GtEdFOqGJP9sIHldgWZCXY9KQo_TdP43C2imyOIPAJw-TBOvierXq8b_PzZQqTluIWUTBY-xEMa5XUrJvyqvlL5hM04k2NiUfn38GFr_IfYlNg_6-Ua3g_GCWBNIgXBNPMHNbRQqkE8rfzit_2K22Zh0fmhRKkuJS-Iu-2aQsGAg4saSQgi4vM5F2V7Jf24ikgCoEc_iDa8Gx1o6kCdk7_CvjJ1K1TGTFAVynLBRO-EpI72FsbYnMOSU1LudkDq-q5BA0XPOeHdC0o6E7QrFWf3y-Q64n_hKFVeIGoxzY2azwIuE_7QCIA8ZJzLhUutwHCnEsEdwHTAAAAAVyIB7AA")
GROUP_ID = int(getenv("GROUP_ID", "-1001801801469"))
CHANNEL_OR_GROUP_ID = int(getenv("CHANNEL_OR_GROUP_ID", "-1001827333320"))
MESSAGE_ID = int(getenv("MESSAGE_ID", "1"))
CHANNEL_NAME = getenv("CHANNEL_NAME", "ʙᴏᴛs ᴜᴘᴅᴀᴛᴇ")
TIME_ZONE = getenv("TIME_ZONE", "Asia/Kolkata")
BOT_LIST = list(getenv("BOT_LIST", "@MrsNatashaBot, @AnonMusicBot, @NixaRobot").split())
BOT_ADMIN_IDS = list(map(int, getenv("BOT_ADMIN_IDS", "5616461719").split()))
