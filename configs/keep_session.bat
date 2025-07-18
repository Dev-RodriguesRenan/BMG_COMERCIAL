@echo off
:: Transfere a sessão RDP para o console
for /f "tokens=3" %%s in ('query session ^| findstr "rdp"') do (
    tscon %%s /dest:console
)

:: Desativa o screen saver e bloqueio de tela
reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v ScreenSaveActive /t REG_SZ /d 0 /f
reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v ScreenSaverIsSecure /t REG_SZ /d 0 /f
reg add "HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Control Panel\Desktop" /v ScreenSaverIsSecure /t REG_SZ /d 0 /f

:: Previne bloqueio automático da sessão
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Personalization" /v NoLockScreen /t REG_DWORD /d 1 /f

:: Configura timeout de sessão RDP para "never"
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services" /v MaxDisconnectionTime /t REG_DWORD /d 0 /f
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services" /v MaxIdleTime /t REG_DWORD /d 0 /f

echo Configurações de sessão aplicadas.