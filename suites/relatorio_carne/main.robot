*** Settings ***
Resource            ../../keywords/relatorio_carne/keywords.robot

Test Setup          Load Images
Test Teardown       Close Force


*** Variables ***
@{BASES}
...         BMG Central
...         Central Nostrobeef
# ...       BMG VILA BELA
...         BMG FOUR FRIGO


*** Test Cases ***
Relatorio de Carne
    FOR    ${base}    IN    @{BASES}
        TRY
            Log    \nExtraindo planilha RELATORIO DE CARNES da base: ${base}\n    level=DEBUG    console=True
            ${is_logged}    Login in FJ Frigo    ${base}
            IF    not ${is_logged}
                Log    \nErro ao logar o caso de teste em: ${base}\n    level=DEBUG    console=True
                Screenshot    Erro_Login_Relatorio_De_Carne_${base}
                Close Force
                CONTINUE
            END
            Select Menu Relatorio de Carne
            Fill Forms in Relatorio de Carne
            Export XLSX in Relatorio de Carne    ${base}
            Sleep    10s    Aguardando 10 segundos para o acessar novamente o sistema do FJ Frigo
        EXCEPT    AS    ${error}
            Log    \nErro ao executar o caso de teste em: ${base}\n    level=DEBUG    console=True
            Log    \nException: ${error}\n    level=DEBUG    console=True
            Screenshot    Erro_Relatorio_De_Carne_${base}
            Close Force
            Sleep    10s    Aguardando 10 segundos para o acessar novamente o sistema do FJ Frigo
            CONTINUE
        END
    END
