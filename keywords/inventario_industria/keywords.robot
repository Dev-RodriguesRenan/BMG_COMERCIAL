*** Settings ***
Library         SikuliLibrary
Library        ../../utils_handler.py
Library         ../keywords/keywords.py
Resource        ../keywords.robot

*** Variables ***
*** Keywords ***
Select Menu Inventario de Industria
    Wait Until Screen Contain    relatorios_icon.png   10
    Key Down    ALT 
    # Clica em relatorios
    Press Key    3
    Sleep    1
    # Clica em faturamento
    Press Key    2
    Sleep    1
    # Clica em apuração
    Press Key   3
    Sleep    1
    # Clica em inventario de industria
    Press Key    3
    Sleep    1
    Key Up    ALT
    Sleep    3s

Fill Forms in Inventario de Industria
    # Preenche o campo de data atual
    ${DATA_ATUAL}    Get Datetime Now 
    With Keys Write Text    ${DATA_ATUAL}
    Sleep    1s
    # Preenche o campo de filial com -1
    With Keys Write Text    -1
    Press Enter
    # Seleciona o campo separado por vencimento
    Wait Until Screen Contain    separado_por_vencimento.png    30
    Click    separado_por_vencimento.png    
    
Export XLSX in Inventario de Industria
    [Arguments]    ${unit}
    ${nome_arquivo}  Get Name File Of Unit    Inventario    ${unit}    
    # Clica no botao de exportar
    Wait Until Screen Contain    export_xls.png    30
    Click    export_xls.png
    # Verifica se é possivel gerar o arquivo
    ${exists_not_xlsx}    Exists    nao_foi_possivel.png    12
    ${exists_menu_error}    Exists    menu_error.png    12
    
    IF    ${exists_not_xlsx} == True
        Log    Não é possível gerar o arquivo XLSX    console=True
        # Clica no botão de ok
        Press Enter
        Log    Não é possível gerar o arquivo XLSX    console=True
        Close FJ Frigo
    ELSE IF    ${exists_menu_error} == True
        Log    Não é possível gerar o arquivo XLSX    console=True
        Close Force
    ELSE
        Log    É possível gerar o arquivo XLSX    console=True
        Log    Extraindo planilha da base: ${unit}    console=True
        # Clica no icone do excel
        Procurar Icone    excel_opened    
        Wait Until Screen Contain    excel_opened.png    600
        Click    excel_opened.png
        Sleep    5s
        Save XLSX    ${nome_arquivo}
        Close FJ Frigo
    END