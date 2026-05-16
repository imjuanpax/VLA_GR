# 🤖 VLA Robotics Agent - Razonamiento Espacial Embodied

**Vision-Language-Action (VLA) System con Razonamiento Geométrico en Tiempo Real**

Un agente robótico inteligente que combina visión por computadora, procesamiento de lenguaje natural y razonamiento espacial para navegar e interpretar entornos dinámicos. Utiliza el modelo **Gemini Robotics ER 1.6** para extraer coordenadas, distancias relativas y ejecutar acciones robóticas basadas en comandos naturales.

---

## 🎯 Características Principales

✨ **Visión Espacial en Tiempo Real**
- Captura automática del entorno mediante webcam
- Análisis de geometría 3D a partir de imágenes 2D
- Extracción de coordenadas relativas `[ymin, xmin, ymax, xmax]` en escala 0-1000

🧠 **Razonamiento VLA (Vision-Language-Action)**
- Integración con modelo Gemini Robotics ER 1.6
- Procesamiento de comandos en lenguaje natural
- Estimación de distancias: primer plano, medio, fondo

🎤 **Interfaz Interactiva**
- Terminal de control con prompts intuitivos
- Retroalimentación en tiempo real del agente
- Terminología técnica de navegación robótica

⚙️ **Stack Moderno**
- `google-genai`: SDK oficial de Gemini
- `opencv-python`: procesamiento de video
- `pillow`: manipulación de imágenes
- `python-dotenv`: gestión de credenciales

---

## 🚀 Instalación Rápida

### Requisitos Previos
- **Python 3.9+**
- **Webcam** conectada y funcional
- **API Key de Google Gemini** (obtén una en [Google AI Studio](https://aistudio.google.com/app/apikeys))

### Pasos

1. **Clona el repositorio**
```bash
git clone https://github.com/tu-usuario/vla-robotics-agent.git
cd vla-robotics-agent
```

2. **Crea un entorno virtual**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instala las dependencias**
```bash
pip install -r requirements.txt
```

4. **Configura tu API Key**
Crea un archivo `.env` en la raíz del proyecto:
```env
GEMINI_API_KEY=tu_api_key_aqui
```

5. **Ejecuta el agente**
```bash
python vla_agent.py
```

---

## 📖 Uso

### Terminal Interactiva

```
🤖 TERMINAL DE CONTROL VLA (RAZONAMIENTO ESPACIAL)
Modelo: gemini-robotics-er-1.6-preview
Escribe 'salir' para finalizar.
==================================================================

🎙️ Operador (Comando): ¿Dónde está la puerta más cercana?

📸 [Sensor Óptico] Capturando escena...
🧠 [Procesador Neuronal] Razonando geometría y contexto...

🦾 VLA Agent Responde:
Coordenadas relativas: [120, 200, 380, 650]
Distancia estimada: Primer plano (centro de la escena)
Orientación: 45° a la derecha...
```

### Ejemplos de Comandos

```python
# Consultas espaciales
"¿Dónde está el objeto rojo?"
"Identifica obstáculos en la zona media"
"¿Cuál es la ruta más eficiente hacia la ventana?"

# Análisis geométrico
"Calcula la distancia relativa al escritorio"
"Detecta ángulos y superficies planas"

# Acciones robóticas simuladas
"Navega hacia la esquina izquierda"
"Identifica puntos de agarre en el entorno"
```

---

## 🏗️ Arquitectura

```
┌─────────────────────────────────────────┐
│         TERMINAL INTERACTIVA            │
│     (Entrada de comandos naturales)     │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│      CAPTURA DE ENTORNO (OpenCV)        │
│    (Webcam → Imagen RGB)                │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│    MODELO GEMINI ROBOTICS ER 1.6        │
│  (Visión + Lenguaje + Razonamiento)     │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│      EXTRACCIÓN DE PARÁMETROS           │
│  - Coordenadas [ymin, xmin, ymax, xmax] │
│  - Distancias relativas                 │
│  - Orientaciones y ángulos              │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│    RESPUESTA AL OPERADOR                │
│  (Terminología técnica robótica)        │
└─────────────────────────────────────────┘
```

---

## 📋 Estructura del Proyecto

```
vla-robotics-agent/
├── vla_agent.py              # Script principal
├── .env                      # Configuración (no subir a GitHub)
├── .gitignore               # Archivos a ignorar
├── requirements.txt         # Dependencias
├── README.md               # Este archivo
└── docs/                   # Documentación adicional
    ├── ARQUITECTURA.md
    └── EJEMPLOS.md
```

---

## 🔧 Configuración Avanzada

### Parámetros del Modelo

Puedes personalizar el comportamiento modificando el `prompt_robotico`:

```python
prompt_robotico = f"""
    Actúa como un sistema de visión robótica (Embodied VLA).
    Analiza la imagen actual y responde a la siguiente consulta: "{pregunta}"
    
    Instrucciones de salida:
    1. Proporciona coordenadas relativas en formato [ymin, xmin, ymax, xmax] (escala 0-1000).
    2. Estima distancias relativas (primer plano, medio, fondo).
    3. Responde con terminología técnica de navegación y robótica.
    4. [ADICIONA TUS REQUISITOS AQUÍ]
"""
```

### Variables de Entorno

| Variable | Descripción | Requerida |
|----------|-------------|-----------|
| `GEMINI_API_KEY` | API Key de Google Gemini | ✅ Sí |

---

## ⚡ Casos de Uso

🏭 **Robótica Industrial**
- Localización de piezas en líneas de producción
- Navegación autónoma en almacenes
- Mapeo de espacios y detección de anomalías

🏥 **Asistencia Robótica**
- Robots asistenciales en hospitales
- Detección de caídas y monitoreo de espacios
- Navegación en entornos complejos

🔬 **Investigación Académica**
- Prototipado de sistemas VLA
- Análisis de razonamiento espacial en IA
- Benchmarking de modelos multimodales

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios significativos:

1. Fork el repositorio
2. Crea una rama (`git checkout -b feature/MiFeature`)
3. Commit tus cambios (`git commit -am 'Agrega MiFeature'`)
4. Push a la rama (`git push origin feature/MiFeature`)
5. Abre un Pull Request

---

## 📝 Licencia

Este proyecto está bajo licencia **MIT**. Ver el archivo `LICENSE` para más detalles.

---

## 🐛 Troubleshooting

### Error: "Sensor óptico no detectado"
```bash
# Verifica que tu webcam esté conectada
# En Linux: ls /dev/video*
# En Windows: Comprueba en Configuración > Dispositivos > Cámara
```

### Error: "No se encontró la GEMINI_API_KEY"
```bash
# Asegúrate de que el archivo .env existe y contiene:
# GEMINI_API_KEY=tu_clave_aqui

# Verifica que está en la raíz del proyecto
cat .env
```

### Latencia Alta
- Reduce la resolución de captura en `capturar_entorno()`
- Implementa caché de imágenes
- Ejecuta en GPU si está disponible

---

## 📚 Recursos

- 📖 [Documentación de Google Gemini](https://ai.google.dev/)
- 🎥 [OpenCV Python Tutorials](https://docs.opencv.org/master/d9/df8/tutorial_root.html)
- 🤖 [Vision-Language-Action Models](https://arxiv.org/abs/2401.00529)
- 🧠 [Embodied AI Research](https://embodied-ai.org/)

---

## ✉️ Contacto & Soporte

- **Issues**: Reporta bugs en la sección [Issues](https://github.com/tu-usuario/vla-robotics-agent/issues)
- **Discussions**: Plantea ideas en [Discussions](https://github.com/tu-usuario/vla-robotics-agent/discussions)
- **Email**: contacto@tudominio.com

---

## 📊 Estado del Proyecto

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Python](https://img.shields.io/badge/python-3.9+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/badge/version-1.0.0-blue)

---

**Creado con 🤖 y ❤️ para avanzar en Robótica e IA**

*Last Updated: 2026 | Engineered for Spatial Reasoning*
