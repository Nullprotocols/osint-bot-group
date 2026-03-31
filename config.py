# config.py - Complete configuration for OSINT Pro Bot on Render

import os

# ==================== BOT TOKEN ====================
BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

# ==================== DATABASE ====================
DB_PATH = "bot_database.db"

# ==================== OWNER & ADMINS ====================
OWNER_ID = int(os.environ.get("OWNER_ID", "8104850843"))
INITIAL_ADMINS_STR = os.environ.get("INITIAL_ADMINS", "8104850843,5987905091")
INITIAL_ADMINS = [int(x.strip()) for x in INITIAL_ADMINS_STR.split(",") if x.strip()]

# ==================== FORCE JOIN CHANNELS ====================
FORCE_JOIN_CHANNELS = [
    {"name": "All Data Here", "link": "https://t.me/all_data_here", "id": -1003090922367},
    {"name": "OSINT Lookup", "link": "https://t.me/osint_lookup", "id": -1003698567122},
    {"name": "LEGEND CHATS", "link": "https://t.me/legend_chats_osint", "id": -1003672015073}
]

# ==================== LOG CHANNELS (per command) ====================
LOG_CHANNELS = {
    "num": -1003482423742,
    "ifsc": -1003624886596,
    "email": -1003431549612,
    "gst": -1003634866992,
    "vehicle": -1003237155636,
    "vchalan": -1003237155636,
    "pincode": -1003677285823,
    "insta": -1003498414978,
    "git": -1003576017442,
    "pak": -1003663672738,
    "ip": -1003665811220,
    "ffinfo": -1003588577282,
    "ffban": -1003521974255,
    "tg2num": -1003642820243,
    "tginfo": -1003643170105,
    "tginfopro": -1003643170105,
}

# ==================== GLOBAL BRANDING BLACKLIST ====================
GLOBAL_BLACKLIST = [
    "@patelkrish_99", "patelkrish_99", "t.me/anshapi", "anshapi",
    "@Kon_Hu_Mai", "Kon_Hu_Mai", "Dm to buy access"
]

# ==================== COMMANDS ====================
COMMANDS = {
    "num": {
        "url": "https://api.b77bf911.workers.dev/mobile?number={}",
        "param": "10-digit number",
        "log": LOG_CHANNELS["num"],
        "desc": "Phone number basic lookup",
        "extra_blacklist": []
    },
    "tg2num": {
        "url": "https://tg-to-num-six.vercel.app/?key=rootxsuryansh&q={}",
        "param": "user id",
        "log": LOG_CHANNELS["tg2num"],
        "desc": "Telegram user ID to number (if available)",
        "extra_blacklist": ['"response_time": "1189ms",',
  '"credit": "@Shuubbhhhaaammm",',
  '"owner": "@Ayano_mindx",',
  '"admin": "@anuragxanuu",',
  '"help_group": "https://t.me/hackedanurag",',
  '"note": "brother"', '9277193139']
    },
    "vehicle": {
        "url": "https://vehicle-info-aco-api.vercel.app/info?vehicle={}",
        "param": "RC number",
        "log": LOG_CHANNELS["vehicle"],
        "desc": "Vehicle registration details",
        "extra_blacklist": []
    },
    "vchalan": {
        "url": "https://api.b77bf911.workers.dev/vehicle?registration={}",
        "param": "RC number",
        "log": LOG_CHANNELS["vchalan"],
        "desc": "Pending & paid chalan info",
        "extra_blacklist": []
    },
    "ip": {
        "url": "https://abbas-apis.vercel.app/api/ip?ip={}",
        "param": "IP address",
        "log": LOG_CHANNELS["ip"],
        "desc": "IP geolocation & ISP details",
        "extra_blacklist": []
    },
    "email": {
        "url": "https://abbas-apis.vercel.app/api/email?mail={}",
        "param": "email",
        "log": LOG_CHANNELS["email"],
        "desc": "Email validation & domain info",
        "extra_blacklist": []
    },
    "ffinfo": {
        "url": "https://abbas-apis.vercel.app/api/ff-info?uid={}",
        "param": "uid",
        "log": LOG_CHANNELS["ffinfo"],
        "desc": "Free Fire basic player info",
        "extra_blacklist": [
            "developer",
            "AnkuCode",
            "TryByte || Ankucode",
            "channel",
            "TryByte"
        ]
    },
    "ffban": {
        "url": "https://abbas-apis.vercel.app/api/ff-ban?uid={}",
        "param": "uid",
        "log": LOG_CHANNELS["ffban"],
        "desc": "Free Fire ban status check",
        "extra_blacklist": []
    },
    "pincode": {
        "url": "https://api.postalpincode.in/pincode/{}",
        "param": "6-digit pincode",
        "log": LOG_CHANNELS["pincode"],
        "desc": "Area & post office details",
        "extra_blacklist": []
    },
    "ifsc": {
        "url": "https://abbas-apis.vercel.app/api/ifsc?ifsc={}",
        "param": "IFSC code",
        "log": LOG_CHANNELS["ifsc"],
        "desc": "Bank branch details",
        "extra_blacklist": []
    },
    "gst": {
        "url": "https://api.b77bf911.workers.dev/gst?number={}",
        "param": "GST number",
        "log": LOG_CHANNELS["gst"],
        "desc": "GST registration info",
        "extra_blacklist": []
    },
    "insta": {
        "url": "https://mkhossain.alwaysdata.net/instanum.php?username={}",
        "param": "username",
        "log": LOG_CHANNELS["insta"],
        "desc": "Instagram public profile info",
        "extra_blacklist": []
    },
    "tginfo": {
        "url": "https://api.b77bf911.workers.dev/telegram?user={}",
        "param": "username/userid",
        "log": LOG_CHANNELS["tginfo"],
        "desc": "Telegram basic info",
        "extra_blacklist": []
    },
    "tginfopro": {
        "url": "https://tg-to-num-six.vercel.app/?key=rootxsuryansh&q={}",
        "param": "username/userid",
        "log": LOG_CHANNELS["tginfopro"],
        "desc": "Telegram advanced profile data",
        "extra_blacklist": ['"response_time": "1189ms",',
  '"credit": "@Shuubbhhhaaammm",',
  '"owner": "@Ayano_mindx",',
  '"admin": "@anuragxanuu",',
  '"help_group": "https://t.me/hackedanurag",',
  '"note": "brother"', '9277193139']
    },
    "git": {
        "url": "https://abbas-apis.vercel.app/api/github?username={}",
        "param": "username",
        "log": LOG_CHANNELS["git"],
        "desc": "GitHub account details",
        "extra_blacklist": []
    },
    "pak": {
        "url": "https://abbas-apis.vercel.app/api/pakistan?number={}",
        "param": "number",
        "log": LOG_CHANNELS["pak"],
        "desc": "Pakistan phone lookup",
        "extra_blacklist": []
    },
}

# ==================== BRANDING & FOOTER ====================
BRANDING = {
    "developer": "@Nullprotocol_X",
    "powered_by": "NULL PROTOCOL"
}
CMD_LIST_FOOTER = "\n\n────────────────────────────\n⚡ Fast • Accurate • Secure\n👨‍💻 DEVELOPED BY NULL PROTOCOL"
REDIRECT_BOT = "@osintfatherNullBot"

# ==================== WEBHOOK ====================
# Webhook URL hardcoded – environment variable ki zaroorat nahi
WEBHOOK_URL = "https://grp-xk6x.onrender.com/webhook"
