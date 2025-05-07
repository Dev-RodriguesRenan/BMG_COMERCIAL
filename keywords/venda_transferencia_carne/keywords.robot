*** Settings ***
Library         SikuliLibrary
Library         ../keywords.py
Resource    ../keywords.robot
Library         ../../utils_handler.py
*** Keywords ***
Select Menu Transferencia de Carne
    # Clica em relatorios
    Wait Until Screen Contain    relatorios_icon.png    30
    Click    relatorios_icon.png
    # Clica em faturamento
    Wait Until Screen Contain    faturamento_icon.png    30
    Click    faturamento_icon.png
    # Clica em vendas
    Wait Until Screen Contain    vendas_icon.png    30
    Click    vendas_icon.png
    # Clica em venda transferencia de carne
    Wait Until Screen Contain    vtdc_icon.png    30
    Click    vtdc_icon.png
    
Fill Forms in Transferencia de Carne
    ${DATA_INICIAL}    Take Last Business Day 
    ${DATA_FINAL}    Take Last Business Day
    # Preenche o campo de data inicial
    With Keys Write Text    ${DATA_INICIAL}
    # Passa para o campo
    Press Special Key    TAB
    # Preenche o campo de data final
    With Keys Write Text    ${DATA_FINAL}
    # Passa para o proximo campo
    FOR    ${counter}    IN RANGE    0    16    1
        Log    Press TAB ${counter}
        Press Special Key    TAB
    END
    # Preench o campo tipo faturamento com 114 e -1
    With Keys Write Text    114
    Press Enter
    With Keys Write Text    -1
    Press Enter
    # Passa para o proximo campo
    FOR    ${counter}    IN RANGE    0    3    1
        Log    Press TAB ${counter}
        Press Special Key    TAB
    END
    # Preench o campo filial
    With Keys Write Text    2
    Press Enter
    With Keys Write Text    -1
    Press Enter

Export XLSX in Transferencia de Carne
    # Clica no botao de exportar
    Wait Until Screen Contain    export_xls.png    30
    Click    export_xls.png
    # Clica no botao de ok
    Wait Until Screen Contain    excel_opened.png    120
    Click    excel_opened.png
    Sleep    5s
    Save XLSX    $nome_arquivo
    Close FJ Frigo

