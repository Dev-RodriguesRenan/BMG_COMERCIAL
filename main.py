import os
import sys
import time
from dotenv import load_dotenv
import subprocess
import threading
from logger.logger import logger

load_dotenv()
BASE_PATH = os.getenv("BASE_PATH", os.getcwd())

files = [
    f"{BASE_PATH}/suites/inventario_industria/main.robot",
    f"{BASE_PATH}/suites/relatorio_carne/main.robot",
    f"{BASE_PATH}/suites/vendas_transferencia_carnes/main.robot",
]
updater_path = f"{BASE_PATH}/suites/updater/main.robot"
python_path = f"{BASE_PATH}/venv/Scripts/python"
verificator_path = f"{BASE_PATH}/verificator.py"
excel_executor_path = f"{BASE_PATH}/excel_handler.py"


def run_file(file_path):
    logger.info(f"Running {file_path}")
    subprocess.run([python_path, "-m", "robot", "-d", "results", file_path])
    logger.info(f"Finished running {file_path}")


def run_all_cases():
    logger.info("Running all cases!!")
    for file in files:
        run_file(file)
    logger.info("All cases finished running!!")
    logger.info("Running excel executor!!")
    subprocess.run([python_path, excel_executor_path])
    logger.info("Finished excel executor!!")


def run_verificator_update():
    logger.debug("Running verificator update!!")
    subprocess.run([python_path, verificator_path])
    logger.debug("Finished running verificator update!!")


if __name__ == "__main__":
    logger.info("Starting main script...")
    logger.info("Closing RDP...")
    # Execute the keep session script
    time.sleep(10)
    # os.system("configs\\keep_session.bat")
    if len(sys.argv) > 1:
        if sys.argv[1] == "--updater":
            run_file(updater_path)
        elif sys.argv[1] == "--debug":
            logger.debug("Running file in debug mode!! awaiting 5 seconds")
            run_all_cases()
        else:
            logger.error("Invalid argument. Use 'updater' or '--debug'.")
            sys.exit(1)
    else:
        logger.info("Waiting hours to start... 06h00")

        # Executa todos os casos de teste diariamente às 06:00
        logger.info("Running updater first!!")
        updater = threading.Thread(target=run_file, args=(updater_path,))
        updater.start()
        updater.join()
        logger.info("Updater finished running!!")
        logger.info("Running all cases now!!")
        run_all = threading.Thread(target=run_all_cases)
        run_all.start()
        # verificator = threading.Thread(target=run_verificator_update)
        # verificator.start()
        run_all.join()
        # verificator.join()
        logger.info("All tasks completed successfully!")
        sys.exit(0)
