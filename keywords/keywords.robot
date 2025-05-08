*** Settings ***
Library         SikuliLibrary
Library         keywords.py
Resource        keywords.robot
Resource        share.robot

*** Keywords ***
# Acessa o sistema da FJ Frigo 
Login in FJ Frigo
    [Arguments]    ${base}
    Press Key    win
    Sleep    2s
    With Keys Write Text    fjfrigo
    Sleep    2s 
    Press Enter
    Wait Until Screen Contain    fj_banner.png    60
    # Seleciona a base da FJ Frigo
    Select Base in FJ Frigo    ${base}
    Sleep    3s
    # Preenche o login e senha
    Fill Credentials in FJ Frigo 
Select Base in FJ Frigo
    [Arguments]    ${base}
    Click    banco_de_dados.png    91    08
    Sleep    2s   
    IF    '${base}' == 'BMG Central'
        Select Primary Option
        Select Option   1
    ELSE IF    '${base}' == 'Central Nostrobeef'
        Select Primary Option
        Select Option    3
    ELSE IF    '${base}' == 'BMG FOUR FRIGO'
        Select Primary Option
        Select Option    7
    ELSE IF    '${base}' == 'BMG VILA BELA'
        Select Primary Option
        Select Option    6
    ELSE
       Log    Escolhendo a base default: BMG Central
    END
    Press Enter
    Press Special Key    TAB
Fill Credentials in FJ Frigo
    Press Special Key    TAB
    # verifica se o login e senha estão preenchidos
    ${is_loged}=    Exists    login.png    5
    IF    '${is_loged}' == 'False'
        With Keys Write Text    ${LOGIN}
        Log    Preechendo login do usuario: ${LOGIN}
    END
    Press Special Key    TAB
    ${is_loged}=    Exists    password.png    5
    IF    '${is_loged}' == 'False'
        Log    Preechendo senha do usuario: ${PASSWORD}
        With Keys Write Text    ${PASSWORD}
    END
    Press Enter
    Press Enter
# Salva o arquivo XLSX
Save XLSX
    [Arguments]    ${nome_arquivo}
    # Verifica se o excel abriu
    Wait Until Screen Contain    excel_is_opened.png    120
    # Atalho para salvar o arquivo
    Press Keys Simultaneously    ctrl    b
    # Salvar na pasta documents
    Wait Until Screen Contain    procurar_icon.png    30
    Click    procurar_icon.png
    Wait Until Screen Contain    excel_is_save.png    120
    With Keys Write Text    ${nome_arquivo}
    Sleep    2s
    Press Enter
    Wait Until Screen Contain    excel_is_opened.png    10
    Alt F4

# Fecha o sistema da FJ Frigo
Close FJ Frigo
    Switch Window FjFrigo 
    Sleep    5s
    Alt F4
# Seleciona a primeira opção de base
Select Primary Option
    FOR    ${counter}    IN RANGE    0    6    1
        Log    ${counter}
        Press Key    up
    END
# Seleciona a opção desejada
Select Option
    [Arguments]    ${option}
    FOR    ${counter}    IN RANGE    0    ${option}    1
        Log    ${counter}
        Sleep    0.5s
        Press Key    down
    END
# Procura o icone até que o mesmo seja encontrado
Procurar Icone
    [Arguments]    ${icon}
    ${isCancel}    Exists    ${icon}.png    10
    WHILE    ${isCancel} == 'True'
        ${isCancel}    Exists    ${icon}.png    10
        IF    ${isCancel} == 'False'
            Log    ${icon} encontrado
            BREAK
        END
        Log    ${icon} não encontrado
    END