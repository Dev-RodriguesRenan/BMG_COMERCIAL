*** Settings ***
Resource        ../keywords/venda_transferencia_carne/keywords.robot
Test Setup        Load Images
*** Variables ***
${base}    BMG Central
*** Test Cases ***
Vendas Transferencia de Carnes
    # FOR    ${base}    IN    @{BASES}
        Log    Extraindo planilha da base: ${base}
        Login in FJ Frigo    ${base}
        Select Menu Transferencia de Carne
        Fill Forms in Transferencia de Carne
        Export XLSX in Transferencia de Carne    ${base}
    # END
    