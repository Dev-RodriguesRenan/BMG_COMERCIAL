*** Settings ***
Library    SikuliLibrary
*** Keywords ***
Load Images
    Add Image Path    ${IMAGES_PATH}
*** Variables ***
${IMAGES_PATH}    ${EXECDIR}/images
${LOGIN}    julio.franca
${PASSWORD}    franca@2023.
@{BASES}    BMG Central
...    Central Nostrobeef
...    BMG VILA BELA
...    BMG FOUR FRIGO