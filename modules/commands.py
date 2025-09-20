# Módulo de comandos automatizados
import webbrowser
from modules import tts

def process_command(texto):
    texto = texto.lower()
    if "wikipedia" in texto:
        tts.speak("Abrindo o Wikipedia.")
        webbrowser.open("https://wikipedia.org")
    elif "youtube" in texto:
        tts.speak("Abrindo o YouTube.")
        webbrowser.open("https://youtube.com")
    elif "farmácia" in texto:
        tts.speak("Procurando farmácias próximas no Google Maps.")
        webbrowser.open("https://www.google.com/maps/search/farmacia+perto+de+mim/")
    elif "sair" in texto or "encerrar" in texto:
        tts.speak("Encerrando o assistente. Até logo!")
        exit()
    else:
        tts.speak("Desculpe, não reconheci o comando.")
