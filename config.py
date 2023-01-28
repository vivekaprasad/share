import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = "5619777978:AAGrMIppNwKiihhNSinddozhG5nRmM6JcPk"

#Your API ID from my.telegram.org
APP_ID = 7009965

#Your API Hash from my.telegram.org
API_HASH = "06651b174c4f0591deb0ed1e5663c996"

#Your db channel Id
CHANNEL_ID = -1001564014969

#OWNER ID
OWNER_ID = 1256202333

#Port
PORT = "8080"

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://prasad:12345@cluster0.an5a5sf.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001741057475"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI'm Science Edu Channel File share bot.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1155042800 1879269300 1174588770  5719771565 5018262868 1331744092 5584593509").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "{first}\n\n<b>ඔබ අපගේ සමූහයට තවමත් එකතු වී නොමැත .\n අපගේ සමූහය -@BioVideoFullSyllubus \nමුලින් ම එයට සම්බන්ධ වී නැවත් උත්සාහ කරන්න යන Button එක ක්ලික් කරන්න .\n\nIPhone පරිශිලකයින් Admin කෙනෙක් හරහා ඔබට උවමනා File එක ලබාගන්න -@ScienceEdu_Admin_Contact_Bot\n\n ස්තුතියි")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
