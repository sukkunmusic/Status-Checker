import os


API_ID = int(os.environ("API_ID", "27878007"))
API_HASH = os.environ("API_HASH", "61e70418c7c29d0ce7fe2cc181950ae0")
SESSION_STRING = os.environ("SESSION_STRING", "AQAO4fJXBdUpd7GtEdFOqGJP9sIHldgWZCXY9KQo_TdP43C2imyOIPAJw-TBOvierXq8b_PzZQqTluIWUTBY-xEMa5XUrJvyqvlL5hM04k2NiUfn38GFr_IfYlNg_6-Ua3g_GCWBNIgXBNPMHNbRQqkE8rfzit_2K22Zh0fmhRKkuJS-Iu-2aQsGAg4saSQgi4vM5F2V7Jf24ikgCoEc_iDa8Gx1o6kCdk7_CvjJ1K1TGTFAVynLBRO-EpI72FsbYnMOSU1LudkDq-q5BA0XPOeHdC0o6E7QrFWf3y-Q64n_hKFVeIGoxzY2azwIuE_7QCIA8ZJzLhUutwHCnEsEdwHTAAAAAVyIB7AA")
TIME_ZONE = os.environ("TIME_ZONE", "")
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST", "MrsNatashaBot, AnonMusicBot, NixaRobot").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ("CHANNEL_OR_GROUP_ID", "-1001827333320"))
MESSAGE_ID = int(os.environ("MESSAGE_ID", "10"))
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS", "5616461719").split(' ')]
GRP_ID = os.environ.get("GRP_ID", "-1001801801469")
CHANNEL_NAME = os.environ.get("CHANNEL_NAME", "ʙᴏᴛs ᴜᴘᴅᴀᴛᴇ")
