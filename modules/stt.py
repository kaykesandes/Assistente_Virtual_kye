# Módulo de Speech to Text
import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ouvindo...")
        audio = recognizer.listen(source)
    try:
        texto = recognizer.recognize_google(audio, language='pt-BR')
        return texto
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return None
