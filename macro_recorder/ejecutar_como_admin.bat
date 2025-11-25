@echo off
REM Script para ejecutar macro_recorder como Administrador
REM Esto es necesario para interactuar con apps de Microsoft Store (WhatsApp, etc.)

echo ========================================
echo   MACRO RECORDER - MODO ADMINISTRADOR
echo ========================================
echo.

REM Verificar si ya es administrador
net session >nul 2>&1
if %errorLevel% == 0 (
    echo ✅ Ejecutando como Administrador
    echo    Ahora podras interactuar con WhatsApp y apps protegidas.
    echo.
    
    REM Activar entorno virtual
    echo Activando entorno virtual...
    call ..\venv\Scripts\activate.bat
    
    REM Ejecutar el grabador unificado
    echo Ejecutando Macro Recorder...
    echo.
    python macro_recorder.py
    
    pause
) else (
    echo ⚠️  Solicitando permisos de Administrador...
    echo.
    
    REM Relanzar como administrador
    powershell -Command "Start-Process cmd -ArgumentList '/c cd /d %~dp0 && %~nx0' -Verb RunAs"
)
