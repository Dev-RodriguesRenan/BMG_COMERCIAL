*** Settings ***
Library         SikuliLibrary
Library         ../keywords.py
Library         ../../verificator.py
Resource        ../share.robot

*** Keywords ***
Open FJ Frigo
    Press Key    win
    Sleep    3s

    With Keys Write Text    fjfrigo
    Sleep    5s
    Press Enter
Verify And Update FJ Frigo
    Wait Until Screen Contain    fj_banner.png    30
    Sleep    15s    Aguarda para caso apareça a tela de update
    # Verifica se a tela de update está presente
    ${update}    Update Fj Frigo
    IF    ${update} == True
        Log    \nFJFRIGO ATUALIZADO...\n    level=DEBUG    console=True
    ELSE
        Log    \nFJFRIGO NÃO FOI ATUALIZADO...\n    level=DEBUG    console=True
        Alt F4
    END
