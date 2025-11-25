# 🎯 INICIO RÁPIDO - GRABADOR DE MACROS

## ¿Qué hace este programa?

Te permite **GRABAR** tus clicks y acciones del mouse/teclado, y luego **REPRODUCIRLAS** automáticamente cuantas veces quieras. Es como tener un asistente que repite exactamente lo que tú haces.

## 🚀 Uso Rápido (3 pasos)

### Paso 1: Activar entorno virtual
```bash
.\venv\Scripts\activate
```

### Paso 2: Ejecutar el grabador
```bash
python macro_recorder.py
```

### Paso 3: Seguir el menú
```
1. Opción 1 → Grabar nueva macro
2. Hacer tus clicks y acciones
3. Presionar ESC cuando termines
4. Guardar con un nombre
5. Opción 2 → Cargar la macro
6. Opción 3 → Reproducir
```

## 📖 Dos versiones disponibles

### 🎯 macro_recorder.py (COMPLETO - Recomendado)
- Graba clicks, teclas, scroll
- Guarda en archivos JSON
- Reproduce con velocidad ajustable
- Múltiples repeticiones

```bash
python macro_recorder.py
```

### 🎯 macro_simple.py (SIMPLE)
- Solo graba clicks
- Más fácil de usar
- Ideal para principiantes

```bash
python macro_simple.py
```

## 💡 Ejemplo práctico

**Quieres hacer login 10 veces:**

1. Ejecuta: `python macro_recorder.py`
2. Opción: 1 (Grabar)
3. Haz: Click en usuario → Escribir → Tab → Escribir password → Enter
4. Presiona: ESC
5. Guarda como: "mi_login"
6. Opción: 2 (Cargar) → escribe "mi_login"
7. Opción: 3 (Reproducir) → escribe "10"
8. ¡Listo! Se ejecuta 10 veces automáticamente

## ⚠️ Importante

- **FAILSAFE:** Mueve el mouse a la esquina superior izquierda para detener
- **Prueba primero con 1 repetición** antes de usar muchas
- **Las macros se guardan en:** `macros/nombre.json`

## 📚 Más información

- **Guía completa:** Lee `GUIA_MACROS.md`
- **Documentación general:** Lee `README.md`
- **Referencia rápida:** Lee `GUIA_RAPIDA.md`

## 🆘 Ayuda rápida

**Error: "No module named 'pynput'"**
```bash
pip install pynput
```

**La macro no funciona bien:**
- Graba de nuevo
- Usa velocidad más lenta (0.5x)
- Asegúrate que la ventana esté en la misma posición

**¿Cómo ver mis macros guardadas?**
- Opción 4 en el menú
- O mira la carpeta `macros/`

---

**¡Listo para automatizar! 🚀**
