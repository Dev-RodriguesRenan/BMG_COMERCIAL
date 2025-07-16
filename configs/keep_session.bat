@echo off
for /f "tokens=3" %%s in ('query session ^| findstr "rdp"') do (
    tscon %%s /dest:console
)
