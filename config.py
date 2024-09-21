import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 23480434
API_HASH = "c4fedb5c4f1132fd35d71a327b777dce"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7702012129:AAG2p-yonBSVHQ9lMWl-mPWgA3ZOOqf041w"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://rajkumarnarauli5:rajkumarnarauli5@cluster0.lif7h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002356341204

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 7317637010

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/sayarkiduniya"
SUPPORT_GROUP = "https://t.me/+6MrgQD-RRIA1MTg9"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "STRING_SESSIONBQFmSHIApKQ_Iba56Zn6SwoYmue0sBjL6gi_KZ_mOxy7l0BHTg-UmGDSWD2hmgtwUE7-UsGl92_I1nM_EH3mUcWrD9jrevV1rfZZv6jSkDyTJIEbEkJ4F0lSatwZtHm7Rryv6TQX8f0Au2pFdbyqoDyrxAxKKWXrqGeSpvja3tXIKakcXxE0DmCnT1FjaGNSV4ILQQTOnjt_KBtgFd6W3WFyoCQ87iWgte5cPxVfjm9joRPFEZ_utjR4Ch4m1xnWBwTkZcKR26snSDPQeiZtKbXAlBhZqm9HxKeGG71q8IScE3ZD-O9gdC_GXqpElELUjC99VbIFZw4pi6VINaaBAjFb24e4WgAAAAFhQkBCAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

https://graph.org/file/f586172fe40a0b5d0b0df.jpg
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/3bc14ec47c39a91a5dbbe.jpg"

PING_IMG_URL = "https://graph.org/file/3bc14ec47c39a91a5dbbe.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/3bc14ec47c39a91a5dbbe.jpg"
STATS_IMG_URL = "https://graph.org/file/3bc14ec47c39a91a5dbbe.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/3bc14ec47c39a91a5dbbe.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/3bc14ec47c39a91a5dbbe.jpg"
STREAM_IMG_URL = "https://graph.org/file/3bc14ec47c39a91a5dbbe.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/3bc14ec47c39a91a5dbbe.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/3bc14ec47c39a91a5dbbe.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/3bc14ec47c39a91a5dbbe.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/3bc14ec47c39a91a5dbbe.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/3bc14ec47c39a91a5dbbe.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
