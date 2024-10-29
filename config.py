import os

from dotenv import load_dotenv

load_dotenv(
    "config.env" if os.path.isfile("config.env") else "sample_config.env"
)

BOT_TOKEN = os.environ.get("1717960444:AAEj8RzVudfZiZ4X1BCJc8H25OVZMJvqDio")
API_ID = int(os.environ.get("7923125"))
SESSION_STRING = os.environ.get("BQB45bUAlsTZxhl9gaItz4r1_e5HQ1cR7ocW2YD_4A8vo-OoJEShS3qGC97qYGXQz_7_LdC3taHrsFA2vmjjM_GI8KRCjMNgM7GF1XwBKkP4aPH2dBy0TtJgdmF7PmH254UVsqaCRLlrdpsHUqzqGH5tMnSJFo7bU8ETGOZu9Xmzl_3u-ITiB8TOsMBABAeRMzKQrBm3DFM0GSmwCVCOEfx7kprmKx1XpVUJwNrdIoWbaJFxnc0wHCBA9Ln6paQm_Xbf5f7e70rynTHJBxEetFOjj0ZX9IFRs02FsCrYxf5kZu-scRKLF-YhQIZ7Xt1XUPHsIfg8nxYeDg-NqBBIlmyCgXN3swAAAABmZf78AQ", "")
API_HASH = os.environ.get("a2e9ae5bd82dac01962e630b567e450e")
USERBOT_PREFIX = os.environ.get("USERBOT_PREFIX", "\\")
PHONE_NUMBER = os.environ.get("+919495343715")
SUDO_USERS_ID = list(map(int, os.environ.get("1289524421", "").split()))
LOG_GROUP_ID = int(os.environ.get("-1001682434334"))
GBAN_LOG_GROUP_ID = int(os.environ.get("-1001682434334"))
MESSAGE_DUMP_CHAT = int(os.environ.get("-1001558373319"))
WELCOME_DELAY_KICK_SEC = int(os.environ.get("WELCOME_DELAY_KICK_SEC", 600))
MONGO_URL = os.environ.get("mongodb+srv://alandavid:alan2202@cluster0.orruk2v.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
ARQ_API_KEY = os.environ.get("JBHZOM-QUGLJS-DLYDXZ-WIBKCJ-ARQ")
ARQ_API_URL = os.environ.get("ARQ_API_URL", "https://arq.hamker.dev")
LOG_MENTIONS = os.environ.get("LOG_MENTIONS", "True").lower() in ["true", "1"]
RSS_DELAY = int(os.environ.get("RSS_DELAY", 300))
PM_PERMIT = os.environ.get("PM_PERMIT", "True").lower() in ["true", "1"]
