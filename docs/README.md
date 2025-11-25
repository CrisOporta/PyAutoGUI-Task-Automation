# 🤖 Bot de Automatización con PyAutoGUI

Bot completo de automatización para Windows usando PyAutoGUI. Este proyecto incluye múltiples ejemplos y herramientas para automatizar tareas en tu computadora.

## 📋 Contenido

- **bot_pyautogui.py** - Script principal con menú interactivo completo
- **bot_avanzado.py** - Bot con tareas repetitivas avanzadas
- **macro_recorder.py** ⭐ **NUEVO** - Grabador completo de macros (clicks, teclas, scroll)
- **macro_simple.py** - Grabador simple de macros (solo clicks)
- **ejemplo_simple.py** - Ejemplo básico para comenzar rápidamente
- **bot_navegador.py** - Automatización de búsquedas web
- **detector_coordenadas.py** - Herramienta para detectar coordenadas del mouse

## 🚀 Instalación

### 1. Activar el entorno virtual

```bash
.\venv\Scripts\activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 💻 Uso

### Ejecutar el bot principal (recomendado para comenzar)

```bash
python bot_pyautogui.py
```

Este script incluye un menú interactivo con todas las funcionalidades:
- ✅ Información de pantalla
- ✅ Demo de movimiento del mouse
- ✅ Demo de clicks
- ✅ Demo de teclado
- ✅ Demo de scroll
- ✅ Capturas de pantalla
- ✅ Detector de posición del mouse
- ✅ Tarea automatizada completa

### Ejemplo simple

Para un ejemplo rápido y directo:

```bash
python ejemplo_simple.py
```

### Automatización web

Para automatizar búsquedas en el navegador:

```bash
python bot_navegador.py
```

### Detector de coordenadas

Para encontrar las coordenadas exactas donde hacer click:

```bash
python detector_coordenadas.py
```

### ⭐ GRABADOR DE MACROS (Recomendado para automatización personalizada)

**Grabador Completo** - Captura clicks, teclas, scroll y tiempos:

```bash
python macro_recorder.py
```

Características:
- 🔴 Graba TODAS tus acciones (clicks, teclas, scroll)
- 💾 Guarda macros en archivos JSON reutilizables
- ▶️ Reproduce con velocidad ajustable
- 🔁 Repite múltiples veces
- 📋 Lista y gestiona todas tus macros

**Grabador Simple** - Solo clicks y tiempos de espera:

```bash
python macro_simple.py
```

Ideal para:
- ✅ Automatizar clicks repetitivos
- ✅ Formularios con campos en posiciones fijas
- ✅ Tareas simples y rápidas

#### 📖 Cómo usar el Grabador de Macros

1. **Ejecuta el grabador**:
   ```bash
   python macro_recorder.py
   ```

2. **Graba tu macro**:
   - Selecciona opción 1 "Grabar nueva macro"
   - Presiona Enter para comenzar
   - Realiza los clicks y acciones que quieres automatizar
   - Presiona ESC cuando termines
   - Guarda la macro con un nombre

3. **Reproduce tu macro**:
   - Selecciona opción 2 "Cargar macro"
   - Selecciona opción 3 "Reproducir"
   - Elige cuántas veces repetir
   - ¡Listo! La macro se ejecuta automáticamente

#### 💡 Ejemplos de uso de Macros

**Ejemplo 1: Rellenar formulario repetitivo**
```
1. Graba: Click en campo → Escribe texto → Tab → Repeat
2. Guarda como "formulario_cliente"
3. Reproduce 100 veces para llenar 100 registros
```

**Ejemplo 2: Proceso de login automático**
```
1. Graba: Click en usuario → Escribe → Tab → Escribe contraseña → Enter
2. Guarda como "auto_login"
3. Reproduce cuando necesites
```

**Ejemplo 3: Descarga de múltiples archivos**
```
1. Graba: Click en botón descarga → Espera → Click OK → Repeat
2. Guarda como "descargar_archivos"
3. Reproduce las veces necesarias
```

## 🛡️ Seguridad

**FAILSAFE activado**: Si mueves el mouse rápidamente a la esquina superior izquierda de la pantalla, el programa se detendrá automáticamente.

## 📚 Funcionalidades Principales

### 1. Movimiento del Mouse

```python
import pyautogui

# Mover a coordenadas absolutas
pyautogui.moveTo(100, 100, duration=2)

# Mover relativamente
pyautogui.move(50, 0)  # 50px a la derecha
```

### 2. Clicks

```python
# Click simple
pyautogui.click()

# Click en coordenadas específicas
pyautogui.click(x=100, y=200)

# Doble click
pyautogui.doubleClick()

# Click derecho
pyautogui.rightClick()
```

### 3. Teclado

```python
# Escribir texto
pyautogui.write('Hola Mundo', interval=0.1)

# Presionar tecla
pyautogui.press('enter')

# Atajos de teclado
pyautogui.hotkey('ctrl', 'c')  # Copiar
pyautogui.hotkey('ctrl', 'v')  # Pegar
```

### 4. Capturas de Pantalla

```python
# Captura completa
screenshot = pyautogui.screenshot()
screenshot.save('captura.png')

# Captura de región
region = (0, 0, 300, 400)  # x, y, width, height
screenshot = pyautogui.screenshot(region=region)
```

### 5. Obtener Información

```python
# Tamaño de pantalla
width, height = pyautogui.size()

# Posición del mouse
x, y = pyautogui.position()

# Color del pixel
color = pyautogui.pixel(x, y)  # Retorna RGB
```

### 6. Scroll

```python
# Scroll hacia abajo
pyautogui.scroll(-3)

# Scroll hacia arriba
pyautogui.scroll(3)
```

## 🎯 Ejemplos de Uso Real

### Ejemplo 1: Abrir una aplicación y escribir

```python
import pyautogui
import time

# Abrir menú inicio
pyautogui.press('win')
time.sleep(1)

# Buscar aplicación
pyautogui.write('notepad')
time.sleep(1)

# Abrir
pyautogui.press('enter')
time.sleep(2)

# Escribir
pyautogui.write('Mensaje automatizado!')
```

### Ejemplo 2: Automatizar formulario web

```python
import pyautogui
import time

# Hacer click en campo nombre
pyautogui.click(500, 300)
pyautogui.write('Juan Perez')

# Tab al siguiente campo
pyautogui.press('tab')

# Escribir email
pyautogui.write('juan@ejemplo.com')

# Enviar formulario
pyautogui.press('enter')
```

### Ejemplo 3: Tomar captura y buscar elemento

```python
import pyautogui

# Buscar un botón por imagen
button_location = pyautogui.locateOnScreen('boton.png')

if button_location:
    # Hacer click en el centro del botón
    button_center = pyautogui.center(button_location)
    pyautogui.click(button_center)
else:
    print("Botón no encontrado")
```

## ⚙️ Configuración Útil

```python
import pyautogui

# Pausa automática entre comandos (segundos)
pyautogui.PAUSE = 1

# Activar failsafe (mover mouse a esquina para abortar)
pyautogui.FAILSAFE = True

# Duración de movimientos
pyautogui.DURATION = 0.5
```

## 🔧 Solución de Problemas

### Error: "pyautogui.FailSafeException"
- Moviste el mouse a la esquina superior izquierda (esto es intencional como medida de seguridad)
- Para desactivar: `pyautogui.FAILSAFE = False` (no recomendado)

### El bot escribe demasiado rápido
- Ajusta el parámetro `interval` en `pyautogui.write()`:
  ```python
  pyautogui.write('texto', interval=0.1)  # 0.1 segundos entre teclas
  ```

### Las coordenadas no son precisas
- Usa el `detector_coordenadas.py` para obtener coordenadas exactas
- Ten en cuenta que las coordenadas pueden cambiar si cambias la resolución de pantalla

## 📖 Recursos Adicionales

- [Documentación oficial de PyAutoGUI](https://pyautogui.readthedocs.io/)
- [Cheat Sheet de PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/quickstart.html)

## ⚠️ Advertencias

1. **Usa con responsabilidad**: Este bot puede controlar tu computadora
2. **Guarda tu trabajo**: Antes de ejecutar automatizaciones complejas
3. **Prueba primero**: Usa los ejemplos simples antes de crear automatizaciones complejas
4. **Tiempos de espera**: Ajusta los `time.sleep()` según la velocidad de tu computadora

## 🎓 Tips y Mejores Prácticas

1. **Siempre usa FAILSAFE** en desarrollo
2. **Añade pausas** entre acciones importantes
3. **Usa coordenadas relativas** cuando sea posible
4. **Documenta tus coordenadas** en comentarios
5. **Prueba en ventanas pequeñas** primero
6. **Captura screenshots** para debugging

## 📝 Licencia

Este proyecto es de uso libre para aprendizaje y automatización personal.

---

**¡Disfruta automatizando! 🚀**
