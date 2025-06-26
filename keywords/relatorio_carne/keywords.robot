*** Settings ***
Library         SikuliLibrary
Library         ../keywords.py
Library         ../../utils_handler.py
Resource        ../keywords.robot
Resource        ../share.robot

*** Variables ***
*** Keywords ***
Select Menu Relatorio de Carne
    # Clica em relatorios
    Wait Until Screen Contain    relatorios_icon.png    30
    Click    relatorios_icon.png
    # Clica em faturamento
    Wait Until Screen Contain    faturamento_icon.png    30
    Click    faturamento_icon.png
    # Clica em apuração
    Wait Until Screen Contain    compras_entradas.png    30
    Click    compras_entradas.png
    # Clica em inventario de industria
    Wait Until Screen Contain    compras_carnes.png    30
    Click    compras_carnes.png
    Sleep    3s
Fill Forms in Relatorio de Carne
    # Preenche o campo com a data do dia primeiro deste mês
    ${DATA_INICIAL}    Get First Day Of Month
    Log    ${DATA_INICIAL}    console=True
    ${DATA_FINAL}    Take Last Business Day
    Log    ${DATA_FINAL}    console=True
    # Preenche o campo de data inicial
    With Keys Write Text    ${DATA_INICIAL}
    # Preenche o campo de data final
    With Keys Write Text    ${DATA_FINAL}
    # Passa para o proximo campo, tipo faturamento, e preenche com 1113 e -1 (12 tabs)
    FOR    ${counter}    IN RANGE    0    12    1
        Log    ${counter}    
        Press Special Key    TAB
    END
    With Keys Write Text    1113    
    Press Enter
    With Keys Write Text    -1
    Press Enter
    # Passa para o proximo campo, filial, e preenche com -1 (1 tabs)
    FOR    ${counter}    IN RANGE    0    1    1
        Log    ${counter}    
        Press Special Key    TAB
    END
    # Digita -1 com input text
    Input Text     ${EMPTY}     -1
    Press Enter
Export XLSX in Relatorio de Carne
    [Arguments]    ${unit}
    ${nome_arquivo}  Get Name File Of Unit    Carne    ${unit}
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
        Wait Until Screen Contain    excel_opened.png    120
        Click    excel_opened.png
        Sleep    5s
        Save XLSX    ${nome_arquivo}
        Close FJ Frigo
    END