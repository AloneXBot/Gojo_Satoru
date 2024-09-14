
from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = "6392016724:AAGVd5l1161SSymqZQLTckUfMOpEGLh67Y8"
    API_ID = 27201175  # Your APP_ID from Telegram
    API_HASH = "f9fcd5bc0af204efdb06219b5c668fc1"  # Your APP_HASH from Telegram
    OWNER_ID = 6079943111  # Your telegram user id defult to mine
    MESSAGE_DUMP = -1001603822916  # Your Private Group ID for logs
    DEV_USERS = [6079943111]
    SUDO_USERS = [6079943111]
    WHITELIST_USERS = [12314134]
    DB_URI = "mongodb+srv://User:testdb.m14k3kx.mongodb.net/?retryWrites=true&w=majority"  # Your mongo DB URI
    DB_NAME = "MYDB"  # Your DB name
    NO_LOAD = []
    GENIUS_API_TOKEN = "" # Your genius API token or leave it as it is
    AuDD_API = "6ecx4OFG0nlUMqAi9OXQER"
    RMBG_API = "iXkrY3xWBKvi6dJcfCLrRxp5" # Your rmbg API token or leave it as it is
    PREFIX_HANDLER = ["!", "/","$"]
    SUPPORT_GROUP = "AlonesHeaven" #Username without @
    SUPPORT_CHANNEL = "AloneXBots" #Username without @
    VERSION = "VERSION" #Leave it as it is
    TIME_ZONE = 'Asia/Kolkata'
    BDB_URI = "mongodb+srv://hny:zara@cluster0.lfe5o.mongodb.net/?retryWrites=true&w=majority" #If you want your birthday module to work pass mongo db uri u can use same URI but I prefer passing a new one
    WORKERS = 8
    TIME_ZONE = 'Asia/Kolkata'
    BOT_USERNAME = "AloneXRobot"
    BOT_ID = "6392016724"
    BOT_NAME = "Alone"
    owner_username = ""


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "6392016724:AAGVd5l1161SSymqZQLTckUfMOpEGLh67Y8"
    API_ID = 27201175  # Your APP_ID from Telegram
    API_HASH = "f9fcd5bc0af204efdb06219b5c668fc1"  # Your APP_HASH from Telegram
    OWNER_ID = 6079943111  # Your telegram user id defult to mine
    MESSAGE_DUMP = -1001603822916  # Your Private Group ID for logs
    DEV_USERS = [6079943111]
    SUDO_USERS = [6079943111]
    WHITELIST_USERS = [12314134]
    DB_URI = "mongodb+srv://User:testdb.m14k3kx.mongodb.net/?retryWrites=true&w=majority"  # Your mongo DB URI
    DB_NAME = "MYDB"  # Your DB name
    NO_LOAD = []
    GENIUS_API_TOKEN = "" # Your genius API token or leave it as it is
    RMBG_API = "iXkrY3xWBKvi6dJcfCLrRxp5" # Your rmbg API token or leave it as it is
    PREFIX_HANDLER = ["!", "/","$"]
    SUPPORT_GROUP = "AlonesHeaven" #Username without @
    SUPPORT_CHANNEL = "AloneXBots" #Username without @
    VERSION = "VERSION" #Leave it as it is
    TIME_ZONE = 'Asia/Kolkata'
    BDB_URI = "mongodb+srv://hny:zara@cluster0.lfe5o.mongodb.net/?retryWrites=true&w=majority" #If you want your birthday module to work pass mongo db uri u can use same URI but I prefer passing a new one
    WORKERS = 8
