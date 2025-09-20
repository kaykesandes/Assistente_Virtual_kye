# Módulo TTS otimizado para WSL
import pyttsx3
import subprocess
import os

def speak_wsl(texto):
    """Versão otimizada do TTS para WSL"""
    try:
        # Tentar usar eSpeak primeiro (mais confiável no WSL)
        subprocess.run(['espeak', '-s', '150', '-v', 'pt-br', texto], 
                     check=True, capture_output=True, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        try:
            # Fallback para espeak em inglês
            subprocess.run(['espeak', '-s', '150', texto], 
                         check=True, capture_output=True, stderr=subprocess.DEVNULL)
        except:
            # Se WSLg estiver disponível, tentar usar Windows TTS
            try:
                # Comando para usar TTS do Windows via WSL
                windows_tts_cmd = f'powershell.exe "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{texto}\')"'
                subprocess.run(windows_tts_cmd, shell=True, capture_output=True, timeout=5)
            except:
                # Última opção: apenas imprimir
                print(f"🔊 [FALA]: {texto}")

def speak_silent(texto):
    """Versão silenciosa que apenas exibe o texto"""
    print(f"🔊 [ASSISTENTE]: {texto}")

def speak(texto):
    """Função principal de TTS com detecção de ambiente"""
    try:
        # Verificar se está no WSL
        with open('/proc/version', 'r') as f:
            version = f.read().lower()
            if 'microsoft' in version or 'wsl' in version:
                # No WSL, usar versão otimizada
                speak_wsl(texto)
                return
    except:
        pass
    
    # Comportamento padrão para outros sistemas
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        if voices:
            for voice in voices:
                if 'pt' in voice.id.lower() or 'brazil' in voice.id.lower():
                    engine.setProperty('voice', voice.id)
                    break
            else:
                engine.setProperty('voice', voices[0].id)
        
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.9)
        engine.say(texto)
        engine.runAndWait()
        
    except Exception as e:
        # Fallback final
        speak_silent(texto)