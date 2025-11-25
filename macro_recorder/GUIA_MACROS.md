# 🎬 GUÍA DEL GRABADOR DE MACROS

## ¿Qué es una Macro?

Una **macro** es una secuencia de acciones grabadas que puedes reproducir automáticamente cuantas veces quieras. Es como grabar un video de tus acciones y reproducirlo después.

## 🚀 Inicio Rápido

### 1. Ejecutar el Grabador

```bash
.\venv\Scripts\activate
python macro_recorder.py
```

### 2. Grabar tu Primera Macro

1. En el menú, selecciona **"1. Grabar nueva macro"**
2. Presiona **Enter** para comenzar
3. Realiza las acciones que quieres automatizar:
   - Clicks del mouse
   - Teclas presionadas
   - Scroll
4. Presiona **ESC** cuando termines
5. Guarda con un nombre descriptivo (ej: "login_sistema")

### 3. Reproducir tu Macro

1. Selecciona **"2. Cargar macro"**
2. Escribe el nombre de tu macro
3. Selecciona **"3. Reproducir macro"**
4. Indica cuántas veces quieres que se repita
5. ¡Observa cómo se ejecuta automáticamente!

## 📚 Dos Versiones Disponibles

### 🎯 Macro Recorder (Completo)

**Archivo:** `macro_recorder.py`

**Captura:**
- ✅ Clicks (izquierdo, derecho, medio)
- ✅ Teclas presionadas
- ✅ Scroll
- ✅ Tiempos de espera automáticos

**Mejor para:**
- Automatizaciones complejas
- Procesos que requieren teclado
- Workflows completos

### 🎯 Macro Simple

**Archivo:** `macro_simple.py`

**Captura:**
- ✅ Solo clicks izquierdos
- ✅ Tiempos de espera automáticos

**Mejor para:**
- Clicks repetitivos
- Automatizaciones simples
- Aprendizaje y pruebas rápidas

## 💡 Casos de Uso Reales

### Caso 1: Rellenar Formulario Web

**Problema:** Necesitas llenar 50 formularios idénticos con datos diferentes.

**Solución:**
```
1. Graba una macro haciendo:
   - Click en primer campo
   - Tab para siguiente campo
   - Tab para siguiente campo
   - Click en botón "Enviar"

2. Guarda como "estructura_formulario"

3. Modifica un script para que:
   - Cargue la macro
   - Antes de cada campo, escriba datos diferentes
   - Reproduzca la macro 50 veces
```

### Caso 2: Proceso de Login

**Problema:** Tienes que hacer login en un sistema múltiples veces al día.

**Solución:**
```
1. Graba:
   - Click en campo usuario
   - Escribir usuario
   - Tab
   - Escribir contraseña
   - Click en "Iniciar sesión"

2. Guarda como "login_rapido"

3. Cada vez que necesites login:
   - Ejecuta macro_recorder.py
   - Carga "login_rapido"
   - Reproduce
```

### Caso 3: Descargar Múltiples Archivos

**Problema:** Necesitas hacer click en 100 botones de descarga.

**Solución:**
```
1. Graba:
   - Click en botón descarga
   - Espera 2 segundos
   - Click en "Guardar"
   - Scroll hacia abajo

2. Guarda como "descargar_archivo"

3. Reproduce 100 veces (con repeticiones)
```

### Caso 4: Pruebas de Software

**Problema:** Necesitas probar la misma secuencia de clicks 20 veces.

**Solución:**
```
1. Graba el flujo de prueba una vez
2. Guarda como "test_caso_1"
3. Reproduce 20 veces automáticamente
4. Compara resultados
```

## ⚙️ Características Avanzadas

### Velocidad de Reproducción

```
Velocidad 0.5x = Mitad de velocidad (más lento)
Velocidad 1.0x = Velocidad normal
Velocidad 2.0x = Doble velocidad (más rápido)
```

**Cuándo usar cada velocidad:**
- **0.5x - 0.8x:** Sistemas lentos, aplicaciones web
- **1.0x:** Velocidad normal grabada
- **1.5x - 2.0x:** Para acelerar procesos conocidos

### Repeticiones

Puedes reproducir una macro N veces:
```
Repeticiones: 10
→ La macro se ejecutará 10 veces seguidas
```

**Útil para:**
- Ingresar múltiples registros
- Pruebas repetitivas
- Procesamiento por lotes

### Gestión de Macros

**Listar todas:** Opción 4 en el menú
**Ver detalles:** Opción 5 (muestra cada acción grabada)
**Eliminar:** Opción 7 (borra macros no necesarias)

## 📁 Formato de Archivo

Las macros se guardan en formato JSON en la carpeta `macros/`:

```json
{
  "name": "mi_macro",
  "created": "2025-11-24 22:30:00",
  "total_actions": 5,
  "actions": [
    {
      "type": "click",
      "x": 500,
      "y": 300,
      "button": "left",
      "wait_before": 0.5,
      "timestamp": "22:30:01.234"
    },
    ...
  ]
}
```

**Ventajas:**
- ✅ Portátil (puedes compartir macros)
- ✅ Editable (puedes modificar manualmente)
- ✅ Legible (fácil de entender)

## 🛠️ Tips y Trucos

### 1. Nombres Descriptivos

❌ Mal: "macro1", "test", "asd"
✅ Bien: "login_sistema", "formulario_cliente", "descargar_reportes"

### 2. Macros Cortas y Específicas

❌ Mal: Una macro de 200 acciones
✅ Bien: Varias macros pequeñas y específicas

**Razón:** Más fácil de mantener y reutilizar.

### 3. Prueba Primero con 1 Repetición

Antes de reproducir 100 veces:
1. Reproduce 1 vez
2. Verifica que funcione correctamente
3. Luego sí, reproduce N veces

### 4. Considera los Tiempos de Carga

Si tu aplicación es lenta:
- Graba con pausas naturales
- O usa velocidad 0.5x - 0.8x al reproducir

### 5. Usa Coordenadas Relativas

Si cambias de resolución de pantalla, las macros pueden fallar.

**Solución:**
- Maximiza ventanas antes de grabar
- Usa siempre la misma resolución
- O graba macros diferentes para cada resolución

### 6. Combina con Scripts Python

Puedes cargar y reproducir macros desde tus propios scripts:

```python
from macro_recorder import MacroRecorder

recorder = MacroRecorder()
recorder.load_macro("mi_macro")
recorder.play_macro(repetitions=10, speed=1.5)
```

## 🔧 Solución de Problemas

### Problema: La macro no hace click en el lugar correcto

**Causas:**
- Cambió la resolución de pantalla
- La ventana no está en la misma posición
- La aplicación cambió de diseño

**Soluciones:**
- Graba de nuevo con la configuración actual
- Maximiza ventanas antes de grabar
- Verifica que la aplicación esté en la misma posición

### Problema: La macro va muy rápido

**Solución:**
```
Al reproducir, usa velocidad más lenta:
Velocidad: 0.5
```

### Problema: La macro va muy lento

**Solución:**
```
Al reproducir, usa velocidad más rápida:
Velocidad: 2.0
```

### Problema: Algunas teclas no se graban

**Causa:** Algunas teclas especiales pueden no capturarse.

**Solución:**
- Usa el grabador completo (macro_recorder.py)
- O graba usando clicks en vez de teclas

### Problema: La macro se detiene en medio

**Causas:**
- FailSafe activado (mouse en esquina)
- Error en la aplicación
- Ventana no está activa

**Soluciones:**
- No muevas el mouse a la esquina durante reproducción
- Asegúrate que la ventana esté activa
- Revisa los detalles de la macro (opción 5)

## 🎓 Mejores Prácticas

1. **Graba con ventanas maximizadas**
2. **Espera a que carguen los elementos** antes de hacer click
3. **Prueba con 1 repetición** primero
4. **Usa nombres descriptivos** para tus macros
5. **Mantén macros pequeñas** y específicas
6. **Documenta tus macros** (qué hacen, cuándo usarlas)
7. **Haz backups** de tus macros importantes
8. **Prueba en entorno de desarrollo** antes de producción

## 📊 Comparación Rápida

| Característica | Macro Recorder | Macro Simple |
|----------------|----------------|--------------|
| Clicks | ✅ | ✅ |
| Teclas | ✅ | ❌ |
| Scroll | ✅ | ❌ |
| Complejidad | Media | Baja |
| Velocidad ajustable | ✅ | ❌ |
| Mejor para | Workflows completos | Clicks repetitivos |

## 🚀 Siguientes Pasos

1. **Practica con macros simples** (3-5 acciones)
2. **Experimenta con repeticiones**
3. **Prueba diferentes velocidades**
4. **Crea tu biblioteca de macros** útiles
5. **Comparte tus macros** con tu equipo

## 💬 Preguntas Frecuentes

**P: ¿Puedo editar una macro después de grabarla?**
R: Sí, las macros son archivos JSON que puedes editar manualmente.

**P: ¿Las macros funcionan en cualquier programa?**
R: Sí, funcionan en cualquier programa que acepte clicks y teclas.

**P: ¿Puedo pausar una macro en ejecución?**
R: Mueve el mouse a la esquina superior izquierda para activar FailSafe.

**P: ¿Cuántas macros puedo guardar?**
R: Ilimitadas. Todas se guardan en la carpeta `macros/`.

**P: ¿Puedo compartir mis macros con otros?**
R: Sí, solo comparte los archivos .json de la carpeta `macros/`.

---

**¡Ahora estás listo para automatizar cualquier tarea repetitiva! 🎉**
