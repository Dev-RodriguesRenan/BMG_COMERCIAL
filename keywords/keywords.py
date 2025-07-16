import os
import pyautogui
import pywinauto

pyautogui.FAILSAFE = False

def press_keys_simultaneously(k1, k2):
    pyautogui.hotkey(k1, k2)


def with_keys_write_text(text):
    pyautogui.write(text, interval=0.1)


def press_enter():
    pyautogui.press("enter")


def alt_f4():
    pyautogui.hotkey("alt", "f4")


def switch_window_fjFrigo():
    list_windows = pywinauto.Desktop(backend="uia").windows()
    for window in list_windows:
        if "Controle administrativo" in window.window_text():
            window.set_focus()
            break


def press_key(key):
    pyautogui.press(key)


def execute_kill():
    try:
        os.system("taskkill /F /IM EXCEL.EXE")
        os.system("taskkill /F /IM fjfrigo.exe")
    except Exception as e:
        print(f"Error: {e}")
        pass
