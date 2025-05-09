*** Settings ***
Library         SikuliLibrary
Library        ../../utils_handler.py
Library         ../keywords/keywords.py
Resource        ../keywords.robot
Resource        ../share.robot

*** Variables ***
*** Keywords ***
Select Menu Inventario de Industria
    # Clica em relatorios
    Wait Until Screen Contain    relatorios_icon.png    30
    Click    relatorios_icon.png
    # Clica em faturamento
    Wait Until Screen Contain    faturamento_icon.png    30
    Click    faturamento_icon.png
    # Clica em apuração
    Wait Until Screen Contain    apuracao_icon.png    30
    Click    apuracao_icon.png
    # Clica em inventario de industria
    Wait Until Screen Contain    inventario_industria_icon.png    30
    Click    inventario_industria_icon.png
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
    # Clica no icone do excel
    Procurar Icone    excel_opened.png    
    Wait Until Screen Contain    excel_opened.png    600
    Click    excel_opened.png
    Sleep    5s
    Save XLSX    ${nome_arquivo}
    Close FJ Frigo