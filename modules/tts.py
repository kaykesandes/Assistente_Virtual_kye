# Módulo de Text to Speech
import pyttsx3
import subprocess
import os

def speak(texto):
    """Converte texto em fala com fallback para diferentes sistemas"""
    try:
        # Tentativa 1: Usar pyttsx3
        engine = pyttsx3.init()
        
        # Configurar voz se disponível
        voices = engine.getProperty('voices')
        if voices:
            # Procurar por uma voz em português ou usar a primeira disponível
            for voice in voices:
                if 'pt' in voice.id.lower() or 'brazil' in voice.id.lower():
                    engine.setProperty('voice', voice.id)
                    break
            else:
                # Se não encontrar voz em português, usar a primeira
                engine.setProperty('voice', voices[0].id)
        
        # Configurar velocidade e volume
        engine.setProperty('rate', 150)  # Velocidade da fala
        engine.setProperty('volume', 0.9)  # Volume
        
        engine.say(texto)
        engine.runAndWait()
        
    except Exception as e1:
        print(f"Erro com pyttsx3: {e1}")
        try:
            # Tentativa 2: Usar espeak diretamente
            subprocess.run(['espeak', '-s', '150', '-v', 'pt-br', texto], 
                         check=True, capture_output=True)
        except Exception as e2:
            print(f"Erro com espeak: {e2}")
            try:
                # Tentativa 3: Usar espeak em inglês
                subprocess.run(['espeak', '-s', '150', texto], 
                             check=True, capture_output=True)
            except Exception as e3:
                print(f"Erro com espeak em inglês: {e3}")
                # Fallback: apenas imprimir o texto
                print(f"[FALA]: {texto}")

def speak_simple(texto):
    """Versão simplificada que apenas imprime o texto se TTS falhar"""
    try:
        speak(texto)
    except Exception:
        print(f"[ASSISTENTE FALA]: {texto}")
