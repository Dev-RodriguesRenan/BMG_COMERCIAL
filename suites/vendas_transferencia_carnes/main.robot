*** Settings ***
Resource        ../keywords/venda_transferencia_carne/keywords.robot
Test Setup        Load Images
*** Variables ***
# ${base}    BMG VILA BELA
*** Test Cases ***
Vendas Transferencia de Carnes
    FOR    ${base}    IN    @{BASES}
        TRY
            Log    Extraindo planilha da base: ${base}
            Login in FJ Frigo    ${base}
            Select Menu Transferencia de Carne
            Fill Forms in Transferencia de Carne
            Export XLSX in Transferencia de Carne    ${base}
        EXCEPT    message
            Log    Erro ao executar o caso de teste em: ${base}
            Close Force
            CONTINUE
        END
    END
    