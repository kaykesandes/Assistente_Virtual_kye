# Assistente Virtual Kye
# Ponto de entrada do assistente virtual

from modules import tts, stt, commands

def main():
    print("Bem-vindo ao Assistente Virtual Kye!")
    while True:
        print("Diga um comando...")
        texto = stt.speech_to_text()
        if texto:
            print(f"Você disse: {texto}")
            commands.process_command(texto)
        else:
            print("Não entendi. Tente novamente.")

if __name__ == "__main__":
    main()
