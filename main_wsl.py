# Assistente Virtual Kye - Versão WSL
# Otimizado para Windows Subsystem for Linux

import sys
import os
from modules.tts_wsl import speak
from modules.commands_wsl import process_command, mostrar_info_wsl

def mostrar_banner():
    """Exibe o banner inicial do assistente"""
    banner = """
    ╔══════════════════════════════════════╗
    ║        ASSISTENTE VIRTUAL KYE        ║
    ║            Versão WSL 1.0            ║
    ║     Otimizado para entrada manual    ║
    ╠══════════════════════════════════════╣
    ║  Comandos disponíveis:               ║
    ║  • 'wikipedia' - Abre Wikipedia      ║
    ║  • 'youtube' - Abre YouTube          ║
    ║  • 'farmacia' - Busca farmácias      ║
    ║  • 'horas' - Informa hora            ║
    ║  • 'data' - Informa data             ║
    ║  • 'google' - Abre Google            ║
    ║  • 'buscar [termo]' - Busca no Google║
    ║  • 'ajuda' - Lista todos comandos    ║
    ║  • 'sair' - Encerra assistente      ║
    ╚══════════════════════════════════════╝
    """
    print(banner)

def detectar_ambiente():
    """Detecta se está rodando no WSL"""
    try:
        with open('/proc/version', 'r') as f:
            version = f.read().lower()
            if 'microsoft' in version or 'wsl' in version:
                return 'WSL'
        return 'Linux Nativo'
    except:
        return 'Desconhecido'

def comandos_interativos():
    """Modo interativo com sugestões de comandos"""
    comandos_exemplo = [
        "wikipedia",
        "youtube", 
        "farmacia",
        "que horas são",
        "que dia é hoje",
        "google",
        "buscar python",
        "ajuda"
    ]
    
    print("\n🎯 EXEMPLOS DE COMANDOS:")
    for i, cmd in enumerate(comandos_exemplo, 1):
        print(f"  {i}. {cmd}")
    
    print("\n💡 DICA: Digite o número ou o comando completo")
    return comandos_exemplo

def processar_entrada(entrada, comandos_exemplo):
    """Processa a entrada do usuário"""
    entrada = entrada.strip()
    
    # Se for um número, usa o comando correspondente
    if entrada.isdigit():
        try:
            idx = int(entrada) - 1
            if 0 <= idx < len(comandos_exemplo):
                comando = comandos_exemplo[idx]
                print(f"📝 Executando: '{comando}'")
                return comando
        except:
            pass
    
    return entrada

def main():
    """Função principal do assistente WSL"""
    try:
        mostrar_banner()
        
        # Detectar ambiente
        ambiente = detectar_ambiente()
        print(f"🖥️  Ambiente detectado: {ambiente}")
        
        if 'WSL' in ambiente:
            print("🔧 Modo WSL ativado - Usando entrada de texto")
            print("ℹ️  Para usar áudio, configure WSLg ou use Windows diretamente")
        
        # Mensagem inicial
        print(f"\n👋 Olá! Eu sou o Assistente Virtual Kye!")
        print("🎤 Como não há microfone disponível, use comandos de texto.")
        
        # Comandos de exemplo
        comandos_exemplo = comandos_interativos()
        
        # Mostrar informações do WSL
        mostrar_info_wsl()
        
        print("\n" + "="*60)
        print("🚀 ASSISTENTE PRONTO! Digite seus comandos abaixo:")
        print("="*60)
        
        # Loop principal
        contador = 0
        while True:
            try:
                contador += 1
                print(f"\n[{contador}] ", end="")
                entrada = input("💬 Digite seu comando (ou 'sair'): ").strip().lower()
                
                if not entrada:
                    print("❌ Comando vazio. Tente novamente.")
                    continue
                
                # Processar entrada
                comando_final = processar_entrada(entrada, comandos_exemplo)
                
                if comando_final:
                    print(f"⚡ Processando: '{comando_final}'")
                    process_command(comando_final)
                    print("✅ Comando executado!")
                else:
                    print("❌ Comando não reconhecido. Digite 'ajuda' para ver opções.")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Encerrando por interrupção do usuário...")
                break
            except EOFError:
                print("\n\n👋 Encerrando assistente...")
                break
            except Exception as e:
                print(f"❌ Erro durante execução: {e}")
                print("🔄 Tentando continuar...")
                
    except Exception as e:
        print(f"💥 Erro crítico: {e}")
    
    finally:
        print("\n" + "="*50)
        print("🏁 Assistente Virtual Kye encerrado.")
        print("💝 Obrigado por usar o assistente!")
        print("="*50)

if __name__ == "__main__":
    main()