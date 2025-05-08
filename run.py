import subprocess

files = [
    "C:/Users/PCVJ/Desktop/BMG_COMERCIAL/suites/inventario_industria/main.robot",
    "C:/Users/PCVJ/Desktop/BMG_COMERCIAL/suites/relatorio_carne/main.robot",
    "C:/Users/PCVJ/Desktop/BMG_COMERCIAL/suites/vendas_transferencia_carnes/main.robot",
]
python_path = "C:/Users/PCVJ/Desktop/BMG_COMERCIAL/venv/Scripts/python"


def run_file(file_path):
    print(f"Running {file_path}")
    subprocess.run([python_path, "-m", "robot", "-d", "results", file_path])
    print(f"Finished running {file_path}")


for file in files:
    run_file(file)
