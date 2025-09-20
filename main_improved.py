# Assistente Virtual Kye - Versão Melhorada
# Ponto de entrada do assistente virtual com mais funcionalidades

import sys
import os
from modules import tts
from modules.stt_alternative import speech_to_text
from modules.commands_extended import process_command

def mostrar_banner():
    """Exibe o banner inicial do assistente"""
    banner = """
    ╔══════════════════════════════════════╗
    ║        ASSISTENTE VIRTUAL KYE        ║
    ║              Versão 1.0              ║
    ╠══════════════════════════════════════╣
    ║  Comandos principais:                ║
    ║  • 'Wikipedia' - Abre Wikipedia      ║
    ║  • 'YouTube' - Abre YouTube          ║
    ║  • 'Farmácia' - Busca farmácias      ║
    ║  • 'Que horas são' - Informa hora    ║
    ║  • 'Ajuda' - Lista todos comandos    ║
    ║  • 'Sair' - Encerra assistente      ║
    ╚══════════════════════════════════════╝
    """
    print(banner)

def main():
    """Função principal do assistente"""
    try:
        mostrar_banner()
        
        # Mensagem de boas-vindas
        mensagem_inicial = "Olá! Eu sou o Assistente Virtual Kye. Como posso ajudá-lo hoje?"
        print(f"\n{mensagem_inicial}")
        tts.speak(mensagem_inicial)
        
        # Loop principal
        while True:
            try:
                print("\n" + "="*50)
                print("Aguardando comando... (ou diga 'sair' para encerrar)")
                print("="*50)
                
                # Captura o comando de voz
                texto = speech_to_text()
                
                if texto:
                    print(f"Você disse: '{texto}'")
                    process_command(texto)
                else:
                    print("Não consegui capturar nenhum comando. Tente novamente.")
                    
            except KeyboardInterrupt:
                print("\n\nEncerrando por interrupção do usuário...")
                tts.speak("Assistente encerrado pelo usuário. Até logo!")
                break
            except Exception as e:
                print(f"Erro durante execução: {e}")
                tts.speak("Ocorreu um erro. Tentando continuar...")
                
    except Exception as e:
        print(f"Erro crítico: {e}")
        tts.speak("Erro crítico detectado. Encerrando assistente.")
    
    finally:
        print("Assistente Virtual Kye encerrado.")

if __name__ == "__main__":
    main()