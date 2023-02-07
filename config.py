import os

from os import getenv


API_ID = int(getenv("API_ID", "25181093"))
API_HASH = getenv("API_HASH", "43ce5a99e3c109cbfc52291f9e51f6b2")
SESSION_STRING = getenv("SESSION_STRING", "AQBhixA7xVK-M9ap93lXVPDtf5oEPPYVJPIE2a7btMbH4HyyDcCNsjW9uHSC_wrxrHE1LursktYugv2KVQHv7-sY1fOLhOUJA5bksACT8z16KjD-VGAUHjYUMBtx-5YtByRUTjYfJXcRvNoVZlNTOAWIjKQn0ukJnqzg2cuj3zDeZZ59B1_fEpDqchwYU0zV96VPT8a1lv-1zhCu0AASw8FQNMyD0WEd_VyTnXDCzwtWi04TEfiAXCdgHpqpq_WqYSE_rYIJLQIgGcLBV6wAGcnUJzMAQt2bd7y31fLOjbX8PvVoW5OEZ1wAY0t2sZFtQpNmpa8Jgio1ehSgRn4BPUesAAAAAUI_36sA")
GROUP_ID = int(getenv("GROUP_ID", "-1001568819422")
CHANNEL_OR_GROUP_ID = int(getenv("CHANNEL_OR_GROUP_ID", "-1001726732099"))
MESSAGE_ID = int(getenv("MESSAGE_ID", "682"))
CHANNEL_NAME = getenv("CHANNEL_NAME", "ʙᴏᴛs ᴜᴘᴅᴀᴛᴇ")
TIME_ZONE = getenv("TIME_ZONE", "Asia/Kolkata")
BOT_LIST = list(getenv("BOT_LIST", "ainaxbot vickmusicrobot miffy_robot aina_musicbot").split())
BOT_ADMIN_IDS = list(map(int, getenv("BOT_ADMIN_IDS", "5140509190").split()))
