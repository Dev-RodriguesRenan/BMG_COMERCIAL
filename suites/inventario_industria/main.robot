*** Settings ***
Resource        ../../keywords/inventario_industria/keywords.robot
Test Setup        Load Images
Test Teardown    Close Force
*** Variables ***
# ${base}    BMG VILA BELA
*** Test Cases ***
Inverntario de Industria
    FOR    ${base}    IN    @{BASES}
        TRY
            Log    \nExtraindo planilha da base: ${base}\n    level=DEBUG    console=True
            Login in FJ Frigo    ${base}
            Select Menu Inventario de Industria
            Fill Forms in Inventario de Industria
            Export XLSX in Inventario de Industria    ${base}
            Sleep    10s    Aguardando 10 segundos para o acessar novamente o sistema do FJ Frigo
        EXCEPT    message
            Log    \nErro ao executar o caso de teste em: ${base}\n    level=DEBUG    console=True
            Close Force
            Sleep    10s    Aguardando 10 segundos para o acessar novamente o sistema do FJ Frigo
            CONTINUE
        END
    END