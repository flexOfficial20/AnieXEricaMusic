import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID","20533795"))
API_HASH = getenv("API_HASH","f6cadf28523943f525e706e6ace8a250")
BOT_TOKEN = getenv("BOT_TOKEN","6999969950:AAHCSV2jk8fkEbU_7xTrQhfKSCGcbWynRJs")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Zxcdc:zxchypernjqjjqv8762@cluster0.hcgtozy.mongodb.net/?retryWrites=true&w=majority")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "999999999"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1002078575375"))
BOTADDLOGS = int(getenv("BOTADDLOGS", "-1002078575375")) # LOGGER_ID Id Also Use No Problem
GBAN_LOGS = int(getenv("GBAN_LOGS", "-1002078575375"))
GCAST_USERS = list(map(int, getenv("GCAST_USERS", "6584789596").split()))
OWNER_ID = int(getenv("OWNER_ID", 6584789596))
OWNER = int(getenv("OWNER", 6584789596))
OWNER_USERNAME = getenv("OWNER_USERNAME","FLEXdub_Official")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "HRKU-588310e1-3ddf-4208-a517-ae0f4508047e")
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/AbhiModszYT/AnieXEricaMusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN",None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FLEX_BOTS_NEWS")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/FLEX_SUPPORT_CHAT")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "99999"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", 7000))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", 7000))
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "9999")) 
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))
STRING1 = getenv("STRING_SESSION", "BQE5UiMAjurVvK0RykFxXllSFBFZQOry1K_i5nzN75rHM0bIvds21NwdR_wj9FM3WTSFqDGPKgZxXl4c56APU_IfDsI63jjwYpDeSv2kRfWA21HhvgFCkiSp54ZgSvF36Lii3QAul5SxNe27AXePAM8yow2EX-wEzPmggzgyXYcqy7nI3N5bBEl8qaAW86Y-LdNaO5_e4xztO8mVMb-IFkxexQObKrCl_-QIINwYzcUuzx3u1QyUGyVttspwfhrmjPg8zLHV90Ehb00cZdSrCjhT0v4d5IYTSh1VfULUdS9YcbB3gzsnHe8z5ycZwQpCxQf7w1Z2NJ2Tw51lC2ts4efwFYYw0QAAAAF-Ni2lAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
AMBOT = [
    "🔎",
    "🔍",
    "✨",
    "ᴘʟꜱ ᴡᴀɪᴛ..",
    "ᴘʀᴏᴄᴇꜱꜱɪɴɢ..",
]

START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/5abc92f2c2367baf29fa3.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://graph.org/file/f234fa4e140eb1b85d185.jpg")
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://graph.org/file/f234fa4e140eb1b85d185.jpg")
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
