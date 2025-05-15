import subprocess
import threading
import time

files = [
    "C:/Users/PCVJ/Desktop/BMG_COMERCIAL/suites/inventario_industria/main.robot",
    "C:/Users/PCVJ/Desktop/BMG_COMERCIAL/suites/relatorio_carne/main.robot",
    "C:/Users/PCVJ/Desktop/BMG_COMERCIAL/suites/vendas_transferencia_carnes/main.robot",
]
python_path = "C:/Users/PCVJ/Desktop/BMG_COMERCIAL/venv/Scripts/python"
updater_path = "C:/Users/PCVJ/Desktop/BMG_COMERCIAL/verificator.py"
excel_executor_path = "C:/Users/PCVJ/Desktop/BMG_COMERCIAL/email_handler.py"


def run_file(file_path):
    print(f"Running {file_path}")
    subprocess.run([python_path, "-m", "robot", "-d", "results", file_path])
    print(f"Finished running {file_path}")


def run_all_cases():
    while True:
        print("Running all cases!!")
        for file in files:
            run_file(file)
        print("All cases finished running!!")
        print("Running excel executor!!")
        subprocess.run([python_path, excel_executor_path])
        print("Finished excel executor!!")
        print("Sleeping for 1 day...")
        time.sleep(3600 * 24)


def run_verificator_updade():
    print(f"Running verificator update!!")
    subprocess.run([python_path, updater_path])
    print(f"Finished running verificator update!!")


if __name__ == "__main__":
    thread_1 = threading.Thread(target=run_all_cases)
    thread_2 = threading.Thread(target=run_verificator_updade)
    thread_1.start()
    thread_2.start()
