import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "18284121"))
    API_HASH = os.environ.get("API_HASH", "394d0f461eca6d8e6dad237e2a489502")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5958187350:AAGns5YG_o-2OegAjeaGeGPWolrNsb4Q4YQ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1ApWapzMBuxo-qOQBu6s3BRVDk66TUtFPRV6w0gX-kZXB5VjP6gMidh9bZfwTEJJ2C8bWv6h1rSifOLTuTPczWQFiU4dOx8FYSkBvHK9PTRUTMstgSQYgbTO9h0aVHHoVSuNvQiXJu7UWKsB2UtAcDpFAYkWcfres1MPFEDU9LtxgAFuqfYusif-1BkxtUfU8H5Jvpke3PTnL33wfrhfKw5pVTrbia9cETkLYl1gKoPf1WyslSzyRuKYw8cvpuilSC7IOGk8lLW1JJENB9tPvlytxqHTpZQ7ZkPXSHZ1_d7g0Uv70dWfh9SjpN4wDf7vM3owRS5jZqDRCN417SDMz38AmsTCsXx8=")
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
