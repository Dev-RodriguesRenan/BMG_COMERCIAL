import os
import shutil
import pandas as pd
from pathlib import Path

BASE_DOCUMENTS = Path("C:\\Users\\PCVJ\\Documents")
BASE_CARNES = os.path.join(BASE_DOCUMENTS, "carnes")
BASE_INVENTARIO_INDUSTRIA = os.path.join(BASE_DOCUMENTS, "inventario_industria")
BASE_VENDAS_TRANSFERENCIA = os.path.join(BASE_DOCUMENTS, "vendas_transferencia")
if not os.path.exists(BASE_CARNES):
    os.makedirs(BASE_CARNES)
if not os.path.exists(BASE_INVENTARIO_INDUSTRIA):
    os.makedirs(BASE_INVENTARIO_INDUSTRIA)
if not os.path.exists(BASE_VENDAS_TRANSFERENCIA):
    os.makedirs(BASE_VENDAS_TRANSFERENCIA)
for arquivo in os.listdir(BASE_DOCUMENTS):
    if arquivo.endswith(".xlsx"):
        src_path = os.path.join(BASE_DOCUMENTS, arquivo)
        if "Inventario" in arquivo and not "consolidado" in arquivo:
            dst_path = os.path.join(BASE_INVENTARIO_INDUSTRIA, arquivo)
            shutil.move(src_path, dst_path)
        if "VendaTransferencia" in arquivo and not "consolidado" in arquivo:
            dst_path = os.path.join(BASE_VENDAS_TRANSFERENCIA, arquivo)
            shutil.move(src_path, dst_path)
        if "Carne" in arquivo and not "consolidado" in arquivo:
            dst_path = os.path.join(BASE_CARNES, arquivo)
            shutil.move(src_path, dst_path)


def merge_excel_files(folder_path: str):
    all_data = pd.DataFrame()
    for file in os.listdir(folder_path):
        if file.endswith(".xlsx"):
            file_path = os.path.join(folder_path, file)
            filename = f"{file.split('_')[-4]}_{file.split('_')[-3]}_{file.split('_')[-2]}_consolidado.xlsx"
            file_path_consolidado = os.path.join(folder_path, filename)
            df = pd.read_excel(file_path)
            all_data = pd.concat([all_data, df], ignore_index=True)
            all_data.drop_duplicates(inplace=True)
            all_data.to_excel(file_path_consolidado, index=False)
    return file_path_consolidado
