

from . import *

try:
    APP_ID = config("APP_ID", "22469064", cast=int)
    API_HASH = config("API_HASH", "c05481978a217fdb11fa6774b15cba32")
    BOT_TOKEN = config("BOT_TOKEN", "7382577497:AAGbfMSCrw2wFfe_op70oCt8BMTZrldkcyc")
    OWNER = config("OWNER_ID", default=7328629001, cast=int)
    LOG = config("LOG_CHANNEL", "-1002170811388", cast=int)
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
