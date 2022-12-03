import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "18284121"))
    API_HASH = os.environ.get("API_HASH", "394d0f461eca6d8e6dad237e2a489502")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5958187350:AAGns5YG_o-2OegAjeaGeGPWolrNsb4Q4YQ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1ApWapzMBu3rjxkdhUB1JCTGDvUrSzGljub9ezfXFNJJ7qiZJBypItyAvMIhZK_QcPVedNWobuEXDGAfgo4aa26MSMsXjhSxbb1S7tCMZ9JkLBmg9Dln023w2fVwFJGD49ZDQD0CqYD7WB5dLM-TPqQT_4P1EAs3UN6xFWK359g0sbXUWE5l4zCU4_vIrFfGLX3Ka_cGIuwv-98wP9AC4uHThDaCsMTL8262KF_nwArU5NVW7evOPFEMV2UlnkUpqY_9LQETK9i3Skn-Jd9ISC6G7Rfzn9cQrhte55TzmIuyUA4RKTTtE_v8297kKDDLUIhOK7n11e_6YirxLI84AbrBIFXF_dMo=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "YuYanMusicBot")
    SUPPORT = os.environ.get("SUPPORT", "YuYanSupport") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "sonforcess") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/1e420d2670772f1706e2d.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/29f523f1e3bb87ddcfda7.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5147029944")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
