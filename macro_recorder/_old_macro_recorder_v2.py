"""
MACRO RECORDER V2 - Con soporte completo para tecla Windows
Usa keyboard library para captura total de teclas
"""

import pyautogui
import time
import json
import os
import keyboard  # Mejor para capturar Windows key
from datetime import datetime
from pynput import mouse
from pynput.mouse import Button

# Configuración
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1


class MacroRecorderV2:
    """Grabador de macros mejorado con captura completa de teclas"""
    
    def __init__(self):
        self.recording = False
        self.actions = []
        self.start_time = None
        self.last_action_time = None
        self.macros_folder = "macros"
        self._create_macros_folder()
        
        # Mouse listener
        self.mouse_listener = None
        
        # Eventos de teclado grabados (para evitar duplicados)
        self.last_keyboard_event_time = 0
    
    def _create_macros_folder(self):
        """Crea la carpeta de macros si no existe"""
        if not os.path.exists(self.macros_folder):
            os.makedirs(self.macros_folder)
    
    def _get_elapsed_time(self):
        """Obtiene el tiempo transcurrido desde la última acción"""
        if self.last_action_time is None:
            elapsed = 0
        else:
            elapsed = time.time() - self.last_action_time
        
        self.last_action_time = time.time()
        return round(elapsed, 3)
    
    def _add_action(self, action_type, **kwargs):
        """Añade una acción a la lista de acciones"""
        if not self.recording:
            return
        
        wait_time = self._get_elapsed_time()
        
        action = {
            'type': action_type,
            'wait_before': wait_time,
            'timestamp': datetime.now().strftime("%H:%M:%S.%f")[:-3],
            **kwargs
        }
        
        self.actions.append(action)
        self._print_action(action)
    
    def _print_action(self, action):
        """Imprime la acción grabada"""
        action_str = f"[{action['timestamp']}] "
        
        if action['type'] == 'click':
            action_str += f"CLICK {action['button']} en ({action['x']}, {action['y']})"
        elif action['type'] == 'scroll':
            direction = "ARRIBA" if action['dy'] > 0 else "ABAJO"
            action_str += f"SCROLL {direction} ({abs(action['dy'])} unidades)"
        elif action['type'] == 'hotkey':
            action_str += f"COMBINACIÓN: {' + '.join(action['keys'])}"
        elif action['type'] == 'key_press':
            action_str += f"TECLA: {action['key']}"
        
        if action['wait_before'] > 0:
            action_str += f" [espera: {action['wait_before']}s]"
        
        print(action_str)
    
    def on_click(self, x, y, button, pressed):
        """Callback para clicks del mouse"""
        if pressed:
            button_name = 'left' if button == Button.left else 'right' if button == Button.right else 'middle'
            self._add_action('click', x=x, y=y, button=button_name)
    
    def on_scroll(self, x, y, dx, dy):
        """Callback para scroll del mouse"""
        self._add_action('scroll', x=x, y=y, dx=dx, dy=dy)
    
    def _keyboard_callback(self, event):
        """Callback para eventos de teclado usando keyboard library"""
        if not self.recording:
            return
        
        # Solo procesar eventos 'down' (presionado)
        if event.event_type != 'down':
            return
        
        # Evitar duplicados (keyboard a veces genera eventos múltiples)
        current_time = time.time()
        if current_time - self.last_keyboard_event_time < 0.05:  # 50ms debounce
            return
        self.last_keyboard_event_time = current_time
        
        # Detectar ESC para detener
        if event.name == 'esc':
            print("\n\n⏹️  ESC detectado - Deteniendo grabación...")
            self.recording = False
            return
        
        # Detectar combinaciones
        modifiers = []
        if keyboard.is_pressed('ctrl'):
            modifiers.append('ctrl')
        if keyboard.is_pressed('alt'):
            modifiers.append('alt')
        if keyboard.is_pressed('shift'):
            modifiers.append('shift')
        if keyboard.is_pressed('windows') or keyboard.is_pressed('left windows') or keyboard.is_pressed('right windows'):
            modifiers.append('win')
        
        # Mapear nombres de teclas
        key_name = event.name
        
        # Normalizar nombres de teclas especiales
        key_map = {
            'left windows': 'win',
            'right windows': 'win',
            'windows': 'win',
            'left ctrl': 'ctrl',
            'right ctrl': 'ctrl',
            'left alt': 'alt',
            'right alt': 'alt',
            'left shift': 'shift',
            'right shift': 'shift',
            'enter': 'enter',
            'return': 'enter',
            'space': 'space',
            'tab': 'tab',
            'backspace': 'backspace',
            'delete': 'delete',
            'up': 'up',
            'down': 'down',
            'left': 'left',
            'right': 'right'
        }
        
        key_name = key_map.get(key_name, key_name)
        
        # No grabar modificadores solos
        if key_name in ['ctrl', 'alt', 'shift', 'win']:
            return
        
        # Si hay modificadores, es una combinación
        if modifiers:
            # Remover el modificador si aparece en la tecla presionada
            if key_name in modifiers:
                return
            
            keys_combo = modifiers + [key_name]
            self._add_action('hotkey', keys=keys_combo)
        else:
            # Tecla simple
            self._add_action('key_press', key=key_name)
    
    def start_recording(self):
        """Inicia la grabación de la macro"""
        print("\n" + "=" * 70)
        print("🔴 GRABACIÓN INICIADA (VERSIÓN MEJORADA)")
        print("=" * 70)
        print("\nInstrucciones:")
        print("  • Realiza los clicks y acciones que quieres automatizar")
        print("  • ✅ CAPTURA TECLA WINDOWS (Win)")
        print("  • ✅ Captura TODAS las combinaciones (Ctrl+X, Win+R, etc.)")
        print("  • Los tiempos entre acciones se guardarán automáticamente")
        print("  • Presiona ESC para detener la grabación")
        print("\n" + "=" * 70)
        print("\nAcciones grabadas:\n")
        
        self.recording = True
        self.actions = []
        self.start_time = time.time()
        self.last_action_time = time.time()
        self.last_keyboard_event_time = 0
        
        # Iniciar listener de mouse
        self.mouse_listener = mouse.Listener(
            on_click=self.on_click,
            on_scroll=self.on_scroll
        )
        self.mouse_listener.start()
        
        # Hook de teclado usando keyboard library
        keyboard.hook(self._keyboard_callback)
        
        # Esperar hasta que recording sea False
        try:
            while self.recording:
                time.sleep(0.1)
        except KeyboardInterrupt:
            pass
        
        # Detener listeners
        keyboard.unhook_all()
        if self.mouse_listener:
            self.mouse_listener.stop()
    
    def stop_recording(self):
        """Detiene la grabación"""
        self.recording = False
        keyboard.unhook_all()
        
        if self.mouse_listener:
            self.mouse_listener.stop()
        
        total_time = time.time() - self.start_time if self.start_time else 0
        
        print("\n" + "=" * 70)
        print("⏹️  GRABACIÓN DETENIDA")
        print("=" * 70)
        print(f"\nTotal de acciones grabadas: {len(self.actions)}")
        print(f"Tiempo total de grabación: {total_time:.2f}s")
        print("=" * 70)
    
    def save_macro(self, name):
        """Guarda la macro en un archivo JSON"""
        if not self.actions:
            print("❌ No hay acciones para guardar")
            return False
        
        filename = os.path.join(self.macros_folder, f"{name}.json")
        
        macro_data = {
            'name': name,
            'created': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'total_actions': len(self.actions),
            'actions': self.actions
        }
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(macro_data, f, indent=2, ensure_ascii=False)
            
            print(f"\n✅ Macro guardada exitosamente: {filename}")
            print(f"   Total de acciones: {len(self.actions)}")
            return True
        
        except Exception as e:
            print(f"\n❌ Error guardando macro: {e}")
            return False
    
    def load_macro(self, name):
        """Carga una macro desde un archivo"""
        filename = os.path.join(self.macros_folder, f"{name}.json")
        
        if not os.path.exists(filename):
            print(f"❌ Macro no encontrada: {filename}")
            return False
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                macro_data = json.load(f)
            
            self.actions = macro_data['actions']
            print(f"\n✅ Macro cargada: {name}")
            print(f"   Creada: {macro_data['created']}")
            print(f"   Total de acciones: {macro_data['total_actions']}")
            return True
        
        except Exception as e:
            print(f"\n❌ Error cargando macro: {e}")
            return False
    
    def list_macros(self):
        """Lista todas las macros guardadas"""
        if not os.path.exists(self.macros_folder):
            print("❌ No hay macros guardadas")
            return []
        
        macros = [f[:-5] for f in os.listdir(self.macros_folder) if f.endswith('.json')]
        
        if not macros:
            print("❌ No hay macros guardadas")
            return []
        
        print("\n" + "=" * 70)
        print("📋 MACROS GUARDADAS")
        print("=" * 70)
        
        for i, macro_name in enumerate(macros, 1):
            filename = os.path.join(self.macros_folder, f"{macro_name}.json")
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                print(f"{i}. {macro_name}")
                print(f"   Creada: {data['created']}")
                print(f"   Acciones: {data['total_actions']}")
                print()
            except:
                print(f"{i}. {macro_name} (error al leer)")
        
        print("=" * 70)
        return macros
    
    def play_macro(self, repetitions=1, speed=1.0):
        """Reproduce la macro cargada"""
        if not self.actions:
            print("❌ No hay macro cargada para reproducir")
            return
        
        print("\n" + "=" * 70)
        print(f"▶️  REPRODUCIENDO MACRO ({repetitions} {'vez' if repetitions == 1 else 'veces'})")
        print("=" * 70)
        print(f"Velocidad: {speed}x")
        print(f"Total de acciones: {len(self.actions)}")
        print("\n⚠️  La reproducción comenzará en 3 segundos...")
        print("    Mueve el mouse a la esquina superior izquierda para abortar")
        print("=" * 70)
        
        time.sleep(3)
        
        try:
            for rep in range(repetitions):
                if repetitions > 1:
                    print(f"\n--- Repetición {rep + 1}/{repetitions} ---")
                
                for i, action in enumerate(self.actions, 1):
                    # Esperar antes de ejecutar
                    wait_time = action['wait_before'] / speed
                    if wait_time > 0:
                        time.sleep(wait_time)
                    
                    # Ejecutar acción
                    action_type = action['type']
                    
                    if action_type == 'click':
                        print(f"[{i}/{len(self.actions)}] Click {action['button']} en ({action['x']}, {action['y']})")
                        
                        if action['button'] == 'left':
                            pyautogui.click(action['x'], action['y'])
                        elif action['button'] == 'right':
                            pyautogui.rightClick(action['x'], action['y'])
                        elif action['button'] == 'middle':
                            pyautogui.middleClick(action['x'], action['y'])
                    
                    elif action_type == 'scroll':
                        print(f"[{i}/{len(self.actions)}] Scroll")
                        pyautogui.scroll(action['dy'])
                    
                    elif action_type == 'hotkey':
                        # Reproducir combinaciones de teclas
                        keys = action['keys']
                        print(f"[{i}/{len(self.actions)}] Combinación: {' + '.join(keys)}")
                        try:
                            # Usar keyboard library para reproducir (mejor soporte Win)
                            keyboard.press_and_release('+'.join(keys))
                            time.sleep(0.1)  # Pequeña pausa después de hotkey
                        except Exception as e:
                            print(f"    ⚠️  Error ejecutando combinación: {e}")
                            # Fallback a pyautogui
                            try:
                                mapped_keys = ['winleft' if k == 'win' else k for k in keys]
                                pyautogui.hotkey(*mapped_keys)
                            except:
                                pass
                    
                    elif action_type == 'key_press':
                        key = action['key']
                        print(f"[{i}/{len(self.actions)}] Tecla: {key}")
                        try:
                            keyboard.press_and_release(key)
                        except Exception as e:
                            # Fallback a pyautogui
                            try:
                                if key == 'win':
                                    pyautogui.press('winleft')
                                else:
                                    pyautogui.press(key)
                            except:
                                print(f"    ⚠️  No se pudo ejecutar tecla: {key}")
                
                if rep < repetitions - 1:
                    time.sleep(1)
            
            print("\n" + "=" * 70)
            print("✅ MACRO COMPLETADA")
            print("=" * 70)
        
        except pyautogui.FailSafeException:
            print("\n\n⚠️  MACRO ABORTADA - FailSafe activado")
        except Exception as e:
            print(f"\n\n❌ Error durante la reproducción: {e}")
    
    def show_macro_details(self):
        """Muestra los detalles de la macro actual"""
        if not self.actions:
            print("❌ No hay macro cargada")
            return
        
        print("\n" + "=" * 70)
        print("📄 DETALLES DE LA MACRO")
        print("=" * 70)
        print(f"Total de acciones: {len(self.actions)}\n")
        
        for i, action in enumerate(self.actions, 1):
            self._print_action(action)
        
        print("\n" + "=" * 70)


def main():
    """Función principal con menú interactivo"""
    recorder = MacroRecorderV2()
    
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║      MACRO RECORDER V2 - CON TECLA WINDOWS ✅            ║
    ║                                                           ║
    ║    Graba y reproduce secuencias de clicks y acciones     ║
    ║         CAPTURA COMPLETA INCLUYENDO TECLA WIN            ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    
    ⚠️  IMPORTANTE: Ejecuta como Administrador para mejor captura
    """)
    
    while True:
        print("\n" + "=" * 70)
        print("MENÚ PRINCIPAL")
        print("=" * 70)
        print("1. 🔴 Grabar nueva macro (✅ Captura Win)")
        print("2. ⚙️  Cargar macro (para editar/ver)")
        print("3. ▶️  Reproducir macro (elige y ejecuta)")
        print("4. 📋 Ver macros guardadas")
        print("5. 📄 Ver detalles de macro cargada")
        print("6. 💾 Guardar macro actual")
        print("7. 🗑️  Eliminar macro")
        print("8. ❌ Salir")
        print("=" * 70)
        
        choice = input("\nSelecciona una opción (1-8): ").strip()
        
        try:
            if choice == '1':
                # Grabar nueva macro
                print("\n⚠️  La grabación comenzará cuando presiones Enter")
                print("    Presiona ESC para detener la grabación")
                input("\nPresiona Enter para comenzar...")
                
                recorder.start_recording()
                recorder.stop_recording()
                
                # Preguntar si quiere guardar
                save = input("\n¿Guardar esta macro? (s/n): ").strip().lower()
                if save == 's':
                    name = input("Nombre de la macro: ").strip()
                    if name:
                        recorder.save_macro(name)
            
            elif choice == '2':
                # Cargar macro
                macros = recorder.list_macros()
                if macros:
                    name = input("\nNombre de la macro a cargar: ").strip()
                    recorder.load_macro(name)
            
            elif choice == '3':
                # Reproducir macro MEJORADO - muestra lista y permite elegir
                macros = recorder.list_macros()
                
                if not macros:
                    continue
                
                # Permitir elegir macro
                name = input("\n¿Qué macro quieres reproducir? Nombre: ").strip()
                
                if name not in macros:
                    print(f"❌ Macro '{name}' no encontrada")
                    continue
                
                # Cargar la macro
                if not recorder.load_macro(name):
                    continue
                
                # Preguntar parámetros
                reps = input("\n¿Cuántas veces reproducir? (default 1): ").strip()
                reps = int(reps) if reps.isdigit() else 1
                
                speed = input("¿Velocidad de reproducción? (1.0 = normal, 2.0 = doble): ").strip()
                try:
                    speed = float(speed) if speed else 1.0
                except:
                    speed = 1.0
                
                # Reproducir
                recorder.play_macro(repetitions=reps, speed=speed)
            
            elif choice == '4':
                # Listar macros
                recorder.list_macros()
            
            elif choice == '5':
                # Ver detalles
                recorder.show_macro_details()
            
            elif choice == '6':
                # Guardar macro actual
                if not recorder.actions:
                    print("❌ No hay macro para guardar")
                    continue
                
                name = input("Nombre de la macro: ").strip()
                if name:
                    recorder.save_macro(name)
            
            elif choice == '7':
                # Eliminar macro
                macros = recorder.list_macros()
                if macros:
                    name = input("\nNombre de la macro a eliminar: ").strip()
                    filename = os.path.join(recorder.macros_folder, f"{name}.json")
                    
                    if os.path.exists(filename):
                        confirm = input(f"¿Seguro que quieres eliminar '{name}'? (s/n): ").strip().lower()
                        if confirm == 's':
                            os.remove(filename)
                            print(f"✅ Macro '{name}' eliminada")
                    else:
                        print(f"❌ Macro '{name}' no encontrada")
            
            elif choice == '8':
                print("\n👋 ¡Hasta luego!")
                break
            
            else:
                print("\n❌ Opción inválida")
        
        except KeyboardInterrupt:
            print("\n\n⚠️  Operación cancelada")
            keyboard.unhook_all()
        except Exception as e:
            print(f"\n❌ Error: {e}")
            keyboard.unhook_all()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 ¡Hasta luego!")
        keyboard.unhook_all()
    except Exception as e:
        print(f"\n❌ Error fatal: {e}")
        keyboard.unhook_all()
