# 🏗️ Arquitectura del Sistema VLA

## Descripción General

El **Agente Robótico VLA (Vision-Language-Action)** es un sistema que integra visión por computadora con procesamiento de lenguaje natural para realizar razonamiento espacial en tiempo real.

---

## Flujo de Procesamiento

```
┌─────────────────────────────────────────────────────────┐
│        TERMINAL INTERACTIVA (stdin/stdout)              │
│                                                         │
│  🎙️ Operador escribe comando natural:                  │
│     "¿Dónde está la puerta?"                            │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│     MÓDULO DE CAPTURA (capturar_entorno)                │
│                                                         │
│  📸 OpenCV + Webcam                                     │
│  - Inicializa captura (cv2.VideoCapture(0))            │
│  - Espera 1s de calibración                            │
│  - Captura frame en BGR                                 │
│  - Convierte a RGB (PIL)                               │
│  - Retorna objeto Image                                 │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│  MÓDULO DE CONSULTA VLA (consultar_agente_espacial)    │
│                                                         │
│  🧠 Google Gemini Robotics ER 1.6                       │
│  - Envía: prompt robótico + imagen                     │
│  - Procesa: razonamiento geométrico                    │
│  - Extrae: coordenadas, distancias, orientaciones      │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│         MÓDULO DE RESPUESTA (stdout)                    │
│                                                         │
│  🦾 Análisis Espacial                                   │
│  - Coordenadas relativas: [ymin, xmin, ymax, xmax]     │
│  - Distancias: primer plano / medio / fondo             │
│  - Orientaciones y ángulos                              │
└─────────────────────────────────────────────────────────┘
```

---

## Componentes Principales

### 1. **Sensor Óptico (OpenCV)**
```python
def capturar_entorno():
    cap = cv2.VideoCapture(0)  # Webcam
    frame = cap.read()          # Captura imagen
    frame_rgb = cv2.cvtColor()  # Conversión color
    return Image.fromarray()    # Retorna PIL Image
```

**Responsabilidades:**
- Inicializar dispositivo de captura
- Calibración de luz (delay 1s)
- Conversión de formato BGR → RGB
- Manejo de errores si la webcam no está disponible

**Salida:** Objeto `PIL.Image` con la escena actual

---

### 2. **Motor de Razonamiento (Gemini API)**
```python
def consultar_agente_espacial(imagen, pregunta):
    prompt_robotico = f"""
        Actúa como sistema VLA...
        Analiza: {pregunta}
        Proporciona: coordenadas, distancias, terminología técnica
    """
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=[prompt_robotico, imagen]
    )
    return response.text
```

**Responsabilidades:**
- Construir prompt técnico robótico
- Enviar imagen + texto al modelo
- Manejar latencia de respuesta
- Capturar errores de API

**Salida:** Análisis espacial en texto

---

### 3. **Terminal de Control (REPL)**
```python
def iniciar_terminal():
    while True:
        pregunta = input("\n🎙️ Operador (Comando): ")
        
        if pregunta.lower() in ['salir', 'exit', 'quit']:
            break
        
        imagen = capturar_entorno()
        respuesta = consultar_agente_espacial(imagen, pregunta)
        print(f"\n🦾 VLA Agent Responde:\n{respuesta}")
```

**Responsabilidades:**
- Loop interactivo REPL
- Validación de entrada
- Orquestación de flujo
- Formateo de salida

---

## Parámetros de Configuración

### Variables de Entorno
| Variable | Valor | Propósito |
|----------|-------|----------|
| `GEMINI_API_KEY` | (tu clave) | Autenticación API |
| `MODEL_ID` | `gemini-robotics-er-1.6-preview` | Modelo a usar |

### Constantes en Código
```python
MODEL_ID = 'gemini-robotics-er-1.6-preview'  # Modelo VLA
CALIBRATION_TIME = 1  # segundos para luz
CAMERA_ID = 0  # ID de webcam por defecto
```

---

## Formato de Salida del Modelo

El modelo retorna análisis con este formato:

```
Coordenadas relativas: [ymin, xmin, ymax, xmax]
  - ymin: posición vertical mínima (0-1000)
  - xmin: posición horizontal mínima (0-1000)
  - ymax: posición vertical máxima (0-1000)
  - xmax: posición horizontal máxima (0-1000)

Distancia estimada: [Primer plano | Medio | Fondo]

Orientación: [ángulo en grados]

Terminología técnica: [conceptos de robótica/navegación]
```

### Ejemplo Real
```
Coordenadas relativas: [150, 300, 600, 850]
Distancia estimada: Primer plano (zona operativa cercana)
Orientación: 35° a la derecha del eje vertical
Análisis: Puerta rectangular, marco de aluminio,
          punto de agarre óptimo en manija (600, 750)
```

---

## Manejo de Errores

### Error: Webcam No Detectada
```python
if not cap.isOpened():
    print("❌ Error: Sensor óptico no detectado.")
    return None
```
→ **Solución:** Verificar permisos, conectar cámara, reintentar

### Error: API Key Inválida
```python
if not API_KEY:
    print("❌ Error: No se encontró la GEMINI_API_KEY en el archivo .env")
    exit()
```
→ **Solución:** Verificar `.env`, recrear clave en Google AI Studio

### Error: Fallo en API Gemini
```python
except Exception as e:
    return f"⚠️ Error en la comunicación con el modelo: {e}"
```
→ **Solución:** Verificar conexión, rate limits, credenciales

---

## Optimizaciones Posibles

### ⚡ Performance
- **Caché de imágenes:** Reutilizar capturas idénticas
- **Compresión:** Reducir resolución antes de enviar
- **Async:** Procesar múltiples consultas en paralelo
- **GPU:** Usar CUDA para OpenCV si está disponible

### 🎯 Precisión Espacial
- **Calibración de cámara:** Usar matriz de intrínsecos
- **Multi-frame:** Promediar coordenadas de N frames
- **Depth estimation:** Integrar sensor de profundidad (RealSense)
- **3D reconstruction:** Construir mapa 3D con múltiples vistas

### 🔧 Interfaz
- **Web UI:** Reemplazar REPL con interfaz web (FastAPI + React)
- **ROS integration:** Publicar en tópicos ROS para robots reales
- **Real-time streaming:** WebSocket para video en vivo
- **Voice input:** Agregar reconocimiento de voz (Google Speech-to-Text)

---

## Dependencias del Proyecto

```
google-genai>=0.5.0     # SDK Gemini (API + modelos)
opencv-python>=4.8.0    # Procesamiento de video
pillow>=10.0.0          # Manipulación de imágenes
python-dotenv>=1.0.0    # Gestión de variables de entorno
```

### Alternativas Consideradas
- **LangChain:** Para orquestación más compleja
- **ROS (Robot Operating System):** Para robots físicos
- **PyTorch Vision:** Para procesamiento offline
- **FastAPI:** Para interfaz web

---

## Seguridad

### ⚠️ Consideraciones Importantes
1. **Nunca** comitear `.env` con credenciales reales
2. **Usar** `.env.example` como plantilla pública
3. **Validar** entrada del usuario (injection attacks)
4. **Rate limit** las llamadas a API Gemini
5. **Monitorear** uso de tokens/costos

### Implementación de Seguridad
```python
# ✅ CORRECTO
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# ❌ INCORRECTO
API_KEY = "sk-1234567890abcdef"  # ¡NUNCA hardcodear!
```

---

## Roadmap Futuro

### v1.1 - Mejorado
- [ ] Persistencia de análisis (base datos SQLite)
- [ ] Historial de comandos
- [ ] Exportar reportes (PDF)

### v2.0 - Integración Robótica
- [ ] Control de brazos robóticos
- [ ] Publicación en ROS topics
- [ ] Feedback de actuadores

### v3.0 - Multimodal Avanzado
- [ ] Integración con LiDAR
- [ ] Construcción de mapas 3D
- [ ] Planificación de trayectorias

---

## Referencias Técnicas

- 📄 [Vision-Language-Action Models](https://arxiv.org/abs/2401.00529)
- 🎥 [OpenCV Documentation](https://docs.opencv.org/)
- 🧠 [Gemini API Guide](https://ai.google.dev/gemini-api/docs)
- 🤖 [Embodied AI Lab](https://embodied-ai.org/)

---

**Última Actualización:** Mayo 2026  
**Mantenedor:** JuanPa  
**Estado:** Activo y en desarrollo
