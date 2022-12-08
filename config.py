import os


API_ID = int(os.environ("API_ID"))
API_HASH = os.environ("API_HASH")
SESSION_STRING = os.environ("SESSION_STRING")
TIME_ZONE = os.environ("TIME_ZONE")
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ("CHANNEL_OR_GROUP_ID"))
MESSAGE_ID = int(os.environ("MESSAGE_ID"))
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]
GRP_ID = os.environ.get("GRP_ID")
CHANNEL_NAME = os.environ.get("CHANNEL_NAME", "@TheBotUpdate")
