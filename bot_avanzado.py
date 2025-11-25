"""
Ejemplo Avanzado: Bot de Tareas Repetitivas
Este script demuestra cómo automatizar tareas repetitivas
"""

import pyautogui
import time
from datetime import datetime

# Configuración
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5


def log(mensaje):
    """Función para imprimir mensajes con timestamp"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {mensaje}")


def esperar_con_cuenta_regresiva(segundos, mensaje="Esperando"):
    """Muestra una cuenta regresiva mientras espera"""
    print(f"\n{mensaje}:", end=" ")
    for i in range(segundos, 0, -1):
        print(f"{i}...", end=" ", flush=True)
        time.sleep(1)
    print("¡Listo!")


def copiar_y_pegar_repetidamente():
    """
    Ejemplo: Copiar un texto y pegarlo múltiples veces
    Útil para rellenar formularios repetitivos
    """
    print("\n" + "=" * 60)
    print("TAREA: Copiar y Pegar Texto Repetidamente")
    print("=" * 60)
    
    # Texto a copiar
    texto = "Este texto será pegado múltiples veces - "
    repeticiones = 5
    
    print(f"Se pegará el texto {repeticiones} veces")
    esperar_con_cuenta_regresiva(5, "Abre un editor de texto y haz click donde quieras pegar")
    
    for i in range(1, repeticiones + 1):
        log(f"Pegando texto {i}/{repeticiones}")
        pyautogui.write(f"{texto}Línea {i}")
        pyautogui.press('enter')
        time.sleep(0.3)
    
    log("✅ Tarea completada!")


def tomar_multiples_screenshots():
    """
    Toma varias capturas de pantalla con intervalos
    Útil para documentar procesos
    """
    print("\n" + "=" * 60)
    print("TAREA: Tomar Screenshots Periódicamente")
    print("=" * 60)
    
    num_capturas = 3
    intervalo = 3  # segundos
    
    print(f"Se tomarán {num_capturas} capturas con intervalo de {intervalo}s")
    esperar_con_cuenta_regresiva(3, "Preparando")
    
    for i in range(1, num_capturas + 1):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"captura_{i}_{timestamp}.png"
        
        log(f"Tomando captura {i}/{num_capturas}")
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)
        log(f"✅ Guardada como: {filename}")
        
        if i < num_capturas:
            time.sleep(intervalo)
    
    print("\n✅ Todas las capturas completadas!")


def llenar_formulario_automatico():
    """
    Simula el llenado automático de un formulario
    Usando TAB para navegar entre campos
    """
    print("\n" + "=" * 60)
    print("TAREA: Llenar Formulario Automáticamente")
    print("=" * 60)
    
    # Datos del formulario
    datos = {
        "Nombre": "Juan Pérez",
        "Email": "juan.perez@ejemplo.com",
        "Teléfono": "555-1234",
        "Dirección": "Calle Principal 123",
        "Ciudad": "Ciudad de México"
    }
    
    print("Datos a ingresar:")
    for campo, valor in datos.items():
        print(f"  {campo}: {valor}")
    
    esperar_con_cuenta_regresiva(5, "Abre un formulario y haz click en el primer campo")
    
    for campo, valor in datos.items():
        log(f"Llenando campo: {campo}")
        pyautogui.write(valor, interval=0.05)
        pyautogui.press('tab')  # Ir al siguiente campo
        time.sleep(0.3)
    
    log("✅ Formulario llenado!")


def macro_rapida_calc():
    """
    Abre la calculadora de Windows y hace una operación
    """
    print("\n" + "=" * 60)
    print("TAREA: Abrir Calculadora y Hacer Operación")
    print("=" * 60)
    
    log("Abriendo calculadora...")
    
    # Abrir calculadora con atajo de Windows
    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    
    pyautogui.write('calc')
    pyautogui.press('enter')
    time.sleep(2)
    
    # Hacer cálculo: 123 + 456 =
    operacion = "123+456"
    log(f"Calculando: {operacion}")
    
    for char in operacion:
        pyautogui.press(char)
        time.sleep(0.2)
    
    pyautogui.press('enter')
    time.sleep(1)
    
    # Tomar screenshot del resultado
    log("Tomando screenshot del resultado...")
    screenshot = pyautogui.screenshot()
    screenshot.save('resultado_calculadora.png')
    
    log("✅ Operación completada! Screenshot guardado")


def scroll_automatico_lento():
    """
    Hace scroll lento hacia abajo
    Útil para leer contenido largo o hacer scroll en presentaciones
    """
    print("\n" + "=" * 60)
    print("TAREA: Scroll Automático Lento")
    print("=" * 60)
    
    scrolls = 10
    pausa_entre_scroll = 1
    
    print(f"Se hará scroll {scrolls} veces con pausa de {pausa_entre_scroll}s")
    esperar_con_cuenta_regresiva(5, "Abre una página web o documento largo")
    
    for i in range(1, scrolls + 1):
        log(f"Scroll {i}/{scrolls}")
        pyautogui.scroll(-2)  # Scroll hacia abajo
        time.sleep(pausa_entre_scroll)
    
    log("✅ Scroll completado!")


def busqueda_automatica_multiple():
    """
    Realiza múltiples búsquedas en Google
    """
    print("\n" + "=" * 60)
    print("TAREA: Búsquedas Automáticas")
    print("=" * 60)
    
    terminos_busqueda = [
        "PyAutoGUI tutorial",
        "Python automation",
        "Web scraping Python"
    ]
    
    print("Términos a buscar:")
    for i, termino in enumerate(terminos_busqueda, 1):
        print(f"  {i}. {termino}")
    
    esperar_con_cuenta_regresiva(5, "Abre Google en tu navegador")
    
    for i, termino in enumerate(terminos_busqueda, 1):
        log(f"Buscando ({i}/{len(terminos_busqueda)}): {termino}")
        
        # Seleccionar todo el texto en la barra de búsqueda
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.3)
        
        # Escribir nuevo término
        pyautogui.write(termino, interval=0.05)
        time.sleep(0.5)
        
        # Buscar
        pyautogui.press('enter')
        time.sleep(3)
        
        # Tomar screenshot
        filename = f"busqueda_{i}.png"
        pyautogui.screenshot(filename)
        log(f"Screenshot guardado: {filename}")
        
        # Esperar antes de la siguiente búsqueda
        if i < len(terminos_busqueda):
            time.sleep(2)
    
    log("✅ Búsquedas completadas!")


def menu_principal():
    """Menú interactivo para elegir tareas"""
    
    print("""
    ╔═══════════════════════════════════════════════════╗
    ║                                                   ║
    ║    BOT DE TAREAS REPETITIVAS CON PYAUTOGUI       ║
    ║                                                   ║
    ╚═══════════════════════════════════════════════════╝
    
    ⚠️  IMPORTANTE: Mover el mouse a la esquina superior
       izquierda para abortar en cualquier momento.
    """)
    
    while True:
        print("\n" + "=" * 60)
        print("TAREAS DISPONIBLES")
        print("=" * 60)
        print("1. Copiar y pegar texto repetidamente")
        print("2. Tomar múltiples screenshots")
        print("3. Llenar formulario automáticamente")
        print("4. Calcular con la calculadora de Windows")
        print("5. Scroll automático lento")
        print("6. Búsquedas automáticas en Google")
        print("7. EJECUTAR TODAS LAS TAREAS")
        print("8. Salir")
        print("=" * 60)
        
        opcion = input("\nSelecciona una tarea (1-8): ").strip()
        
        try:
            if opcion == '1':
                copiar_y_pegar_repetidamente()
            elif opcion == '2':
                tomar_multiples_screenshots()
            elif opcion == '3':
                llenar_formulario_automatico()
            elif opcion == '4':
                macro_rapida_calc()
            elif opcion == '5':
                scroll_automatico_lento()
            elif opcion == '6':
                busqueda_automatica_multiple()
            elif opcion == '7':
                confirm = input("\n⚠️  Esto ejecutará TODAS las tareas. ¿Continuar? (s/n): ")
                if confirm.lower() == 's':
                    for tarea in [copiar_y_pegar_repetidamente, tomar_multiples_screenshots,
                                  llenar_formulario_automatico, macro_rapida_calc,
                                  scroll_automatico_lento, busqueda_automatica_multiple]:
                        tarea()
                        print("\n" + "─" * 60)
                        time.sleep(2)
            elif opcion == '8':
                print("\n👋 ¡Hasta luego!")
                break
            else:
                print("\n❌ Opción inválida")
                
        except pyautogui.FailSafeException:
            print("\n\n⚠️  FAILSAFE ACTIVADO - Bot detenido por el usuario")
            break
        except KeyboardInterrupt:
            print("\n\n⚠️  Interrumpido por el usuario")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    try:
        menu_principal()
    except Exception as e:
        print(f"\n❌ Error fatal: {e}")
