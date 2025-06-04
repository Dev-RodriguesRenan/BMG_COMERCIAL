*** Settings ***
Resource    ../keywords/updater/keywords.robot
Test Setup    Load Images

*** Test Cases ***
Updater
    Open FJ Frigo
    Verify And Update FJ Frigo

