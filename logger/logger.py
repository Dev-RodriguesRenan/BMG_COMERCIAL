import datetime
import logging
import os
import sys
import colorama
from dotenv import load_dotenv

load_dotenv()
# Configuração do diretório base para logs
BASE_DIR_LOGS = os.path.join(os.getenv("BASE_PATH", os.getcwd()), "logs")
if not os.path.exists(BASE_DIR_LOGS):
    os.makedirs(BASE_DIR_LOGS)

# definindo as cores
LOG_COLORS = {
    "DEBUG": colorama.Fore.BLUE,
    "INFO": colorama.Fore.GREEN,
    "WARNING": colorama.Fore.YELLOW,
    "ERROR": colorama.Fore.RED,
    "CRITICAL": colorama.Fore.MAGENTA + colorama.Style.BRIGHT,
}
colorama.init(autoreset=True)

# definindo o formato do log
LOG_FORMAT = (
    "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
    "%Y-%m-%d %H:%M:%S",
)


# config da classe formatadora
class HandlerFormatter(logging.Formatter):
    def format(self, record):
        log_color = LOG_COLORS.get(record.levelname, colorama.Fore.WHITE)
        log_msg = super().format(record)
        return f"{log_color}{log_msg}{colorama.Style.RESET_ALL}"


# configurando o logger
logger = logging.getLogger(f"app_{__file__}")
logger.setLevel(logging.DEBUG)

# criando handlers para console e arquivo
console_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler(
    f"{BASE_DIR_LOGS}/app_{os.getpid()}_{datetime.datetime.today().strftime('%d_%m_%Y')}.log"
)

# configurando o formato dos handlers
console_handler.setFormatter(HandlerFormatter(*LOG_FORMAT))
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

# adicionando os handlers ao logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
