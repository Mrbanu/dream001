import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "18284121"))
    API_HASH = os.environ.get("API_HASH", "394d0f461eca6d8e6dad237e2a489502")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5958187350:AAGns5YG_o-2OegAjeaGeGPWolrNsb4Q4YQ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1ApWapzMBu03w040C_2udtRRGY5-FZu_-IDHzG1vVkxKwqeXeJbIoWTF6cl3iSRjtHAVsCiZX1Vlr9hbsFa6O2dvJCCAi8RYp2xrtUPkrxzhGLD7A8v-8b5chWwRetGlC-vbTJHMCye6-Vsh6p3kKorPqfFdUOTH7ibl6pbDEOXgOFVmwIeGB_dVdZNtB3o6ksZnNpqre7mfZAAyg_IUsgxKw_oEI2ViiBcN3v-S14AmaHRM1tg2eMDG_QfwOOb1nwyWeG0K9pakMcERSEeU-SOxLp3i8VU48-yi2T4lSL23i3s_LKjgt_Yf9aRCNk3nxCDow94dHoMAqe33ISJ_xlaltShdUHr4=")
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
