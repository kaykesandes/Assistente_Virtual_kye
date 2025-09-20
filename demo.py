# Demo do Assistente Virtual Kye - Apenas para demonstração
import sys
sys.path.append('/home/kayke/project/Python/DataScience/Assistente_Virtual_kye')

from modules import tts
from modules.commands_extended import process_command, mostrar_ajuda

def demo():
    """Demonstração das funcionalidades do assistente"""
    print("🎤 DEMO - ASSISTENTE VIRTUAL KYE 🎤")
    print("="*50)
    
    # Banner inicial
    banner = """
    ╔══════════════════════════════════════╗
    ║        ASSISTENTE VIRTUAL KYE        ║
    ║              Versão 1.0              ║
    ║         DEMO FUNCIONANDO! ✅         ║
    ╚══════════════════════════════════════╝
    """
    print(banner)
    
    # Teste de fala
    print("\n1️⃣ Testando módulo de Texto para Fala (TTS):")
    tts.speak("Olá! Eu sou o Assistente Virtual Kye!")
    
    # Mostrar comandos disponíveis
    print("\n2️⃣ Comandos disponíveis:")
    mostrar_ajuda()
    
    # Demonstrar alguns comandos
    print("\n3️⃣ Demonstrando comandos:")
    
    comandos_demo = [
        "que horas são",
        "que dia é hoje",
        "ajuda"
    ]
    
    for comando in comandos_demo:
        print(f"\n🗣️ Simulando comando: '{comando}'")
        process_command(comando)
        print("-" * 40)
    
    print("\n✅ DEMO CONCLUÍDA COM SUCESSO!")
    print("\nPara usar o assistente completo com reconhecimento de voz:")
    print("Execute: python main_improved.py")
    print("\nO assistente está funcionando perfeitamente! 🎉")

if __name__ == "__main__":
    demo()