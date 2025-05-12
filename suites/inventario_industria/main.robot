*** Settings ***
Resource        ../../keywords/inventario_industria/keywords.robot
Test Setup        Load Images
*** Variables ***
# ${base}    BMG VILA BELA
*** Test Cases ***
Inverntario de Industria
    FOR    ${base}    IN    @{BASES}
        TRY
            Log    Extraindo planilha da base: ${base}
            Login in FJ Frigo    ${base}
            Select Menu Inventario de Industria
            Fill Forms in Inventario de Industria
            Export XLSX in Inventario de Industria    ${base}
        EXCEPT    message
            Log    Erro ao executar o caso de teste em: ${base}
            Close Force
            CONTINUE
        END
    END