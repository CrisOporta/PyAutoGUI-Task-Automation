"""
SIMPLE MACRO RECORDER
Versión simplificada del grabador de macros - Solo clicks y tiempos
"""

import pyautogui
import time
import json
from datetime import datetime
from pynput import mouse
from pynput.mouse import Button

pyautogui.FAILSAFE = True


class SimpleMacro:
    def __init__(self):
        self.clicks = []
        self.start_time = None
        self.recording = False
    
    def on_click(self, x, y, button, pressed):
        """Captura clicks del mouse"""
        if pressed and button == Button.left:
            elapsed = time.time() - self.start_time
            self.clicks.append({
                'x': x,
                'y': y,
                'time': round(elapsed, 2)
            })
            print(f"✓ Click #{len(self.clicks)} en ({x}, {y}) - Tiempo: {elapsed:.2f}s")
    
    def record(self, duration):
        """Graba clicks por un tiempo determinado"""
        print("\n" + "=" * 60)
        print(f"🔴 GRABANDO MACRO POR {duration} SEGUNDOS")
        print("=" * 60)
        print("Haz clicks en los lugares que quieres automatizar...")
        print("Los tiempos entre clicks se guardarán automáticamente\n")
        
        self.clicks = []
        self.start_time = time.time()
        self.recording = True
        
        with mouse.Listener(on_click=self.on_click) as listener:
            time.sleep(duration)
            listener.stop()
        
        self.recording = False
        
        print("\n" + "=" * 60)
        print(f"✅ Grabación completada: {len(self.clicks)} clicks")
        print("=" * 60)
    
    def save(self, filename):
        """Guarda la macro"""
        data = {
            'created': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'total_clicks': len(self.clicks),
            'clicks': self.clicks
        }
        
        with open(f"{filename}.json", 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"\n💾 Macro guardada: {filename}.json")
    
    def load(self, filename):
        """Carga una macro"""
        with open(f"{filename}.json", 'r') as f:
            data = json.load(f)
        
        self.clicks = data['clicks']
        print(f"\n📁 Macro cargada: {len(self.clicks)} clicks")
    
    def play(self, repetitions=1):
        """Reproduce la macro"""
        if not self.clicks:
            print("❌ No hay macro para reproducir")
            return
        
        print("\n" + "=" * 60)
        print(f"▶️  REPRODUCIENDO MACRO ({repetitions}x)")
        print("=" * 60)
        print("Iniciando en 3 segundos...\n")
        time.sleep(3)
        
        for rep in range(repetitions):
            if repetitions > 1:
                print(f"\n--- Repetición {rep + 1}/{repetitions} ---")
            
            last_time = 0
            for i, click in enumerate(self.clicks, 1):
                # Esperar el tiempo correspondiente
                wait = click['time'] - last_time
                if wait > 0:
                    time.sleep(wait)
                
                # Hacer click
                print(f"[{i}/{len(self.clicks)}] Click en ({click['x']}, {click['y']})")
                pyautogui.click(click['x'], click['y'])
                
                last_time = click['time']
            
            if rep < repetitions - 1:
                time.sleep(1)
        
        print("\n✅ Macro completada!")


def main():
    """Programa principal"""
    macro = SimpleMacro()
    
    print("""
    ╔═══════════════════════════════════════════════╗
    ║                                               ║
    ║        SIMPLE MACRO RECORDER                 ║
    ║     Grabador Simple de Macros de Clicks      ║
    ║                                               ║
    ╚═══════════════════════════════════════════════╝
    """)
    
    while True:
        print("\n" + "=" * 50)
        print("MENÚ")
        print("=" * 50)
        print("1. Grabar nueva macro")
        print("2. Cargar macro")
        print("3. Reproducir macro")
        print("4. Salir")
        print("=" * 50)
        
        choice = input("\nOpción: ").strip()
        
        if choice == '1':
            duration = input("¿Cuántos segundos grabar? (default 10): ").strip()
            duration = int(duration) if duration.isdigit() else 10
            
            macro.record(duration)
            
            save = input("\n¿Guardar macro? (s/n): ").strip().lower()
            if save == 's':
                name = input("Nombre del archivo: ").strip()
                if name:
                    macro.save(name)
        
        elif choice == '2':
            filename = input("Nombre del archivo: ").strip()
            try:
                macro.load(filename)
            except FileNotFoundError:
                print(f"❌ Archivo '{filename}.json' no encontrado")
            except Exception as e:
                print(f"❌ Error: {e}")
        
        elif choice == '3':
            reps = input("¿Cuántas veces reproducir? (default 1): ").strip()
            reps = int(reps) if reps.isdigit() else 1
            
            try:
                macro.play(repetitions=reps)
            except Exception as e:
                print(f"❌ Error: {e}")
        
        elif choice == '4':
            print("\n👋 ¡Hasta luego!")
            break
        
        else:
            print("❌ Opción inválida")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 ¡Hasta luego!")
