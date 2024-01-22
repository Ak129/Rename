import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "26562289")

API_HASH = os.environ.get("API_HASH", "d7426fd6f91cff563d62d318a7e5aab1")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6989442605:AAEKfz7YTfsIKclaVV6Sbh5Y9FjegCLF0Ag") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1002140562507") 

DB_NAME = os.environ.get("DB_NAME", "apkthugs")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://apkthugs:abhishekooo@cluster0.ko0vhvz.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/19f85da7b34528d7c7d0b.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5454532062').split()]

