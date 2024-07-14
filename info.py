import os

API_ID = os.getenv('API_ID')
if API_ID is None:
    raise ValueError("API_ID is not set")

API_HASH = os.getenv('API_HASH')
if API_HASH is None:
    raise ValueError("API_HASH is not set")

BOT_TOKEN = os.getenv('BOT_TOKEN')
if BOT_TOKEN is None:
    raise ValueError("BOT_TOKEN is not set")

SESSION = os.getenv('SESSION')
if SESSION is None:
    raise ValueError("SESSION is not set")

DATABASE_URI = os.getenv('DATABASE_URI')
if DATABASE_URI is None:
    raise ValueError("DATABASE_URI is not set")

LOG_CHANNEL = os.getenv('LOG_CHANNEL')
if LOG_CHANNEL is None:
    raise ValueError("LOG_CHANNEL is not set")

ADMIN = os.getenv('ADMIN')
if ADMIN is None:
    raise ValueError("ADMIN is not set")
else:
    ADMIN = int(ADMIN)

CHANNEL = os.getenv('CHANNEL')
if CHANNEL is None:
    raise ValueError("CHANNEL is not set")
