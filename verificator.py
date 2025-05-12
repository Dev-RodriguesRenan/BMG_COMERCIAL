import time
import pyautogui
import pywinauto


def verify_exists_update():
    """Verifica se existe uma janela de atualização e, se existir e NÃO houver a janela 'Controle administrativo',
    ativa a janela e pressiona a tecla "enter"."""
    while True:
        print("Verificando se existe janela de atualização", end="\r")
        windows_list_activated = pywinauto.Desktop(backend="uia").windows()
        # Verifica se existe any janela com "Controle administrativo"
        has_controle_admin = any(
            "Controle administrativo" in window.window_text()
            for window in windows_list_activated
        )

        # Se não existir janela de Controle administrativo, procura janela de atualização
        if not has_controle_admin:
            for window in windows_list_activated:
                if "atualização" in window.window_text():
                    window.set_focus()
                    time.sleep(0.5)
                    pyautogui.press("enter")
                    print(
                        "Janela de atualização encontrada e tecla 'enter' pressionada"
                    )
        else:
            for window in windows_list_activated:
                if "atualização" in window.window_text():
                    window.set_focus()
                    time.sleep(0.5)
                    pyautogui.press("right")
                    time.sleep(0.5)
                    pyautogui.press("enter")
                    print(
                        "Janela de atualização encontrada e tecla 'right' e 'enter' pressionada para fechar o updater"
                    )
        time.sleep(10)


if __name__ == "__main__":
    verify_exists_update()
