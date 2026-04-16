import os
import cv2
import time
from PIL import Image
from dotenv import load_dotenv
from google import genai

# =================================================================
# CONFIGURACIÓN DEL AGENTE ROBÓTICO (EMBODIED VLA)
# =================================================================

# Cargar variables de entorno desde el archivo .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("❌ Error: No se encontró la GEMINI_API_KEY en el archivo .env")
    exit()

client = genai.Client(api_key=API_KEY)
MODEL_ID = "models/gemini-robotics-er-1.5-preview" 

def capturar_entorno():
    """Toma una fotografía instantánea para analizar el estado del espacio."""
    print("\n📸 [Sensor Óptico] Capturando escena...")
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("❌ Error: Sensor óptico no detectado.")
        return None
        
    time.sleep(1) # Calibración de luz
    ret, frame = cap.read()
    cap.release()
    
    if not ret: 
        return None
        
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return Image.fromarray(frame_rgb)

def consultar_agente_espacial(imagen, pregunta):
    """Envía la imagen y la consulta al modelo VLA para extraer coordenadas."""
    
    prompt_robotico = f"""
    Actúa como un sistema de visión robótica (Embodied VLA).
    Analiza la imagen actual y responde a la siguiente consulta: "{pregunta}"
    
    Instrucciones de salida:
    1. Proporciona coordenadas relativas en formato [ymin, xmin, ymax, xmax] (escala 0-1000).
    2. Estima distancias relativas (primer plano, medio, fondo).
    3. Responde con terminología técnica de navegación y robótica.
    """
    
    try:
        print("🧠 [Procesador Neuronal] Razonando geometría y contexto...")
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=[prompt_robotico, imagen]
        )
        return response.text
    except Exception as e:
        return f"⚠️ Error en la comunicación con el modelo: {e}"

def iniciar_terminal():
    print("="*65)
    print("🤖 TERMINAL DE CONTROL VLA (RAZONAMIENTO ESPACIAL)")
    print(f"Modelo: {MODEL_ID}")
    print("Escribe 'salir' para finalizar.")
    print("="*65)

    while True:
        pregunta = input("\n🎙️ Operador (Comando): ")
        
        if pregunta.lower() in ['salir', 'exit', 'quit']:
            print("👋 Sistema terminado.")
            break
            
        if not pregunta.strip():
            continue

        imagen = capturar_entorno()
        
        if imagen:
            respuesta = consultar_agente_espacial(imagen, pregunta)
            print(f"\n🦾 VLA Agent Responde:\n{respuesta}")
            print("-" * 65)

if __name__ == "__main__":
    iniciar_terminal()