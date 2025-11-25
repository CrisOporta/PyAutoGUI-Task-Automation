# 🚀 GUÍA RÁPIDA - PyAutoGUI

## Comandos Esenciales

### Activar entorno virtual
```bash
.\venv\Scripts\activate
```

### Ejecutar scripts
```bash
# Bot principal (recomendado para comenzar)
python bot_pyautogui.py

# Ejemplo simple
python ejemplo_simple.py

# Bot avanzado con tareas repetitivas
python bot_avanzado.py

# Automatización web
python bot_navegador.py

# Detector de coordenadas
python detector_coordenadas.py
```

## Snippets de Código Útiles

### 1. Configuración Básica
```python
import pyautogui
import time

# Seguridad: mouse a esquina = abortar
pyautogui.FAILSAFE = True

# Pausa entre comandos
pyautogui.PAUSE = 1
```

### 2. Información de Pantalla
```python
# Tamaño de pantalla
width, height = pyautogui.size()

# Posición del mouse
x, y = pyautogui.position()

# Color del pixel
color = pyautogui.pixel(x, y)  # RGB
```

### 3. Movimiento del Mouse
```python
# Mover a posición absoluta
pyautogui.moveTo(500, 500, duration=2)

# Mover relativamente
pyautogui.move(100, 0)  # 100px derecha

# Mover al centro
width, height = pyautogui.size()
pyautogui.moveTo(width/2, height/2)
```

### 4. Clicks
```python
# Click simple
pyautogui.click()

# Click en coordenadas
pyautogui.click(100, 200)

# Doble click
pyautogui.doubleClick()

# Click derecho
pyautogui.rightClick()

# Click y arrastrar
pyautogui.drag(100, 0, duration=1)  # arrastra 100px derecha
```

### 5. Teclado
```python
# Escribir texto
pyautogui.write('Hola Mundo', interval=0.1)

# Presionar tecla
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('esc')

# Atajos
pyautogui.hotkey('ctrl', 'c')  # Copiar
pyautogui.hotkey('ctrl', 'v')  # Pegar
pyautogui.hotkey('ctrl', 'a')  # Seleccionar todo
pyautogui.hotkey('win', 'r')   # Ejecutar
```

### 6. Capturas de Pantalla
```python
# Captura completa
screenshot = pyautogui.screenshot()
screenshot.save('captura.png')

# Captura de región (x, y, width, height)
region = (0, 0, 500, 500)
screenshot = pyautogui.screenshot(region=region)
```

### 7. Scroll
```python
# Scroll hacia abajo
pyautogui.scroll(-3)

# Scroll hacia arriba
pyautogui.scroll(3)

# Scroll en posición específica
pyautogui.scroll(-5, x=100, y=200)
```

### 8. Buscar Imagen
```python
# Buscar imagen en pantalla
location = pyautogui.locateOnScreen('boton.png')

if location:
    # Click en el centro
    center = pyautogui.center(location)
    pyautogui.click(center)
```

## Plantillas de Tareas Comunes

### Abrir Programa
```python
pyautogui.press('win')
time.sleep(1)
pyautogui.write('notepad')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(2)
```

### Llenar Formulario
```python
datos = ['Nombre', 'Email', 'Teléfono']
for dato in datos:
    pyautogui.write(dato)
    pyautogui.press('tab')
    time.sleep(0.5)
```

### Copiar y Pegar
```python
pyautogui.hotkey('ctrl', 'a')  # Seleccionar todo
time.sleep(0.3)
pyautogui.hotkey('ctrl', 'c')  # Copiar
time.sleep(0.3)
pyautogui.click(x, y)           # Click destino
pyautogui.hotkey('ctrl', 'v')  # Pegar
```

### Abrir URL en Navegador
```python
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write('https://www.google.com')
pyautogui.press('enter')
time.sleep(5)
```

## Tips y Trucos

### ✅ Mejores Prácticas
- Siempre usar `time.sleep()` entre acciones
- Activar `FAILSAFE = True` durante desarrollo
- Probar con pausas largas primero, luego optimizar
- Guardar coordenadas en variables con nombres descriptivos

### ⚠️ Evitar
- No usar sin pausas (puede ser muy rápido)
- No confiar en coordenadas absolutas si cambias resolución
- No automatizar sin supervisión hasta estar seguro

### 🔧 Debugging
```python
# Ver posición en tiempo real
while True:
    x, y = pyautogui.position()
    print(f"X: {x}, Y: {y}", end='\r')
    time.sleep(0.1)
```

### 📍 Obtener Coordenadas
```python
# Opción 1: Usar detector_coordenadas.py

# Opción 2: En código
print("Posiciona el mouse y presiona Enter...")
input()
x, y = pyautogui.position()
print(f"Coordenadas: ({x}, {y})")
```

## Teclas Especiales

```python
# Navegación
'enter', 'tab', 'esc', 'backspace', 'delete'
'home', 'end', 'pageup', 'pagedown'
'up', 'down', 'left', 'right'

# Modificadores
'ctrl', 'alt', 'shift', 'win'

# Funciones
'f1', 'f2', ... 'f12'

# Números y símbolos
'0' - '9', 'space'
```

## Manejo de Errores

```python
try:
    # Tu automatización
    pyautogui.click(100, 100)
    pyautogui.write('texto')
    
except pyautogui.FailSafeException:
    print("Detención de seguridad activada")
    
except Exception as e:
    print(f"Error: {e}")
    
finally:
    print("Limpieza si es necesaria")
```

## Ejemplos de Uso Real

### 1. Bot de Respuestas Automáticas
```python
respuestas = {
    "Hola": "¡Hola! ¿Cómo estás?",
    "Adiós": "¡Hasta luego!",
}

# Detectar texto y responder
for pregunta, respuesta in respuestas.items():
    # ... tu lógica
    pyautogui.write(respuesta)
    pyautogui.press('enter')
```

### 2. Captura Periódica de Pantalla
```python
import time
from datetime import datetime

for i in range(10):
    timestamp = datetime.now().strftime("%H%M%S")
    pyautogui.screenshot(f"captura_{timestamp}.png")
    time.sleep(60)  # cada minuto
```

### 3. Rellenar Datos Repetitivos
```python
datos = [
    ["Juan", "juan@mail.com", "555-0001"],
    ["María", "maria@mail.com", "555-0002"],
]

for fila in datos:
    for campo in fila:
        pyautogui.write(campo)
        pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(1)
```

---

**¡Consulta README.md para más información!**
