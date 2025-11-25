"""
Automatización de Búsqueda en el Navegador
Este script abre el navegador y realiza una búsqueda
"""

import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

print("🌐 Automatización de Búsqueda Web")
print("=" * 50)
print("Este script:")
print("1. Abrirá el navegador predeterminado")
print("2. Buscará en Google")
print("3. Escribirá una consulta")
print("\n⚠️  Asegúrate de tener un navegador configurado")
print("=" * 50)

input("\nPresiona Enter para comenzar...")

# Método 1: Usando atajo de teclado Windows + R y escribiendo la URL
print("\n1. Abriendo navegador...")
pyautogui.hotkey('win', 'r')
time.sleep(1)

pyautogui.write('https://www.google.com')
pyautogui.press('enter')

print("2. Esperando que cargue el navegador...")
time.sleep(5)  # Esperar que cargue

print("3. Buscando la barra de búsqueda...")
# Hacer click en el centro de la pantalla (donde suele estar la barra de búsqueda)
screen_width, screen_height = pyautogui.size()
pyautogui.click(screen_width // 2, screen_height // 2)

time.sleep(1)

print("4. Escribiendo consulta de búsqueda...")
consulta = "PyAutoGUI automation tutorial"
pyautogui.write(consulta, interval=0.1)

time.sleep(1)

print("5. Presionando Enter para buscar...")
pyautogui.press('enter')

print("\n✅ Búsqueda completada!")
print("⚠️  El navegador permanece abierto.")

time.sleep(3)

# Tomar captura de pantalla de los resultados
print("\n📸 Tomando captura de pantalla...")
screenshot = pyautogui.screenshot()
screenshot.save('resultados_busqueda.png')
print("✅ Captura guardada como 'resultados_busqueda.png'")
