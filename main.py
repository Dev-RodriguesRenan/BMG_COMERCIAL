import os
import sys
import time
import schedule
import subprocess

BASE_PATH = "C:/Users/Administrator/Downloads/BMG_COMERCIAL"

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
    print(f"Running {file_path}")
    subprocess.run([python_path, "-m", "robot", "-d", "results", file_path])
    print(f"Finished running {file_path}")


def run_all_cases():
    print("Running all cases!!")
    for file in files:
        run_file(file)
    print("All cases finished running!!")
    print("Running excel executor!!")
    subprocess.run([python_path, excel_executor_path])
    print("Finished excel executor!!")


def run_verificator_update():
    print("Running verificator update!!")
    subprocess.run([python_path, verificator_path])
    print("Finished running verificator update!!")


if __name__ == "__main__":
    print("Starting main script...")
    # Execute the keep session script
    time.sleep(5)
    # os.system("configs\\keep_session.bat")
    if len(sys.argv) > 1:
        if sys.argv[1] == "--updater":
            run_file(updater_path)
        elif sys.argv[1] == "--cases":
            run_all_cases()
        elif sys.argv[1] == "--debug":
            print("Running file in debug mode!! awaiting 5 seconds")
            time.sleep(5)
            run_file(updater_path)
            run_all_cases()
        else:
            print("Invalid argument. Use 'updater' or '--debug'.")
            sys.exit(1)
    else:
        print("Waiting hours to start... 06h00")
        # Verifica e atualiza o sistema caso necessário
        schedule.every().day.at("06:00").do(run_file, updater_path)
        # Loop para fechar o updater caso abra no meio da execução
        schedule.every().day.at("06:10").do(run_verificator_update)
        # Executa todos os casos de teste diariamente às 06:10
        schedule.every().day.at("06:10").do(run_all_cases)

        while True:
            schedule.run_pending()
            time.sleep(1)
