"""
Detector de Coordenadas del Mouse
Herramienta útil para saber dónde hacer click en tus automatizaciones
"""

import pyautogui
import time

print("""
╔═══════════════════════════════════════════════════╗
║                                                   ║
║     DETECTOR DE COORDENADAS DEL MOUSE             ║
║                                                   ║
║  Esta herramienta te muestra en tiempo real:     ║
║  • Posición X, Y del mouse                       ║
║  • Color RGB del pixel bajo el cursor            ║
║                                                   ║
║  Úsala para encontrar las coordenadas exactas    ║
║  donde necesitas hacer click en tus scripts.     ║
║                                                   ║
╚═══════════════════════════════════════════════════╝

Instrucciones:
1. Mueve el mouse sobre el elemento que quieres
2. Anota las coordenadas X, Y que se muestran
3. Usa esas coordenadas en pyautogui.click(x, y)

Presiona Ctrl+C para detener
""")

input("Presiona Enter para comenzar...")

print("\n" + "=" * 60)
print("Coordenadas en tiempo real:")
print("=" * 60)

try:
    while True:
        # Obtener posición del mouse
        x, y = pyautogui.position()
        
        # Obtener color del pixel
        pixel_color = pyautogui.pixel(x, y)
        
        # Mostrar información (el \r sobrescribe la línea anterior)
        position_str = f"X: {x:5d} | Y: {y:5d}"
        color_str = f"RGB: ({pixel_color[0]:3d}, {pixel_color[1]:3d}, {pixel_color[2]:3d})"
        
        print(f"{position_str} | {color_str}", end='\r')
        
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n\n✅ Herramienta detenida")
    print("\nTip: Usa las coordenadas que anotaste en tu código:")
    print("     pyautogui.click(x, y)")
