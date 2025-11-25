"""
Ejemplo Simple de PyAutoGUI
Script básico para comenzar a usar PyAutoGUI
"""

import pyautogui
import time

# Configuración de seguridad
pyautogui.FAILSAFE = True

print("Bot de automatización simple")
print("=" * 50)

# Obtener tamaño de la pantalla
screen_width, screen_height = pyautogui.size()
print(f"Resolución de pantalla: {screen_width}x{screen_height}")

# Obtener posición actual del mouse
x, y = pyautogui.position()
print(f"Posición del mouse: X={x}, Y={y}")

print("\nEjemplo 1: Mover el mouse al centro de la pantalla")
time.sleep(2)
pyautogui.moveTo(screen_width // 2, screen_height // 2, duration=2)

print("\nEjemplo 2: Hacer un click")
time.sleep(1)
pyautogui.click()

print("\nEjemplo 3: Abrir el Bloc de Notas y escribir un mensaje")
input("Presiona Enter para continuar...")

# Abrir menú de inicio
pyautogui.press('win')
time.sleep(1)

# Buscar notepad
pyautogui.write('notepad')
time.sleep(1)

# Abrir
pyautogui.press('enter')
time.sleep(2)

# Escribir mensaje
pyautogui.write('Hola! Este mensaje fue escrito por un bot con PyAutoGUI', interval=0.1)

print("\n✅ Automatización completada!")
print("⚠️  El Bloc de Notas está abierto. Ciérralo manualmente.")
