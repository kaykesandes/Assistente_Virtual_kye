# Módulo de comandos expandido com mais funcionalidades
import webbrowser
import subprocess
import os
from datetime import datetime
from modules import tts
try:
    from modules.azure_llm import perguntar_ao_modelo, AzureLLMConfigError  # type: ignore
    _HAS_LLM = True
except Exception:
    _HAS_LLM = False

def abrir_wikipedia():
    """Abre a Wikipedia"""
    tts.speak("Abrindo o Wikipedia.")
    webbrowser.open("https://pt.wikipedia.org")

def abrir_youtube():
    """Abre o YouTube"""
    tts.speak("Abrindo o YouTube.")
    webbrowser.open("https://youtube.com")

def buscar_farmacia():
    """Busca farmácias próximas"""
    tts.speak("Procurando farmácias próximas no Google Maps.")
    webbrowser.open("https://www.google.com/maps/search/farmacia+perto+de+mim/")

def que_horas_sao():
    """Informa a hora atual"""
    agora = datetime.now()
    hora_formatada = agora.strftime("%H:%M")
    tts.speak(f"Agora são {hora_formatada}")
    print(f"Hora atual: {hora_formatada}")

def que_dia_e_hoje():
    """Informa a data atual"""
    hoje = datetime.now()
    data_formatada = hoje.strftime("%d de %B de %Y")
    tts.speak(f"Hoje é {data_formatada}")
    print(f"Data atual: {data_formatada}")

def abrir_google():
    """Abre o Google"""
    tts.speak("Abrindo o Google.")
    webbrowser.open("https://google.com")

def buscar_no_google(termo_busca):
    """Busca um termo no Google"""
    if termo_busca:
        tts.speak(f"Buscando {termo_busca} no Google.")
        webbrowser.open(f"https://www.google.com/search?q={termo_busca}")
    else:
        abrir_google()

def mostrar_ajuda():
    """Mostra os comandos disponíveis"""
    comandos = [
        "- 'Wikipedia' - Abre a Wikipedia",
        "- 'YouTube' - Abre o YouTube", 
        "- 'Farmácia' - Busca farmácias próximas",
        "- 'Que horas são' - Informa a hora atual",
        "- 'Que dia é hoje' - Informa a data atual",
        "- 'Google' - Abre o Google",
        "- 'Buscar [termo]' - Busca um termo no Google",
        "- 'Ajuda' - Mostra esta lista de comandos",
        "- 'Sair' ou 'Encerrar' - Encerra o assistente"
        "- 'Perguntar <sua pergunta>' - Pergunta ao modelo de IA"
    ]
    
    print("\n=== COMANDOS DISPONÍVEIS ===")
    for comando in comandos:
        print(comando)
    print("============================\n")
    
    tts.speak("Lista de comandos exibida na tela.")

def encerrar_assistente():
    """Encerra o assistente"""
    tts.speak("Encerrando o assistente. Até logo!")
    print("Assistente encerrado.")
    exit()

def process_command(texto):
    """Processa os comandos de voz"""
    if not texto:
        return
    
    texto = texto.lower().strip()
    print(f"Processando comando: '{texto}'")
    
    # Comandos de navegação
    if "wikipedia" in texto:
        abrir_wikipedia()
    elif "youtube" in texto:
        abrir_youtube()
    elif "farmácia" in texto or "farmacia" in texto:
        buscar_farmacia()
    
    # Comandos de informação
    elif "que horas" in texto or "horas são" in texto:
        que_horas_sao()
    elif "que dia" in texto or "data" in texto:
        que_dia_e_hoje()
    
    # Comandos de busca
    elif "buscar" in texto:
        # Extrai o termo de busca após a palavra "buscar"
        palavras = texto.split()
        if "buscar" in palavras:
            idx = palavras.index("buscar")
            if idx + 1 < len(palavras):
                termo = " ".join(palavras[idx + 1:])
                buscar_no_google(termo)
            else:
                abrir_google()
        else:
            abrir_google()
    elif "google" in texto:
        abrir_google()
    
    # Comandos de sistema
    elif "ajuda" in texto or "help" in texto or "comandos" in texto:
        mostrar_ajuda()
    elif "sair" in texto or "encerrar" in texto or "tchau" in texto or "bye" in texto:
        encerrar_assistente()
    elif texto.startswith("perguntar ") or texto.startswith("pergunta "):
        if not _HAS_LLM:
            aviso = "Recurso de IA não disponível. Instale dependências Azure e configure .env."
            tts.speak(aviso)
            print(aviso)
            return
        # Remove gatilho
        pergunta = texto.split(" ", 1)[1].strip()
        if not pergunta:
            tts.speak("Você precisa dizer a pergunta após 'perguntar'.")
            return
        tts.speak("Consultando modelo de linguagem...")
        try:
            resposta = perguntar_ao_modelo(pergunta, contexto="Você é o assistente Kye em português.")
            print("\n=== RESPOSTA IA ===")
            print(resposta)
            print("===================\n")
            tts.speak(resposta[:250])  # Limita fala
        except AzureLLMConfigError as e:
            msg = f"Configuração Azure incompleta: {e}";
            print(msg)
            tts.speak("Configuração Azure OpenAI ausente ou incompleta.")
        except Exception as e:
            print(f"Erro ao consultar modelo: {e}")
            tts.speak("Erro ao consultar o modelo.")
    
    # Comando não reconhecido
    else:
        mensagem = "Desculpe, não reconheci esse comando. Diga 'ajuda' para ver os comandos disponíveis."
        tts.speak(mensagem)
        print(mensagem)