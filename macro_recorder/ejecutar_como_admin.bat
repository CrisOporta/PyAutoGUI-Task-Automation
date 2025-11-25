@echo off
REM Script para ejecutar macro_recorder_v2 como Administrador

echo ========================================
echo   MACRO RECORDER V2 - CON TECLA WIN
echo ========================================
echo.

REM Verificar si ya es administrador
net session >nul 2>&1
if %errorLevel% == 0 (
    echo ✅ Ejecutando como Administrador
    echo.
    
    REM Activar entorno virtual
    echo Activando entorno virtual...
    call ..\venv\Scripts\activate.bat
    
    REM Ejecutar V2
    echo Ejecutando Macro Recorder V2...
    echo.
    python macro_recorder_v2.py
    
    pause
) else (
    echo ⚠️  Este script necesita permisos de Administrador
    echo     para capturar la tecla Windows
    echo.
    echo Relanzando con permisos...
    echo.
    
    REM Relanzar como administrador
    powershell -Command "Start-Process cmd -ArgumentList '/c cd /d %~dp0 && %~nx0' -Verb RunAs"
)
