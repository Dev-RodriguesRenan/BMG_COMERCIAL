import os
import shutil
import pandas as pd
from pathlib import Path
from email_handler import send_email, email_credentials

# Definindo o caminho base para os documentos
BASE_DOCUMENTS = Path("C:\\Users\\PCVJ\\Documents")
BASE_CARNES = os.path.join(BASE_DOCUMENTS, "carnes")
BASE_INVENTARIO_INDUSTRIA = os.path.join(BASE_DOCUMENTS, "inventario_industria")
BASE_VENDAS_TRANSFERENCIA = os.path.join(BASE_DOCUMENTS, "vendas_transferencia")

message = """
<p>Segue o anexo do arquivo consolidado de {} gerado: </p>
<p><b>{}</b></p>
<p>Atenciosamente,</p>
<p>Equipe de Técnica, (vjbots.com)</p>
"""
# Verificando se as pastas existem, caso não existam, cria-las
if not os.path.exists(BASE_CARNES):
    os.makedirs(BASE_CARNES)
if not os.path.exists(BASE_INVENTARIO_INDUSTRIA):
    os.makedirs(BASE_INVENTARIO_INDUSTRIA)
if not os.path.exists(BASE_VENDAS_TRANSFERENCIA):
    os.makedirs(BASE_VENDAS_TRANSFERENCIA)

# Movendo os arquivos para as pastas corretas
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
    """Merge the Excel files into a single file.
    Args:
        folder_path (str): path of the folder where the files are located

    Returns:
        str: path of the consolidated file
    """
    try:
        all_data = pd.DataFrame()
        for file in os.listdir(folder_path):
            if file.endswith(".xlsx") and not "consolidado" in file:
                file_path = os.path.join(folder_path, file)
                filename = f"{file.split('_')[-4]}_{file.split('_')[-3]}_{file.split('_')[-2]}_consolidado.xlsx"
                file_path_consolidado = os.path.join(folder_path, filename)
                df = get_dataframe_filtered(file_path, file)
                print(f"Arquivo {file_path} lido: {df.head(3)}")
                print("-" * 100)
                all_data = pd.concat([all_data, df], ignore_index=True)
                all_data.drop_duplicates(inplace=True)
                all_data.to_excel(file_path_consolidado, index=False)
        return file_path_consolidado
    except Exception as e:
        print(f"Erro ao processar os arquivos: {e}")
        return None


def get_dataframe_filtered(file_path_dataframe: str, df_name: str):
    """Filter the dataframe according to the file name.

    Args:
        file_path_dataframe (str): full path of the file to be read
        df_name (str): name of the file to be read and filtered

    Returns:
        pd.DataFrame: filtered dataframe
    """
    if "inventario" in df_name.lower():
        print("-" * 100)
        print("Lendo linhas do inventario")
        print("-" * 100)
        return pd.read_excel(file_path_dataframe, header=3)
    if "carne" in df_name.lower():
        print("-" * 100)
        print("Lendo linhas de carnes")
        print("-" * 100)
        return pd.read_excel(file_path_dataframe, header=4)
    if "vendatransferencia" in df_name.lower():
        print("-" * 100)
        print("Lendo linhas do vendas transferencia")
        print("-" * 100)
        return pd.read_excel(file_path_dataframe, header=4)


def main():
    try:
        # gerar o arquivo consolidado de vendas
        filename = merge_excel_files(BASE_VENDAS_TRANSFERENCIA)
        if filename:
            print(
                f"Arquivo consolidado de Relatório de Vendas/Transferências criado: {filename}"
            )
            # enviar arquivo para o e-mail
            send_email(
                subject="Relatório de Vendas/Transferências Consolidado",
                body=message.format(
                    "Relatório de Vendas/Transferências", os.path.basename(filename)
                ),
                to_email=email_credentials["receiver"],
                attachments=filename,
            )
        # gerar o arquivo consolidado de carnes
        filename = merge_excel_files(BASE_CARNES)
        if filename:
            print(
                f"Arquivo consolidado de Relatório de Compra de Carne criado: {filename}"
            )
            # enviar arquivo para o e-mail
            send_email(
                subject="Relatório de Compra de Carne Consolidado",
                body=message.format(
                    "Relatório de Compra de Carne", os.path.basename(filename)
                ),
                to_email=email_credentials["receiver"],
                attachments=filename,
            )
        # gerar o arquivo consolidado de inventario
        filename = merge_excel_files(BASE_INVENTARIO_INDUSTRIA)
        if filename:
            print(
                f"Arquivo consolidado de Relatório de Inventário Indústria criado: {filename}"
            )
            # enviar arquivo para o e-mail
            send_email(
                subject="Relatório de Inventário Indústria Consolidadas",
                body=message.format(
                    "Relatório de Inventário Indústria", os.path.basename(filename)
                ),
                to_email=email_credentials["receiver"],
                attachments=filename,
            )
        print("Todos os arquivos foram processados e enviados com sucesso.")
    except Exception as e:
        print(f"Erro ao processar os arquivos: {e}")


main()
