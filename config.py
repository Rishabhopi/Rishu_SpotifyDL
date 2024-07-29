# Copyright (C) 2024 DX-MODS
#Licensed under the  AGPL-3.0 License;
#you may not use this file except in compliance with the License.
#Author ZIYAN
#if you use our codes try to donate here https://www.buymeacoffee.com/ziyankp

import re
import os
from os import environ,sys
from sys import executable
import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client
import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(message)s",
    handlers = [logging.FileHandler('bot.log'), logging.StreamHandler()]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

try:
    API_ID = int(environ['API_ID',"14050586"])
    API_HASH = environ['API_HASH',"42a60d9c657b106370c79bb0a8ac560c"]
    BOT_TOKEN = environ['BOT_TOKEN']
    DB_URL = environ['DB_URL',"mongodb+srv://Krishna:pss968048@cluster0.4rfuzro.mongodb.net/?retryWrites=true&w=majority"]
    DB_NAME = environ['DB_NAME',"cluster0"]
    OWNER_ID = int(environ['OWNER_ID',"5738579437"])
except KeyError:
    LOGGER.debug("One or More ENV variable not found.")
    sys.exit(1)
# Optional Variable
SUDO_USERS = environ.get("SUDO_USERS",str(OWNER_ID)).split()
SUDO_USERS = [int(_x) for _x in SUDO_USERS]
if OWNER_ID not in SUDO_USERS:
    SUDO_USERS.append(OWNER_ID)
ADMIN = int(environ['ADMIN',"5738579437"])
AUTH_CHATS = environ.get('AUTH_CHATS',None ).split()
AUTH_CHATS = [int(_x) for _x in AUTH_CHATS]
START_PIC = environ['START_PIC',"https://graph.org/file/7f790884507f5778f92bd.jpg"]
LOG_GROUP = environ.get("LOG_GROUP","-1002062847270")
DUMP_GROUP = environ.get("DUMP_GROUP", None)
if LOG_GROUP:
    LOG_GROUP = int(LOG_GROUP)
BUG = environ.get("BUG", None)
if BUG:
    BUG = int(BUG)
GENIUS_API = environ.get("GENIUS_API",None)
MAINTENANCE = bool(environ.get('MAINTENANCE', None))
if GENIUS_API:
    GENIUS_API = GENIUS_API
