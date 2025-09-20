# Módulo de comandos otimizado para WSL
import webbrowser
import subprocess
import os
from datetime import datetime
from modules.tts_wsl import speak

def abrir_url_wsl(url, descricao="página"):
    """Abre URL no navegador do Windows via WSL"""
    try:
        # Método 1: Usar explorer.exe para abrir URLs no Windows
        subprocess.run(['explorer.exe', url], check=True)
        speak(f"Abrindo {descricao} no navegador do Windows.")
        print(f"✅ {descricao.capitalize()} aberta: {url}")
    except:
        try:
            # Método 2: Usar cmd.exe com start
            subprocess.run(['cmd.exe', '/c', 'start', url], check=True)
            speak(f"Abrindo {descricao} no navegador.")
            print(f"✅ {descricao.capitalize()} aberta: {url}")
        except:
            try:
                # Método 3: Python webbrowser (pode não funcionar no WSL)
                webbrowser.open(url)
                speak(f"Tentando abrir {descricao}.")
                print(f"⚠️ Tentativa de abrir: {url}")
            except:
                # Método 4: Exibir URL para cópia manual
                speak(f"Não foi possível abrir automaticamente. Copie este link.")
                print(f"🔗 Link para copiar: {url}")
                print(f"📋 Copie e cole no seu navegador do Windows")

def abrir_wikipedia():
    """Abre a Wikipedia"""
    abrir_url_wsl("https://pt.wikipedia.org", "Wikipedia")

def abrir_youtube():
    """Abre o YouTube"""
    abrir_url_wsl("https://youtube.com", "YouTube")

def buscar_farmacia():
    """Busca farmácias próximas"""
    abrir_url_wsl("https://www.google.com/maps/search/farmacia+perto+de+mim/", "mapa de farmácias")

def que_horas_sao():
    """Informa a hora atual"""
    agora = datetime.now()
    hora_formatada = agora.strftime("%H:%M")
    mensagem = f"Agora são {hora_formatada}"
    speak(mensagem)
    print(f"🕐 Hora atual: {hora_formatada}")

def que_dia_e_hoje():
    """Informa a data atual"""
    hoje = datetime.now()
    
    # Nomes dos meses em português
    meses = {
        1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
        5: "maio", 6: "junho", 7: "julho", 8: "agosto",
        9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
    }
    
    # Nomes dos dias da semana
    dias_semana = {
        0: "segunda-feira", 1: "terça-feira", 2: "quarta-feira",
        3: "quinta-feira", 4: "sexta-feira", 5: "sábado", 6: "domingo"
    }
    
    dia_semana = dias_semana[hoje.weekday()]
    dia = hoje.day
    mes = meses[hoje.month]
    ano = hoje.year
    
    mensagem = f"Hoje é {dia_semana}, {dia} de {mes} de {ano}"
    speak(mensagem)
    print(f"📅 Data atual: {mensagem}")

def abrir_google():
    """Abre o Google"""
    abrir_url_wsl("https://google.com", "Google")

def buscar_no_google(termo_busca):
    """Busca um termo no Google"""
    if termo_busca:
        url = f"https://www.google.com/search?q={termo_busca.replace(' ', '+')}"
        abrir_url_wsl(url, f"busca por '{termo_busca}'")
    else:
        abrir_google()

def mostrar_ajuda():
    """Mostra os comandos disponíveis"""
    comandos = [
        "📖 'wikipedia' - Abre a Wikipedia",
        "🎥 'youtube' - Abre o YouTube", 
        "💊 'farmacia' - Busca farmácias próximas",
        "🕐 'que horas são' - Informa a hora atual",
        "📅 'que dia é hoje' - Informa a data atual",
        "🌐 'google' - Abre o Google",
        "🔍 'buscar [termo]' - Busca um termo no Google",
        "❓ 'ajuda' - Mostra esta lista de comandos",
        "👋 'sair' ou 'encerrar' - Encerra o assistente"
    ]
    
    print("\n" + "="*50)
    print("📋 COMANDOS DISPONÍVEIS NO WSL")
    print("="*50)
    for comando in comandos:
        print(f"  {comando}")
    print("="*50)
    
    speak("Lista de comandos exibida na tela.")

def mostrar_info_wsl():
    """Mostra informações específicas do WSL"""
    info = """
    ℹ️  INFORMAÇÕES IMPORTANTES - WSL:
    
    🔧 Este assistente está otimizado para WSL
    🌐 URLs são abertas no navegador do Windows
    🔊 TTS pode usar o Windows (se WSLg estiver ativo)
    📋 Se algo não abrir, o link será exibido para cópia
    
    💡 DICAS:
    • Use comandos simples como 'youtube', 'google'
    • Para buscas: 'buscar python tutorial'
    • Digite números (1-8) para comandos rápidos
    """
    print(info)
    speak("Informações sobre WSL exibidas na tela.")

def encerrar_assistente():
    """Encerra o assistente"""
    mensagem = "Encerrando o assistente. Até logo!"
    speak(mensagem)
    print(f"👋 {mensagem}")
    exit()

def process_command(texto):
    """Processa os comandos de voz/texto otimizado para WSL"""
    if not texto:
        return
    
    texto = texto.lower().strip()
    print(f"🔄 Processando comando: '{texto}'")
    
    # Comandos de navegação
    if "wikipedia" in texto:
        abrir_wikipedia()
    elif "youtube" in texto:
        abrir_youtube()
    elif "farmácia" in texto or "farmacia" in texto:
        buscar_farmacia()
    
    # Comandos de informação
    elif any(palavra in texto for palavra in ["que horas", "horas são", "horas", "hora"]):
        que_horas_sao()
    elif any(palavra in texto for palavra in ["que dia", "data", "hoje"]):
        que_dia_e_hoje()
    
    # Comandos de busca
    elif "buscar" in texto:
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
    elif "info" in texto or "informações" in texto or "wsl" in texto:
        mostrar_info_wsl()
    elif any(palavra in texto for palavra in ["sair", "encerrar", "tchau", "bye", "exit"]):
        encerrar_assistente()
    
    # Comando não reconhecido
    else:
        mensagem = "Comando não reconhecido. Digite 'ajuda' para ver os comandos disponíveis."
        speak(mensagem)
        print(f"❌ {mensagem}")
        
        # Sugerir comandos similares
        sugestoes = []
        if "youtube" in texto or "video" in texto:
            sugestoes.append("youtube")
        if "wiki" in texto or "pesquisa" in texto:
            sugestoes.append("wikipedia")
        if "tempo" in texto or "hora" in texto:
            sugestoes.append("que horas são")
        if "busca" in texto or "procurar" in texto:
            sugestoes.append("buscar [termo]")
            
        if sugestoes:
            print(f"💡 Talvez você queira: {', '.join(sugestoes)}")