# 🤖 Bot de Automatización con PyAutoGUI

Sistema completo de automatización con grabador de macros para Windows.

## 🚀 Inicio Rápido

### 1. Activar entorno virtual
```bash
.\venv\Scripts\activate
```

### 2. Ejecutar el programa principal

**Grabador de Macros (Recomendado):**
```bash
python macro_recorder.py
```

**Otros bots disponibles:**
```bash
python bot_pyautogui.py      # Bot interactivo completo
python bot_avanzado.py       # Tareas repetitivas
python macro_simple.py       # Grabador simple
```

## 📁 Estructura del Proyecto

```
Bot/
├── README.md                      Guía principal
├── ORGANIZACION.md               Explicación de estructura
│
├── 🎬 macro_recorder/             ⭐ TODO SOBRE MACROS
│   ├── README.md                  Guía de macros
│   ├── macro_recorder.py          Grabador completo
│   ├── macro_simple.py            Grabador simple
│   ├── INICIO_RAPIDO_MACROS.md   Inicio rápido
│   ├── GUIA_MACROS.md            Guía completa
│   └── macros/                    Macros guardadas
│
├── 🤖 bot_pyautogui.py            Bot interactivo principal
├── 🤖 bot_avanzado.py             Bot con tareas avanzadas
│
├── ejemplos/                      Ejemplos y herramientas
│   ├── README.md                  Guía de ejemplos
│   ├── ejemplo_simple.py          Ejemplo básico
│   ├── detector_coordenadas.py
│   └── bot_navegador.py
│
├── docs/                          📚 Documentación
│   ├── INDEX.md                   Índice completo
│   ├── README.md                  Doc general
│   ├── GUIA_RAPIDA.md            Referencia rápida
│   ├── RESUMEN.md
│   └── PROBLEMAS_SOLUCIONADOS.md
│
└── venv/                          Entorno virtual
```

## 🎯 ¿Qué Puedo Hacer?

### 🎬 Grabador de Macros (Carpeta macro_recorder/)

**¿Qué hace?** Graba tus clicks y acciones para reproducirlas automáticamente.

```bash
.\venv\Scripts\activate
cd macro_recorder
python macro_recorder.py
```

1. Graba tus acciones (clicks, teclas, scroll)
2. Guarda la macro con un nombre
3. Reproduce cuantas veces quieras
4. **Todo sobre macros está en la carpeta `macro_recorder/`**

### 🤖 Bots de Automatización

**Bot Interactivo:**
```bash
.\venv\Scripts\activate
python bot_pyautogui.py
```

**Bot Avanzado:**
```bash
.\venv\Scripts\activate
python bot_avanzado.py
```

### � Ejemplos

```bash
# Ejemplo simple de automatización
.\venv\Scripts\activate
python ejemplos/ejemplo_simple.py

# Detector de coordenadas del mouse
python ejemplos/detector_coordenadas.py

# Automatización web
python ejemplos/bot_navegador.py
```

## �📖 Documentación

### Macros
- **[macro_recorder/README.md](macro_recorder/README.md)** - Todo sobre macros
- **[macro_recorder/INICIO_RAPIDO_MACROS.md](macro_recorder/INICIO_RAPIDO_MACROS.md)** - Inicio rápido
- **[macro_recorder/GUIA_MACROS.md](macro_recorder/GUIA_MACROS.md)** - Guía completa

### General
- **[docs/INDEX.md](docs/INDEX.md)** - Índice de documentación
- **[docs/GUIA_RAPIDA.md](docs/GUIA_RAPIDA.md)** - Referencia de comandos
- **[docs/README.md](docs/README.md)** - Documentación general
- **[docs/PROBLEMAS_SOLUCIONADOS.md](docs/PROBLEMAS_SOLUCIONADOS.md)** - Troubleshooting

### Ejemplos
- **[ejemplos/README.md](ejemplos/README.md)** - Guía de ejemplos

## 💡 Ejemplo Rápido de Uso

**Automatizar un login con macros:**

```bash
.\venv\Scripts\activate
cd macro_recorder
python macro_recorder.py
2. Opción 1: Grabar
3. Haz: Click usuario → Escribir → Tab → Escribir password → Enter
4. Presiona ESC
5. Guarda como "mi_login"
6. Carga y reproduce cuando necesites

## 📦 Dependencias

- pyautogui 0.9.54
- pynput 1.8.1
- Pillow 12.0.0
- opencv-python 4.12.0.88

**Instalar:**
```bash
pip install -r requirements.txt
```

## ⚠️ Importante

- **Activa el entorno virtual antes de ejecutar**: `.\venv\Scripts\activate`
- **Todo sobre macros está en** `macro_recorder/`
- **FAILSAFE activado**: Mueve el mouse a la esquina superior izquierda para abortar
- **Presiona ESC** para detener la grabación de macros

## 🆘 Ayuda

Si tienes problemas, consulta: [docs/PROBLEMAS_SOLUCIONADOS.md](docs/PROBLEMAS_SOLUCIONADOS.md)

---

**¡Comienza a automatizar!** 🚀

### Macros:
```bash
.\venv\Scripts\activate
cd macro_recorder
python macro_recorder.py
```

### Bots:
```bash
.\venv\Scripts\activate
python bot_pyautogui.py
```

### Ejemplos:
```bash
.\venv\Scripts\activate
python ejemplos/ejemplo_simple.py
```
