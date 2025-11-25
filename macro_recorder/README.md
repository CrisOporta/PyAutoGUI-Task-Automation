# 🎬 MACRO RECORDER - TODO EN UNO

## ✅ ARCHIVOUNIFICADO

Todo está ahora en **un solo archivo**: `macro_recorder.py`

## 🚀 Inicio Rápido

```bash
# Ejecutar (recomendado como Administrador)
python macro_recorder.py
```

## ✨ Características Completas

### ✅ Captura TODAS las Teclas
- ✅ Tecla Windows (Win)
- ✅ Ctrl, Alt, Shift
- ✅ Todas las combinaciones (Ctrl+C, Win+R, etc.)
- ✅ Teclas especiales (Enter, Tab, Flechas, etc.)
- ✅ Letras, números, símbolos

### ✅ Funcionalidades
- 🔴 Grabar macros con tiempos precisos
- 💾 Guardar macros en archivos JSON
- ▶️  Reproducir macros (elige directamente)
- ⚡ Velocidad ajustable (0.5x - 2.0x)
- 🔄 Repeticiones (1x - infinito)
- 📋 Listar macros guardadas
- 📄 Ver detalles de macros
- 🗑️  Eliminar macros

### ✅ Flujo Mejorado
- Opción 3: Lista macros → Eliges → Configuras → ¡Reproduce!
- No necesitas cargar antes de reproducir
- Todo en un solo paso

## 📋 Menú Principal

```
1. 🔴 Grabar nueva macro (✅ Captura Win)
2. ⚙️  Cargar macro (para editar/ver)
3. ▶️  Reproducir macro (elige y ejecuta)  ← MEJORADO
4. 📋 Ver macros guardadas
5. 📄 Ver detalles de macro cargada
6. 💾 Guardar macro actual
7. 🗑️  Eliminar macro
8. ❌ Salir
```

## 💡 Ejemplo de Uso Completo

### Grabar una macro

```bash
python macro_recorder.py
```

1. Selecciona opción `1`
2. Presiona Enter
3. Realiza tus acciones (puedes usar Win+R, Ctrl+C, etc.)
4. Presiona ESC
5. Guarda con un nombre: `mi_macro`

### Reproducir una macro

```bash
python macro_recorder.py
```

1. Selecciona opción `3`
2. Verás lista de macros disponibles
3. Escribe el nombre: `mi_macro`
4. Configura repeticiones: `1`
5. Configura velocidad: `1`
6. ¡Se reproduce automáticamente!

## 🎯 Casos de Uso

### Caso 1: Abrir WhatsApp Web
```
Graba:
- Win + R
- Escribe "chrome whatsapp.com"
- Enter

Reproduce:
¡Abre WhatsApp automáticamente!
```

### Caso 2: Copiar y Pegar en Múltiples Lugares
```
Graba:
- Ctrl + A (seleccionar)
- Ctrl + C (copiar)
- Click en otro lugar
- Ctrl + V (pegar)

Reproduce:
¡Copia y pega automáticamente!
```

### Caso 3: Llenar Formulario
```
Graba:
- Click en campo 1
- Escribir nombre
- Tab
- Escribir email
- Tab
- Click en enviar

Reproduce 10 veces:
¡Llena 10 formularios automáticamente!
```

## 📁 Estructura de Archivos

```
macro_recorder/
├── macro_recorder.py          ⭐ ARCHIVO PRINCIPAL (TODO AQUÍ)
├── macro_simple.py            Versión simple (opcional)
├── macros/                    Tus macros guardadas (JSON)
├── README.md                  Este archivo
├── GUIA_MACROS.md            Guía completa
├── INICIO_RAPIDO_MACROS.md   Inicio rápido
└── _old_macro_recorder_v2.py Respaldo (antiguo)
```

## 📦 Dependencias

- pyautogui >= 0.9.54
- pynput >= 1.7.6
- keyboard >= 0.13.5 (para captura de Win)
- Pillow >= 10.0.0
- opencv-python >= 4.8.0

Ya están instaladas en `venv`.

## ⚠️ Importante

### Para Captura Completa de Tecla Windows
**Ejecuta como Administrador:**

**Opción 1: PowerShell Admin**
```powershell
# Click derecho en menú Inicio → Terminal (Admin)
cd C:\Users\criso\OneDrive\Escritorio\Bot\macro_recorder
python macro_recorder.py
```

**Opción 2: Doble Click**
```bash
# Usa ejecutar_como_admin.bat
# (pide permisos automáticamente)
```

### FAILSAFE
- Mueve el mouse a la esquina superior izquierda para abortar
- Presiona ESC para detener la grabación

## 🎉 Ventajas del Archivo Unificado

✅ **Un solo archivo** - Todo en `macro_recorder.py`
✅ **Más simple** - No hay confusión entre v1 y v2
✅ **Todas las funciones** - Captura Win + flujo mejorado
✅ **Fácil de compartir** - Un archivo, una carpeta de macros
✅ **Respaldo guardado** - `_old_macro_recorder_v2.py` por si acaso

## 📚 Documentación

- **README.md** (este archivo) - Guía principal
- **GUIA_MACROS.md** - Guía completa detallada
- **INICIO_RAPIDO_MACROS.md** - Inicio en 2 minutos
- **CAPTURA_COMPLETA.md** - Detalles de captura de teclas
- **TECLA_WINDOWS.md** - Solución para tecla Windows
- **MEJORA_REPRODUCCION.md** - Mejoras en reproducción

## 🆘 Solución de Problemas

### No captura tecla Windows
→ Ejecuta como Administrador

### Error: No module named 'keyboard'
→ `pip install keyboard`

### Las macros no funcionan
→ Graba de nuevo en la misma resolución de pantalla

### ESC no detiene
→ Ya está solucionado en esta versión

## 🚀 Comandos Rápidos

```bash
# Ejecutar
python macro_recorder.py

# Como Admin (PowerShell)
# Click derecho en Inicio → Terminal (Admin)
cd C:\Users\criso\OneDrive\Escritorio\Bot\macro_recorder
python macro_recorder.py

# Doble click
ejecutar_como_admin.bat
```

---

**¡Todo unificado en un solo archivo!** 🎬✨

**Comienza ahora:**
```bash
python macro_recorder.py
```
