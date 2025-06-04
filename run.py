import time
import schedule
import subprocess

files = [
    "C:/Users/PCVJ/Desktop/BMG_COMERCIAL/suites/inventario_industria/main.robot",
    "C:/Users/PCVJ/Desktop/BMG_COMERCIAL/suites/relatorio_carne/main.robot",
    "C:/Users/PCVJ/Desktop/BMG_COMERCIAL/suites/vendas_transferencia_carnes/main.robot",
]
updater_path = "C:/Users/PCVJ/Desktop/BMG_COMERCIAL/suites/updater/main.robot"
python_path = "C:/Users/PCVJ/Desktop/BMG_COMERCIAL/venv/Scripts/python"
verificator_path = "C:/Users/PCVJ/Desktop/BMG_COMERCIAL/verificator.py"
excel_executor_path = "C:/Users/PCVJ/Desktop/BMG_COMERCIAL/excel_handler.py"


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


def run_verificator_update():
    print(f"Running verificator update!!")
    subprocess.run([python_path, verificator_path])
    print(f"Finished running verificator update!!")


if __name__ == "__main__":
    # Verifica e atualiza o sistema caso necessário
    schedule.every().day.at("06:50").do(run_file, updater_path)
    # Loop para fechar o updater caso abra no meio da execução
    schedule.every().day.at("07:00").do(run_verificator_update)
    # Executa todos os casos de teste diariamente às 07:00
    schedule.every().day.at("07:00").do(run_all_cases)

    while True:
        schedule.run_pending()
        time.sleep(1)
