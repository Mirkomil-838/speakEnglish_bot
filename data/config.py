from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("5424907566:AAGGuuMSPq05gcrDm3o_1mGYN5NPXw-qDqA")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("213.230.87.164")  # Xosting ip manzili
