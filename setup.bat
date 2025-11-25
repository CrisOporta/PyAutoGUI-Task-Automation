@echo off
REM Script de inicio para el Bot de PyAutoGUI (Windows CMD)

echo ========================================
echo    BOT DE AUTOMATIZACION CON PYAUTOGUI
echo ========================================
echo.

REM Activar entorno virtual
echo Activando entorno virtual...
call .\venv\Scripts\activate.bat

REM Instalar dependencias
echo Instalando dependencias...
pip install -r requirements.txt

echo.
echo ========================================
echo LISTO! Ejecuta uno de estos comandos:
echo ========================================
echo   python bot_pyautogui.py          - Bot principal (recomendado)
echo   python ejemplo_simple.py         - Ejemplo simple
echo   python bot_navegador.py          - Automatizacion web
echo   python detector_coordenadas.py   - Detector de coordenadas
echo.
