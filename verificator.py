import time
import pyautogui
import pywinauto


def verify_exists_update():
    """Verifica se existe uma janela de atualização e, se existir e NÃO houver a janela 'Controle administrativo',
    ativa a janela e pressiona a tecla "enter"."""
    while True:
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
        time.sleep(10)
