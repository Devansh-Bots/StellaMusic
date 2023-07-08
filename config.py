from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/af2b45f1aff30c6c5f4f1.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/3001ea3ef300201820f2b.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/NotMySpace")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/DadEyeBotz")
l
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1794184828").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
