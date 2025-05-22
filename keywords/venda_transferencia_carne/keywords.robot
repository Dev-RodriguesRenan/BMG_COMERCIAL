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
    Sleep    3s
Fill Forms in Transferencia de Carne
    ${DATA_INICIAL}    Take Last Business Day
    Log    ${DATA_INICIAL} 
    ${DATA_FINAL}    Take Last Business Day
    Log    ${DATA_FINAL} 
    # Preenche o campo de data inicial
    With Keys Write Text    ${DATA_INICIAL}
    # Passa para o campo
    Sleep    1s
    # Preenche o campo de data final
    With Keys Write Text    ${DATA_FINAL}
    # Passa para o proximo campo
    FOR    ${counter}    IN RANGE    0    17    1
        Log    Press TAB ${counter}
        Press Special Key    TAB
    END
    # Preench o campo tipo faturamento com 114 e -1
    With Keys Write Text    114
    Press Enter
    With Keys Write Text    -1
    Press Enter
    # Passa para o proximo campo
    FOR    ${counter}    IN RANGE    0    1    1
        Log    Press TAB ${counter}
        Press Special Key    TAB
    END
    # Preench o campo filial
    With Keys Write Text    2
    Press Enter
    With Keys Write Text    -1
    Press Enter

Export XLSX in Transferencia de Carne
    [Arguments]    ${unit}
    ${nome_arquivo}  Get Name File Of Unit    VendaTransferencia    ${unit}
    # Clica no botao de exportar
    Wait Until Screen Contain    export_xls.png    30
    Click    export_xls.png
    # Verifica se é possivel gerar o arquivo
    ${exists_not_xlsx}    Exists    nao_foi_possivel.png    12
    ${exists_menu_error}    Exists    menu_error.png    12
    
    IF    ${exists_not_xlsx} == True
        Log    Não é possível gerar o arquivo XLSX
        # Clica no botão de ok
        Press Enter
        Log    Não é possível gerar o arquivo XLSX
        Close FJ Frigo
    ELSE IF    ${exists_menu_error} == True
        Log    Não é possível gerar o arquivo XLSX
        Close Force
    ELSE
        Log    É possível gerar o arquivo XLSX
        Log    Extraindo planilha da base: ${unit}
        # Clica no icone do excel
        Procurar Icone    excel_opened.png
        Wait Until Screen Contain    excel_opened.png    120
        Click    excel_opened.png
        Sleep    5s
        Save XLSX    ${nome_arquivo}
        Close FJ Frigo
    END

