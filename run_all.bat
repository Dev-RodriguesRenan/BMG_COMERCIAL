@echo Iniciando execução dos testes Robot Framework
@echo ----------------------------------------------
start "" cmd /k "call C:\Users\PCVJ\Desktop\BMG_COMERCIAL\venv\Scripts\python -m robot -d results suites/inventario_industria/main.robot"
start "" cmd /k "call C:\Users\PCVJ\Desktop\BMG_COMERCIAL\venv\Scripts\python -m robot -d results suites/relatorio_carne/main.robot"
start "" cmd /k "call C:\Users\PCVJ\Desktop\BMG_COMERCIAL\venv\Scripts\python -m robot -d results suites/vendas_transferencia_carnes/main.robot"
@echo ----------------------------------------------
@echo Testes Robot Framework finalizados
@echo ----------------------------------------------
@echo Pressione qualquer tecla para sair...
PAUSE > NUL