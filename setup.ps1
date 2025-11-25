# Script de inicio para el Bot de PyAutoGUI
# Este script activa el entorno virtual e instala las dependencias

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   BOT DE AUTOMATIZACIÓN CON PYAUTOGUI" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar si existe el entorno virtual
if (!(Test-Path ".\venv\Scripts\activate.ps1")) {
    Write-Host "❌ Error: No se encontró el entorno virtual" -ForegroundColor Red
    Write-Host "Creando entorno virtual..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host "✅ Entorno virtual creado" -ForegroundColor Green
}

# Activar entorno virtual
Write-Host "🔄 Activando entorno virtual..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1

# Instalar dependencias
Write-Host "📦 Instalando dependencias..." -ForegroundColor Yellow
pip install -r requirements.txt

Write-Host ""
Write-Host "✅ ¡Todo listo!" -ForegroundColor Green
Write-Host ""
Write-Host "Ejecuta uno de estos comandos:" -ForegroundColor Cyan
Write-Host "  python bot_pyautogui.py          - Bot principal (recomendado)" -ForegroundColor White
Write-Host "  python ejemplo_simple.py         - Ejemplo simple" -ForegroundColor White
Write-Host "  python bot_navegador.py          - Automatización web" -ForegroundColor White
Write-Host "  python detector_coordenadas.py   - Detector de coordenadas" -ForegroundColor White
Write-Host ""
