# Versão alternativa do módulo Speech to Text usando o microfone padrão do sistema
import speech_recognition as sr
import subprocess
import tempfile
import os

def speech_to_text_simple():
    """Versão simplificada usando apenas SpeechRecognition sem PyAudio"""
    recognizer = sr.Recognizer()
    
    # Usando o microfone padrão
    try:
        with sr.Microphone() as source:
            print("Ajustando para ruído ambiente...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Ouvindo... Fale agora!")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        
        print("Processando...")
        texto = recognizer.recognize_google(audio, language='pt-BR')
        return texto.lower()
    
    except sr.WaitTimeoutError:
        print("Tempo limite esgotado. Nenhuma fala detectada.")
        return None
    except sr.UnknownValueError:
        print("Não consegui entender o que foi dito.")
        return None
    except sr.RequestError as e:
        print(f"Erro no serviço de reconhecimento: {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None

def speech_to_text_from_file(audio_file_path):
    """Reconhece fala de um arquivo de áudio"""
    recognizer = sr.Recognizer()
    
    try:
        with sr.AudioFile(audio_file_path) as source:
            audio = recognizer.record(source)
        
        texto = recognizer.recognize_google(audio, language='pt-BR')
        return texto.lower()
    
    except sr.UnknownValueError:
        print("Não consegui entender o áudio do arquivo.")
        return None
    except sr.RequestError as e:
        print(f"Erro no serviço de reconhecimento: {e}")
        return None
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")
        return None

# Função principal que tenta diferentes métodos
def speech_to_text():
    """Função principal de speech to text com fallback"""
    try:
        return speech_to_text_simple()
    except Exception as e:
        print(f"Erro no reconhecimento de voz: {e}")
        print("Você pode digitar o comando manualmente:")
        return input("Digite seu comando: ").lower()