# Robô de Extração e Relatórios BMG Comercial

## O que é?

Este projeto é um robô de extração e consolidação de relatórios desenvolvido para a BMG Comercial. Ele integra testes automatizados com o Robot Framework, scripts em Python e bibliotecas como SikuliLibrary e PyAutoGUI para interagir com a interface do sistema FJ Frigo.  

## Para que serve?

O robô automatiza a extração e consolidação de relatórios relacionados a:
- **Inventário de Indústria:** Extração e consolidação de dados do inventário.
- **Compra e Relatório de Carnes:** Geração dos relatórios de carnes.
- **Vendas e Transferência de Carnes:** Extração dos dados referentes às vendas e transferências de carnes.

Além disso, o sistema agrupa os arquivos extraídos, consolida os dados em planilhas XLSX usando o pandas, e envia os relatórios consolidados por e-mail.

## O que faz?

- **Interação com o Sistema:**  
  Utiliza Robot Framework e SikuliLibrary para realizar ações na interface (como cliques, preenchimento de formulários, navegação entre menus) no sistema FJ Frigo.

- **Execução Automatizada de Testes:**  
  Os arquivos `.robot` localizados na pasta `suites` possuem testes que executam os cenários para extrair os relatórios de cada área. Os testes são executados em threads paralelas (conforme definido no `run.py`).

- **Consolidação e Processamento de Dados:**  
  O script `excel_handler.py` move os arquivos XLSX para as pastas corretas e, utilizando o pandas, consolida os dados de vários relatórios em uma única planilha, processo realizado para cada cenário (Inventário Indústria, Relatório de Carnes e Vendas e Transferências de Carnes), após a consolidação os envia por e-mail.  
   
- **Envio de Relatórios por E-mail:**  
  Após a consolidação, o script `excel_handler.py` chama uma função de envio de `email_handler.py` e envia os relatórios consolidados para os destinatários configurados, utilizando autenticação via e-mail.

- **Verificação e Atualização do Sistema:**  
  O `verificator.py` monitora a presença de janelas de atualização no sistema e automatiza a pressão da tecla "enter" ou encerra atualizadores, garantindo que o sistema FJ Frigo permaneça utilizável durante a execução dos testes.

## Estrutura do Projeto

- **suites/**:  
  Contém os arquivos de teste (.robot) para os diferentes relatórios (Inventário, Carnes, Vendas/Transferência).

- **keywords/**:  
  Define palavras-chave reutilizáveis, organizadas por área (ex.: inventário, carnes, vendas/transferência), e recursos compartilhados.

- **venv/**:  
  Ambiente virtual Python configurado para o projeto.

- **run.py**:  
  Script principal para iniciar a execução dos testes e a verificação de atualizações, utilizando threads para rodar as funções em paralelo.

- **excel_handler.py, email_handler.py e creads.py**:  
  Scripts responsáveis pelo processamento dos arquivos Excel, consolidação dos dados e envio de e-mails.
  
- **.vscode/**:  
  Configurações específicas do Visual Studio Code para o ambiente do projeto.

## Pré-requisitos e Configuração

- **Python 3.x:** Certifique-se de que o Python e um ambiente virtual estejam configurados.
- **Robot Framework e SikuliLibrary:** Instale as dependências via pip.
- **Configuração do Ambiente:**  
  Atualize o arquivo `.env` com as credenciais de e-mail necessárias.
- **Dependências adicionais:**  
  Bibliotecas como `pandas`, `pyautogui`, `pywinauto`, `smtplib`, e `dotenv`.

## Como Executar?

1. Ative o ambiente virtual:
    ```shell
    cd c:\Users\YOUR_USER\YOUR_FOLDER\YOUR_WORKDIRECTORY
    venv\Scripts\activate
    ```
2. Execute o script principal:
    ```shell
    python run.py
    ```
3. Durante a execução, os testes serão executados e, após a extração, a consolidação e o envio dos relatórios ocorrerão automaticamente.

## Observações

- **Interrupção do Programa:**  
  A execução pode ser interrompida tanto via Ctrl+C (caso seja implementado um tratamento de sinal adequado) quanto pelo método atual que força o encerramento do Python.
- **Personalizações:**  
  As palavras-chave e parâmetros dos testes podem ser ajustados conforme necessário para diferentes bases de dados e configurações do sistema.

## Conclusão

Este projeto automatiza a rotina de extração e consolidação de relatórios na BMG Comercial, permitindo uma gestão mais eficiente dos dados. Ele integra diversas ferramentas e frameworks para oferecer uma solução robusta e automatizada para processos recorrentes de geração de relatórios.
