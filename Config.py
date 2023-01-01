import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "18284121"))
    API_HASH = os.environ.get("API_HASH", "394d0f461eca6d8e6dad237e2a489502")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5958187350:AAGns5YG_o-2OegAjeaGeGPWolrNsb4Q4YQ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "AgC8M_WrrBZuFXA6lmvWqiaDznfaQsGnMqhUv7_dP1xIpm1bDT4t7AvL_-UClSmLt4DIGnqKlC0pwaYNvR7krLkkuqOtkUsUjQNUxDpi9gz2ekljm5OIpYao824wZnCUsnHpjaRILz0ptBcDcKQDg-WclrXLEKKIyOgqVSb5PI_cerVDgpwfAU4d3E_RMcArmte-pjnJ8AYkQ1QJ_eUiehjKWpmNx8Al4ifFrDPkjp-8TL5AuGiTnBGeDpVN4WubuNcjM4A6PcLs6ig5u7_a8I_8QoBge8mBc95PLfhRuE7PE9hgmBbQ-OF3cgjFS4IZ26CNExsSBvX1eFqv6EH9l9mFAAAAATLJcbgA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "YuYanMusicBot")
    SUPPORT = os.environ.get("SUPPORT", "YuYanSupport") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "sonforcess") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/1e420d2670772f1706e2d.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/29f523f1e3bb87ddcfda7.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5147029944")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "2592000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', False) # Change it to "True"
