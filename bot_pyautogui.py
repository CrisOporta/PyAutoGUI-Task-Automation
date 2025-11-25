"""
Bot de Automatización con PyAutoGUI
Este script demuestra diferentes funcionalidades de PyAutoGUI
"""

import pyautogui
import time
import os
from datetime import datetime

# Configuración de seguridad - mover el mouse a la esquina superior izquierda abortará el script
pyautogui.FAILSAFE = True
# Pausa entre comandos (en segundos)
pyautogui.PAUSE = 1


class AutomationBot:
    """Clase para manejar automatizaciones con PyAutoGUI"""
    
    def __init__(self):
        self.screen_width, self.screen_height = pyautogui.size()
        self.screenshots_folder = "screenshots"
        self._create_screenshots_folder()
    
    def _create_screenshots_folder(self):
        """Crea la carpeta para guardar screenshots si no existe"""
        if not os.path.exists(self.screenshots_folder):
            os.makedirs(self.screenshots_folder)
    
    def get_screen_info(self):
        """Obtiene información sobre la pantalla"""
        print("=" * 50)
        print("INFORMACIÓN DE LA PANTALLA")
        print("=" * 50)
        print(f"Resolución: {self.screen_width}x{self.screen_height}")
        x, y = pyautogui.position()
        print(f"Posición actual del mouse: X={x}, Y={y}")
        print("=" * 50)
    
    def demo_mouse_movement(self):
        """Demuestra el movimiento del mouse"""
        print("\n📍 DEMO: Movimiento del Mouse")
        print("El mouse se moverá en un patrón...")
        time.sleep(2)
        
        # Movimiento absoluto
        print("Moviendo a la esquina superior izquierda...")
        pyautogui.moveTo(100, 100, duration=1)
        
        print("Moviendo al centro de la pantalla...")
        pyautogui.moveTo(self.screen_width // 2, self.screen_height // 2, duration=1)
        
        # Movimiento relativo
        print("Moviendo 200px a la derecha...")
        pyautogui.move(200, 0, duration=0.5)
        
        print("Dibujando un cuadrado...")
        distance = 200
        pyautogui.move(0, distance, duration=0.5)  # abajo
        pyautogui.move(-distance, 0, duration=0.5)  # izquierda
        pyautogui.move(0, -distance, duration=0.5)  # arriba
        pyautogui.move(distance, 0, duration=0.5)  # derecha
        
        print("✅ Demo de movimiento completada\n")
    
    def demo_clicks(self):
        """Demuestra diferentes tipos de clicks"""
        print("\n🖱️  DEMO: Clicks del Mouse")
        print("Esperando 3 segundos para que posiciones una ventana...")
        time.sleep(3)
        
        x, y = pyautogui.position()
        print(f"Haciendo click en posición: ({x}, {y})")
        
        # Click simple
        pyautogui.click()
        time.sleep(0.5)
        
        # Doble click
        print("Haciendo doble click...")
        pyautogui.doubleClick()
        time.sleep(0.5)
        
        # Click derecho
        print("Haciendo click derecho...")
        pyautogui.rightClick()
        time.sleep(1)
        
        # Presionar ESC para cerrar menú contextual
        pyautogui.press('esc')
        
        print("✅ Demo de clicks completada\n")
    
    def demo_keyboard(self):
        """Demuestra el uso del teclado"""
        print("\n⌨️  DEMO: Escritura con Teclado")
        print("Esperando 3 segundos. Abre un bloc de notas o editor de texto...")
        time.sleep(3)
        
        # Escribir texto
        print("Escribiendo texto...")
        pyautogui.write("Hola! Este es un bot con PyAutoGUI", interval=0.1)
        pyautogui.press('enter')
        pyautogui.press('enter')
        
        # Atajos de teclado
        print("Escribiendo más texto con formato...")
        pyautogui.write("Este texto sera copiado y pegado", interval=0.1)
        
        # Seleccionar todo
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.5)
        
        # Copiar
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)
        
        # Ir al final y pegar
        pyautogui.press('end')
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'v')
        
        print("✅ Demo de teclado completada\n")
    
    def demo_screenshot(self):
        """Toma capturas de pantalla"""
        print("\n📸 DEMO: Captura de Pantalla")
        
        # Captura de pantalla completa
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.screenshots_folder}/screenshot_{timestamp}.png"
        
        print(f"Tomando captura de pantalla completa...")
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)
        print(f"✅ Captura guardada en: {filename}")
        
        # Captura de región específica
        print("Tomando captura de región central...")
        region_filename = f"{self.screenshots_folder}/region_{timestamp}.png"
        region = (
            self.screen_width // 4, 
            self.screen_height // 4,
            self.screen_width // 2, 
            self.screen_height // 2
        )
        screenshot = pyautogui.screenshot(region=region)
        screenshot.save(region_filename)
        print(f"✅ Captura de región guardada en: {region_filename}\n")
    
    def find_and_click(self, image_path, confidence=0.8):
        """
        Busca una imagen en la pantalla y hace click en ella
        
        Args:
            image_path: Ruta de la imagen a buscar
            confidence: Nivel de confianza (0.0 a 1.0)
        """
        print(f"\n🔍 Buscando imagen: {image_path}")
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=confidence)
            if location:
                # Obtener el centro de la imagen encontrada
                center = pyautogui.center(location)
                print(f"✅ Imagen encontrada en: {center}")
                pyautogui.click(center)
                return True
            else:
                print("❌ Imagen no encontrada")
                return False
        except Exception as e:
            print(f"❌ Error buscando imagen: {e}")
            return False
    
    def get_mouse_position_tool(self, duration=10):
        """
        Herramienta para obtener posiciones del mouse en tiempo real
        Útil para saber dónde hacer click
        """
        print("\n📍 HERRAMIENTA: Detector de Posición del Mouse")
        print(f"Moviendo el mouse para ver coordenadas (duración: {duration}s)")
        print("Presiona Ctrl+C para detener antes de tiempo")
        print("-" * 50)
        
        try:
            start_time = time.time()
            while time.time() - start_time < duration:
                x, y = pyautogui.position()
                pixel_color = pyautogui.pixel(x, y)
                print(f"X: {x:4d} Y: {y:4d} RGB: {pixel_color}", end='\r')
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("\n⚠️  Detenido por el usuario")
        
        print("\n✅ Herramienta finalizada\n")
    
    def demo_scroll(self):
        """Demuestra el uso del scroll"""
        print("\n🔄 DEMO: Scroll")
        print("Esperando 3 segundos. Abre una página web o documento largo...")
        time.sleep(3)
        
        print("Scrolling hacia abajo...")
        pyautogui.scroll(-3, pause=0.5)  # Negativo = abajo
        time.sleep(1)
        
        print("Scrolling hacia arriba...")
        pyautogui.scroll(3, pause=0.5)  # Positivo = arriba
        
        print("✅ Demo de scroll completada\n")
    
    def example_automation_task(self):
        """
        Ejemplo de tarea automatizada completa
        Este ejemplo abre el bloc de notas y escribe un mensaje
        """
        print("\n🤖 TAREA AUTOMATIZADA: Abrir Bloc de Notas y Escribir")
        print("=" * 50)
        
        # Abrir el menú de inicio
        print("Paso 1: Abriendo menú de inicio...")
        pyautogui.press('win')
        time.sleep(1)
        
        # Buscar bloc de notas
        print("Paso 2: Buscando 'notepad'...")
        pyautogui.write('notepad', interval=0.1)
        time.sleep(1)
        
        # Abrir bloc de notas
        print("Paso 3: Abriendo Bloc de Notas...")
        pyautogui.press('enter')
        time.sleep(2)
        
        # Escribir contenido
        print("Paso 4: Escribiendo contenido automatizado...")
        mensaje = f"""
╔════════════════════════════════════════╗
║   MENSAJE AUTOMATIZADO CON PYAUTOGUI  ║
╚════════════════════════════════════════╝

Fecha y hora: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Este mensaje fue escrito automáticamente por un bot.

Características del bot:
✓ Movimiento del mouse
✓ Clicks automáticos
✓ Escritura de texto
✓ Capturas de pantalla
✓ Detección de posiciones
✓ Y mucho más!

¡La automatización es genial! 🚀
"""
        pyautogui.write(mensaje, interval=0.02)
        
        print("✅ Tarea automatizada completada\n")
        print("⚠️  NOTA: El bloc de notas permanece abierto. Ciérralo manualmente.")


def main():
    """Función principal con menú interactivo"""
    bot = AutomationBot()
    
    while True:
        print("\n" + "=" * 50)
        print("🤖 BOT DE AUTOMATIZACIÓN CON PYAUTOGUI")
        print("=" * 50)
        print("\nSelecciona una opción:")
        print("1. Ver información de pantalla")
        print("2. Demo: Movimiento del mouse")
        print("3. Demo: Clicks")
        print("4. Demo: Teclado")
        print("5. Demo: Scroll")
        print("6. Demo: Captura de pantalla")
        print("7. Herramienta: Detector de posición del mouse")
        print("8. Tarea completa: Abrir Bloc de Notas")
        print("9. Salir")
        print("=" * 50)
        
        choice = input("\nIngresa tu elección (1-9): ").strip()
        
        if choice == '1':
            bot.get_screen_info()
        elif choice == '2':
            bot.demo_mouse_movement()
        elif choice == '3':
            bot.demo_clicks()
        elif choice == '4':
            bot.demo_keyboard()
        elif choice == '5':
            bot.demo_scroll()
        elif choice == '6':
            bot.demo_screenshot()
        elif choice == '7':
            duration = input("¿Cuántos segundos? (default 10): ").strip()
            duration = int(duration) if duration.isdigit() else 10
            bot.get_mouse_position_tool(duration)
        elif choice == '8':
            confirm = input("⚠️  Esto abrirá el Bloc de Notas. ¿Continuar? (s/n): ")
            if confirm.lower() == 's':
                bot.example_automation_task()
        elif choice == '9':
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print("\n❌ Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    print("""
    ╔════════════════════════════════════════════════╗
    ║                                                ║
    ║     BOT DE AUTOMATIZACIÓN CON PYAUTOGUI       ║
    ║                                                ║
    ║  ⚠️  IMPORTANTE: CONFIGURACIÓN DE SEGURIDAD     ║
    ║                                                ║
    ║  Para detener el bot en cualquier momento:    ║
    ║  → Mueve el mouse a la esquina superior       ║
    ║    izquierda de la pantalla                   ║
    ║                                                ║
    ╚════════════════════════════════════════════════╝
    """)
    
    input("Presiona Enter para comenzar...")
    
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa interrumpido por el usuario")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
