# 📁 Ejemplos y Herramientas

Esta carpeta contiene ejemplos simples y herramientas útiles para PyAutoGUI.

## 🎯 Archivos Disponibles

### 1. ejemplo_simple.py
**Descripción:** Ejemplo básico de PyAutoGUI para comenzar rápidamente.

**Qué hace:**
- Mueve el mouse al centro de la pantalla
- Hace un click
- Abre el Bloc de Notas
- Escribe un mensaje automáticamente

**Cómo ejecutar:**
```bash
.\venv\Scripts\activate
python ejemplos/ejemplo_simple.py
```

**Ideal para:**
- ✅ Primera vez usando PyAutoGUI
- ✅ Entender conceptos básicos
- ✅ Pruebas rápidas

---

### 2. detector_coordenadas.py
**Descripción:** Herramienta para detectar posiciones del mouse en tiempo real.

**Qué hace:**
- Muestra coordenadas X, Y del mouse
- Muestra color RGB del pixel bajo el cursor
- Actualiza en tiempo real

**Cómo ejecutar:**
```bash
.\venv\Scripts\activate
python ejemplos/detector_coordenadas.py
```

**Ideal para:**
- ✅ Encontrar coordenadas para tus scripts
- ✅ Planificar automatizaciones
- ✅ Saber dónde hacer click exactamente

**Tip:** Usa esto ANTES de crear macros para saber las coordenadas exactas.

---

### 3. bot_navegador.py
**Descripción:** Automatización de búsquedas en navegador web.

**Qué hace:**
- Abre el navegador predeterminado
- Navega a Google
- Realiza una búsqueda automática
- Toma captura de pantalla de resultados

**Cómo ejecutar:**
```bash
.\venv\Scripts\activate
python ejemplos/bot_navegador.py
```

**Ideal para:**
- ✅ Automatizar búsquedas web
- ✅ Investigación automatizada
- ✅ Scraping básico

---

## 🚀 Inicio Rápido

### Opción 1: Ejemplo más simple
```bash
.\venv\Scripts\activate
python ejemplos/ejemplo_simple.py
```

### Opción 2: Detector de coordenadas
```bash
.\venv\Scripts\activate
python ejemplos/detector_coordenadas.py
# Mueve el mouse para ver coordenadas
# Presiona Ctrl+C para salir
```

### Opción 3: Automatización web
```bash
.\venv\Scripts\activate
python ejemplos/bot_navegador.py
```

## 💡 Tips

### Usar el Detector de Coordenadas

1. Ejecuta `detector_coordenadas.py`
2. Mueve el mouse sobre el elemento que quieres automatizar
3. Anota las coordenadas X, Y
4. Usa esas coordenadas en tus scripts:
   ```python
   pyautogui.click(x, y)
   ```

### Modificar los Ejemplos

Todos estos scripts son **código abierto** y **modificables**. Úsalos como base para tus propias automatizaciones:

1. Copia el archivo
2. Modifica según tus necesidades
3. Ejecuta tu versión personalizada

### Crear Tu Propio Ejemplo

```python
import pyautogui
import time

# Tu código aquí
pyautogui.click(100, 100)
time.sleep(1)
pyautogui.write('Hola!')
```

## 🎓 Progresión de Aprendizaje

### Nivel 1: Principiante
→ `ejemplo_simple.py`
- Aprende conceptos básicos
- Entiende cómo funciona PyAutoGUI

### Nivel 2: Intermedio
→ `detector_coordenadas.py`
- Aprende a encontrar coordenadas
- Planifica tus automatizaciones

### Nivel 3: Aplicación
→ `bot_navegador.py`
- Automatización práctica
- Proyecto completo ejemplo

### Nivel 4: Creación
→ Usa el **grabador de macros** en la raíz
```bash
python macro_recorder.py
```

## 📚 Documentación Relacionada

- **[Guía Rápida](../docs/GUIA_RAPIDA.md)** - Snippets de código
- **[Documentación General](../docs/README.md)** - Info completa de PyAutoGUI
- **[Guía de Macros](../docs/GUIA_MACROS.md)** - Grabador de macros

## ⚠️ Notas Importantes

- **Siempre activa el entorno virtual** antes de ejecutar
- **FAILSAFE activado**: Mueve el mouse a la esquina superior izquierda para abortar
- Los tiempos de espera pueden variar según tu PC

## 🔗 Volver

[← Volver al README principal](../README.md)

---

**¡Experimenta y aprende!** 🚀
