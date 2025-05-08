*** Settings ***
Resource        ../../keywords/relatorio_carne/keywords.robot
Test Setup        Load Images

*** Variables ***
${base}    BMG VILA BELA

*** Test Cases ***
Relatorio de Carne
    # FOR    ${base}    IN    @{BASES}
        Log    Extraindo planilha da base: ${base}
        Login in FJ Frigo    ${base}
        Select Menu Relatorio de Carne
        Fill Forms in Relatorio de Carne
        Export XLSX in Relatorio de Carne    ${base}
    # END