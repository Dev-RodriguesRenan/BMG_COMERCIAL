*** Settings ***
Resource        ../keywords/venda_transferencia_carne/keywords.robot
Test Setup        Load Images
Test Teardown    Close Force
*** Variables ***
@{BASES}    
...    BMG Central
...    Central Nostrobeef
# ...    BMG VILA BELA
...    BMG FOUR FRIGO
*** Test Cases ***
Vendas Transferencia de Carnes
    FOR    ${base}    IN    @{BASES}
        TRY
            Log    \nExtraindo planilha VENDAS/TRANSFERENCIA da base: ${base}\n    level=DEBUG    console=True
            Login in FJ Frigo    ${base}
            Select Menu Transferencia de Carne
            Fill Forms in Transferencia de Carne
            Export XLSX in Transferencia de Carne    ${base}
            Sleep    10s    Aguardando 10 segundos para o acessar novamente o sistema do FJ Frigo
        EXCEPT     AS     ${error}
            Log    \nErro ao executar o caso de teste em: ${base}\n    level=DEBUG    console=True
            Log    \nException: ${error}\n    level=DEBUG    console=True
            Screenshot    Erro_Transferencia_Carne_${base}
            Close Force
            Sleep    10s    Aguardando 10 segundos para o acessar novamente o sistema do FJ Frigo
            CONTINUE
        END
    END
    