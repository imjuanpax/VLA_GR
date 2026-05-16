# 🤝 Guía de Contribución

¡Gracias por tu interés en contribuir a **VLA Robotics Agent**! Este documento te guía en el proceso.

---

## 📋 Índice

- [Cómo Reportar Bugs](#-cómo-reportar-bugs)
- [Cómo Sugerir Mejoras](#-cómo-sugerir-mejoras)
- [Proceso de Pull Request](#-proceso-de-pull-request)
- [Guía de Estilo](#-guía-de-estilo)
- [Preguntas Frecuentes](#-preguntas-frecuentes)

---

## 🐛 Cómo Reportar Bugs

### Antes de Reportar

1. **Busca en Issues existentes** - Quizás ya lo reportaron
2. **Revisa la documentación** - Especialmente troubleshooting en README
3. **Prueba la versión más reciente** - El bug podría estar solucionado

### Al Reportar

Usa este template en la sección Issues:

```markdown
## Descripción del Bug
[Descripción clara y concisa]

## Pasos para Reproducir
1. [Primer paso]
2. [Segundo paso]
3. [...]

## Comportamiento Esperado
[Qué debería pasar]

## Comportamiento Actual
[Qué sucede realmente]

## Entorno
- SO: [Windows/Linux/macOS]
- Python: [3.9/3.10/3.11]
- Versión del Proyecto: [v1.0.0]
- Webcam: [modelo si aplica]

## Logs/Screenshots
[Adjunta output de error si es relevante]
```

### Ejemplo de Buen Reporte

```markdown
## Descripción del Bug
La aplicación se cuelga cuando se corre el segundo comando

## Pasos para Reproducir
1. Correr vla_robotics_terminal.py
2. Ingresar comando: "¿Dónde está la puerta?"
3. Esperar respuesta (funciona)
4. Ingresar segundo comando: "¿Distancia al escritorio?"
5. → Se cuelga

## Comportamiento Esperado
Debería procesar el segundo comando sin problemas

## Entorno
- SO: Ubuntu 22.04
- Python: 3.10.12
- Versión: main branch
- Webcam: Logitech C920

## Error
```
Traceback (most recent call last):
  File "vla_robotics_terminal.py", line 95, in <module>
    iniciar_terminal()
RuntimeError: Camera not released properly
```
```

---

## 💡 Cómo Sugerir Mejoras

### Para Nuevas Features

```markdown
## Descripción de la Mejora
[Qué quieres agregar y por qué]

## Caso de Uso
[Cómo se usaría esta feature]

## Ejemplos de Pseudocódigo
[Si tienes ideas de implementación]

## Alternativas Consideradas
[Otros enfoques posibles]
```

### Ejemplo: Feature Request

```markdown
## Descripción de la Mejora
Agregar soporte para múltiples webcams

## Caso de Uso
En laboratorios con múltiples cámaras, sería útil 
poder seleccionar cuál usar al inicio.

## Pseudocódigo
```python
# En iniciar_terminal()
camera_id = input("Selecciona ID de cámara (0, 1, 2...): ")
image = capturar_entorno(camera_id=camera_id)
```

## Alternativas
- Usar envvar CAMERA_ID en .env
- Detectar todas las cámaras automáticamente
```

---

## 🔄 Proceso de Pull Request

### 1️⃣ Fork y Clonar

```bash
# Fork en GitHub (botón "Fork")
git clone https://github.com/tu-usuario/vla-robotics-agent.git
cd vla-robotics-agent
git remote add upstream https://github.com/usuario-original/vla-robotics-agent.git
```

### 2️⃣ Crear Rama

```bash
# Actualiza main primero
git checkout main
git pull upstream main

# Crea rama descriptiva
git checkout -b feature/agregar-soporte-multiple-webcam
# o para bugs:
git checkout -b fix/camera-memory-leak
```

**Nomenclatura:**
- `feature/descripcion` - Nuevas funcionalidades
- `fix/descripcion` - Correcciones de bugs
- `docs/descripcion` - Cambios en documentación
- `refactor/descripcion` - Reorganización de código

### 3️⃣ Hacer Cambios

```bash
# Instala dependencias de desarrollo
pip install -r requirements.txt
pip install pytest black flake8  # Para testing/linting

# Haz tus cambios
nano vla_robotics_terminal.py

# Test local
python vla_robotics_terminal.py

# Lint tu código
black vla_robotics_terminal.py
flake8 vla_robotics_terminal.py

# Commit con mensaje claro
git add .
git commit -m "feat: agregar selección de múltiples webcams

- Permite elegir webcam al iniciar
- Valida disponibilidad de cámara
- Retorna error descriptivo si no existe"
```

### 4️⃣ Push y Pull Request

```bash
git push origin feature/agregar-soporte-multiple-webcam
```

En GitHub:
1. Ve a tu fork
2. Click "Compare & pull request"
3. Describe los cambios
4. Espera revisión

### 5️⃣ Template para PR

```markdown
## Descripción
[Qué cambia y por qué]

## Tipo de Cambio
- [ ] Bug fix
- [ ] Nueva feature
- [ ] Cambio de documentación
- [ ] Refactoring

## Testing
- [ ] Probé localmente
- [ ] Agregué tests (si aplica)
- [ ] La documentación está actualizada

## Checklist
- [ ] Mi código sigue la guía de estilo
- [ ] He testeado los cambios
- [ ] No hay conflictos con main
- [ ] Agregué comentarios si es complejo

## Screenshots/Logs
[Si hay cambios visuales, adjunta screenshots]
```

---

## 📐 Guía de Estilo

### Python

```python
# ✅ BUENO
def capturar_entorno() -> Optional[Image]:
    """Captura un frame de la webcam.
    
    Returns:
        Image: Objeto PIL con frame RGB o None si hay error
    """
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("❌ Error: Sensor óptico no detectado.")
        return None
    
    time.sleep(1)
    ret, frame = cap.read()
    cap.release()
    
    if not ret:
        return None
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return Image.fromarray(frame_rgb)


# ❌ MALO
def cap_env():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Sin validación
```

### Estándares

- **Nombres:** snake_case para funciones, UPPER_CASE para constantes
- **Docstrings:** Usa docstring estilo Google
- **Longitud línea:** Máximo 88 caracteres (Black formatter)
- **Imports:** Agrupa: stdlib → third-party → local
- **Comentarios:** Explica el "por qué", no el "qué"

### Ejemplo Completo

```python
"""
Módulo para captura y procesamiento de imágenes robóticas.

Este módulo proporciona funciones para interactuar con webcams
y enviar frames al modelo VLA de Google Gemini.
"""

import os
import time
from typing import Optional

import cv2
from PIL import Image
from dotenv import load_dotenv

# Constantes
DEFAULT_CAMERA_ID = 0
CALIBRATION_TIME_SECONDS = 1


def capturar_entorno(camera_id: int = DEFAULT_CAMERA_ID) -> Optional[Image]:
    """Captura un frame de la webcam especificada.
    
    Realiza calibración de luz antes de capturar para mejorar
    la calidad de la imagen.
    
    Args:
        camera_id: ID de la webcam (default: 0)
    
    Returns:
        Image: Objeto PIL con frame en formato RGB
        None: Si hay error al acceder a la cámara
    
    Raises:
        ValueError: Si camera_id es negativo
    
    Example:
        >>> image = capturar_entorno(camera_id=0)
        >>> if image:
        ...     image.show()
    """
    if camera_id < 0:
        raise ValueError("camera_id debe ser >= 0")
    
    cap = cv2.VideoCapture(camera_id)
    
    if not cap.isOpened():
        print(f"❌ Error: No se pudo abrir cámara {camera_id}")
        return None
    
    # Calibración de luz
    time.sleep(CALIBRATION_TIME_SECONDS)
    
    ret, frame = cap.read()
    cap.release()
    
    if not ret:
        print("❌ Error: No se pudo capturar frame")
        return None
    
    # Conversión BGR → RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return Image.fromarray(frame_rgb)
```

---

## ✅ Checklist Antes de Hacer PR

- [ ] Fork actualizado con la rama principal
- [ ] Rama creada con nombre descriptivo
- [ ] Cambios están limitados a lo necesario
- [ ] Código sigue la guía de estilo (Black, Flake8)
- [ ] Agregaste docstrings en funciones nuevas
- [ ] Testeaste los cambios localmente
- [ ] Documentación actualizada (README, ARCHITECTURE)
- [ ] No hay archivos sensibles (.env real, keys, etc.)
- [ ] Commit messages son claros y descriptivos
- [ ] No hay conflictos con main

---

## 🧪 Testing

### Pruebas Manuales

```bash
# Instala en modo desarrollo
pip install -e .

# Prueba básica
python vla_robotics_terminal.py

# Test interactivo
# Ingresa: "¿Dónde hay una puerta?"
# Valida: imagen capturada, respuesta coherente
```

### Pruebas Automatizadas (Futuro)

```python
# tests/test_camera.py
import pytest
from vla_robotics_terminal import capturar_entorno

def test_capturar_entorno_returns_image():
    """Verifica que capturar_entorno retorna PIL Image."""
    image = capturar_entorno()
    assert image is not None
    assert image.mode == 'RGB'

def test_capturar_entorno_invalid_camera():
    """Verifica error con cámara inválida."""
    with pytest.raises(ValueError):
        capturar_entorno(camera_id=-1)
```

---

## ❓ Preguntas Frecuentes

**P: ¿Mi PR será aceptada?**  
R: Si sigue la guía de estilo y agrega valor, probablemente sí. Mejor discute features grandes en Issues primero.

**P: ¿Cuánto tiempo tarda la revisión?**  
R: Generalmente 1-2 semanas. Sé paciente, los mantenedores tienen vida fuera de GitHub 😄

**P: ¿Necesito tests?**  
R: No obligatorio ahora, pero son bienvenidos. Para cambios grandes, recomendado.

**P: ¿Debo actualizar requirements.txt si agrego dependencias?**  
R: **Sí**, pero discute primero en un Issue. Minimiza dependencias externas.

**P: ¿Puedo hacer commits directos a main?**  
R: No, siempre usa feature branches y PRs para mantener historial limpio.

---

## 📬 Contacto

- **Issues:** Para bugs y features
- **Discussions:** Para preguntas generales
- **Email:** Si algo es muy sensible

---

**¡Gracias por contribuir a VLA Robotics! 🚀**
