import os
import time
import pyautogui
import pywinauto
import datetime


def update_fj_frigo():
    """Atualiza o sistema FJ Frigo.

    Returns:
        bool: True se a atualização foi bem-sucedida, False caso contrário.
    """
    windows_list = pywinauto.Desktop(backend="uia").windows()
    for window in windows_list:
        if "atualização" in window.window_text().lower():
            print(
                f"{time.strftime('%X')} >>> Janela de atualização encontrada, iremos atualizar o sistema"
            )
            # Foca a janela de atualização
            window.set_focus()
            time.sleep(2.5)
            # Pressiona a tecla "enter" para confirmar a atualização
            pyautogui.press("enter")
            print(
                f"{time.strftime('%X')} >>> Janela de atualização encontrada e tecla 'enter' pressionada para atualizar o sistema"
            )
            time.sleep(15)
            # Verifica se a janela de login foi aberta
            for w in windows_list:
                if "login de usuário" in w.window_text().lower():
                    w.set_focus()
            return True
    print(f"{time.strftime('%X')} >>> Nenhuma janela de atualização encontrada.")
    return False


def verify_exists_update(duration_hours=2):
    """Verifica se existe uma janela de atualização e, se existir e NÃO houver a janela 'Controle administrativo',
    ativa a janela e pressiona a tecla "enter".
    Args:
        duration_hours (int, optional): Duração em horas para verificar a janela de atualização. Defaults to 2.
    """
    end_hours = datetime.datetime.now() + datetime.timedelta(hours=duration_hours)
    while datetime.datetime.now() < end_hours:
        print(">>> Verificando se existe janela de atualização", end="\r")
        windows_list_activated = pywinauto.Desktop(backend="uia").windows()
        # Verifica se existe any janela com "Controle administrativo"
        has_controle_admin = any(
            "Controle administrativo" in window.window_text()
            or "Login de usuário" in window.window_text()
            for window in windows_list_activated
        )
        print(
            f"{time.strftime('%X')} >>> Controle administrativo/Login de usuário {has_controle_admin}",
            end="\r",
        )
        # Se não existir janela de Controle administrativo, procura janela de atualização
        if not has_controle_admin:
            for window in windows_list_activated:
                if "atualização" in window.window_text():
                    print(
                        f"{time.strftime('%X')} >>> Janela de atualização encontrada, iremos atualizar o sistema"
                    )
                    window.set_focus()
                    time.sleep(0.5)
                    pyautogui.press("enter")
                    print(
                        f"{time.strftime('%X')} >>> Janela de atualização encontrada e tecla 'enter' pressionada para atualizar o sistema"
                    )
        else:
            for window in windows_list_activated:
                if "atualização" in window.window_text():
                    print(
                        f"{time.strftime('%X')} >>> Janela de atualização encontrada, iremos ignorar pois o sistema está em uso!!"
                    )
                    os.system("taskkill /f /im FJUpdaterLocal.exe")
                    print(f"{time.strftime('%X')} >>> Ignorada com sucesso!!")


if __name__ == "__main__":
    verify_exists_update()
