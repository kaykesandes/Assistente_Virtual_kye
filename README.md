# README - Assistente Virtual Kye

## Descrição
O Assistente Virtual Kye é um sistema completo de assistência virtual desenvolvido em Python, utilizando Processamento de Linguagem Natural (PLN). O sistema possui funcionalidades de conversão de texto para fala (TTS), fala para texto (STT) e execução de comandos automatizados por voz.

## Características Principais

### 1. Módulo Text-to-Speech (TTS)
- Converte texto em áudio usando a biblioteca `pyttsx3`
- Suporte para português brasileiro
- Configuração de voz ajustável

### 2. Módulo Speech-to-Text (STT)
- Reconhecimento de voz usando `SpeechRecognition`
- Suporte para português brasileiro
- Fallback para entrada manual em caso de erro
- Múltiplas opções de entrada (microfone, arquivo de áudio)

### 3. Comandos Automatizados
- **Wikipedia**: Abre a Wikipedia em português
- **YouTube**: Abre o YouTube
- **Farmácia**: Busca farmácias próximas no Google Maps
- **Hora**: Informa a hora atual
- **Data**: Informa a data atual
- **Google**: Abre o Google ou faz buscas específicas
- **Ajuda**: Lista todos os comandos disponíveis
- **Sair**: Encerra o assistente

## Estrutura do Projeto

```
Assistente_Virtual_kye/
├── main.py                 # Versão básica do assistente
├── main_improved.py        # Versão melhorada com mais funcionalidades
├── requirements.txt        # Dependências do projeto
├── README.md              # Este arquivo
└── modules/
    ├── __init__.py        # Arquivo de inicialização do pacote
    ├── tts.py             # Módulo Text-to-Speech
    ├── stt.py             # Módulo Speech-to-Text básico
    ├── stt_alternative.py # Módulo STT com mais opções
    ├── commands.py        # Comandos básicos
    └── commands_extended.py # Comandos expandidos
```

## Dependências

### Bibliotecas Python
- `pyttsx3` - Text-to-Speech
- `speechrecognition` - Speech-to-Text
- `pyaudio` - Interface de áudio

### Dependências do Sistema (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install -y portaudio19-dev python3-pyaudio
```

## Instalação

1. **Clone ou baixe o projeto**
2. **Configure o ambiente Python:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   # ou
   .venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências do sistema (Ubuntu/Debian):**
   ```bash
   sudo apt-get install -y portaudio19-dev python3-pyaudio
   ```

4. **Instale as dependências Python:**
   ```bash
   pip install -r requirements.txt
   ```

## Como Usar

### Versão Básica
```bash
python main.py
```

### Versão Melhorada (Recomendada)
```bash
python main_improved.py
```

## Comandos Disponíveis

| Comando | Descrição |
|---------|-----------|
| "Wikipedia" | Abre a Wikipedia |
| "YouTube" | Abre o YouTube |
| "Farmácia" | Busca farmácias próximas |
| "Que horas são" | Informa a hora atual |
| "Que dia é hoje" | Informa a data atual |
| "Google" | Abre o Google |
| "Buscar [termo]" | Busca um termo no Google |
| "Ajuda" | Mostra lista de comandos |
| "Sair" | Encerra o assistente |

## Exemplos de Uso

1. **Iniciar o assistente:**
   - Execute `python main_improved.py`
   - Aguarde a mensagem de boas-vindas

2. **Fazer uma busca:**
   - Diga: "Buscar receitas de bolo"
   - O assistente abrirá o Google com a busca

3. **Consultar informações:**
   - Diga: "Que horas são"
   - O assistente informará a hora atual

4. **Obter ajuda:**
   - Diga: "Ajuda"
   - Verá todos os comandos disponíveis

## Solução de Problemas

### Erro de instalação do PyAudio
Se encontrar erros ao instalar o PyAudio:

1. **Ubuntu/Debian:**
   ```bash
   sudo apt-get install portaudio19-dev python3-pyaudio
   ```

2. **CentOS/RHEL:**
   ```bash
   sudo yum install portaudio-devel
   ```

3. **macOS:**
   ```bash
   brew install portaudio
   ```

### Problemas de microfone
- Verifique se o microfone está funcionando
- Teste com: `arecord -l` (Linux) para listar dispositivos
- Configure as permissões de microfone se necessário

### Problemas de reconhecimento de voz
- Fale claramente e devagar
- Certifique-se de ter conexão com internet (usa Google Speech API)
- Em caso de falha, o sistema permite entrada manual

## Personalização

### Adicionar novos comandos
Edite o arquivo `modules/commands_extended.py` e adicione sua função:

```python
def meu_novo_comando():
    tts.speak("Executando meu novo comando")
    # Sua lógica aqui

# Adicione na função process_command:
elif "meu comando" in texto:
    meu_novo_comando()
```

### Configurar voz
Edite `modules/tts.py` para personalizar a voz:

```python
def speak(texto):
    engine = pyttsx3.init()
    
    # Configurações de voz
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Mudar índice
    engine.setProperty('rate', 150)  # Velocidade
    engine.setProperty('volume', 0.9)  # Volume
    
    engine.say(texto)
    engine.runAndWait()
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias:
1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Abra um Pull Request

## Licença

Este projeto é desenvolvido para fins educacionais e de aprendizado.

## Referências

- [Text-to-Speech DIO](https://github.com/diegobrunoDIO/Text-to-Speech-DIO)
- [Speech-to-Text DIO](https://github.com/diegobrunoDIO/Speech-to-text-ML-DIO)
- [Documentação SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [Documentação pyttsx3](https://pypi.org/project/pyttsx3/)