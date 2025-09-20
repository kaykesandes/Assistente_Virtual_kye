"""Integração com Azure OpenAI (GPT) para o Assistente Kye.

LEMBRETE IMPORTANTE: Nunca versionar o arquivo .env com chaves reais.
Crie um .env.example e adicione .env ao .gitignore.

Variáveis esperadas:
  AZURE_OPENAI_API_KEY
  AZURE_OPENAI_ENDPOINT  (ex: https://NOME.openai.azure.com)
  AZURE_OPENAI_API_VERSION (ex: 2024-10-01-preview ou mais recente)
  AZURE_OPENAI_DEPLOYMENT_NAME (nome do deployment do modelo, ex: gpt-4o-mini)

Dependência: azure-ai-openai (SDK novo unificado). Se não disponível, fazemos fallback para requests.
"""
from __future__ import annotations

import os
import json
from typing import List, Dict, Optional

try:  # Tenta importar SDK oficial
    from azure.ai.openai import OpenAIClient  # type: ignore
    from azure.core.credentials import AzureKeyCredential  # type: ignore
    _HAS_AZURE_SDK = True
except Exception:  # pragma: no cover
    _HAS_AZURE_SDK = False
    try:
        import requests  # type: ignore
    except Exception:
        requests = None  # type: ignore


class AzureLLMConfigError(RuntimeError):
    pass


def _load_env(var: str, required: bool = True) -> Optional[str]:
    value = os.environ.get(var)
    if required and (value is None or not value.strip()):
        raise AzureLLMConfigError(f"Variável de ambiente obrigatória ausente: {var}")
    return value


def get_client():
    """Retorna cliente do Azure ou None se não disponível."""
    if not _HAS_AZURE_SDK:
        return None
    endpoint = _load_env("AZURE_OPENAI_ENDPOINT")
    api_key = _load_env("AZURE_OPENAI_API_KEY")
    return OpenAIClient(endpoint=endpoint, credential=AzureKeyCredential(api_key))


def chat_completion(messages: List[Dict[str, str]],
                    temperature: float = 0.7,
                    max_tokens: int = 512) -> str:
    """Envia mensagens para o Azure OpenAI e retorna a resposta de texto.

    messages: lista no formato [{'role': 'user'|'system'|'assistant', 'content': '...'}]
    """
    deployment = _load_env("AZURE_OPENAI_DEPLOYMENT_NAME")
    api_version = _load_env("AZURE_OPENAI_API_VERSION")
    endpoint = _load_env("AZURE_OPENAI_ENDPOINT")
    api_key = _load_env("AZURE_OPENAI_API_KEY")

    # Caso SDK disponível
    if _HAS_AZURE_SDK:
        client = get_client()
        try:
            result = client.chat_completions.create(
                model=deployment,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            # Compat SDK recente: choices[0].message.content
            if result.choices:
                return result.choices[0].message.content.strip()
            return "(Sem resposta do modelo)"
        except Exception as e:  # pragma: no cover
            return f"[ERRO LLM SDK] {e}"

    # Fallback Requests (rota legacy /openai/deployments/{deployment}/chat/completions)
    if requests is None:
        return "[Integração Azure desativada - instale 'requests' ou 'azure-ai-openai']"
    url = f"{endpoint.rstrip('/')}/openai/deployments/{deployment}/chat/completions?api-version={api_version}"
    headers = {"Content-Type": "application/json", "api-key": api_key}
    payload = {"messages": messages, "temperature": temperature, "max_tokens": max_tokens}
    try:
        resp = requests.post(url, headers=headers, data=json.dumps(payload), timeout=60)
        if resp.status_code >= 400:
            return f"[ERRO LLM HTTP {resp.status_code}] {resp.text}"
        data = resp.json()
        choices = data.get("choices", [])
        if choices:
            msg = choices[0].get("message", {}).get("content", "").strip()
            return msg or "(Resposta vazia)"
        return "(Sem resposta do modelo)"
    except Exception as e:  # pragma: no cover
        return f"[ERRO LLM REQUEST] {e}"


def perguntar_ao_modelo(pergunta: str, contexto: str | None = None) -> str:
    """Interface simples para uso nos comandos.
    contexto opcional vira mensagem 'system'.
    """
    msgs: List[Dict[str, str]] = []
    if contexto:
        msgs.append({"role": "system", "content": contexto})
    msgs.append({"role": "user", "content": pergunta})
    return chat_completion(msgs)


if __name__ == "__main__":  # Execução manual rápida
    try:
        print(perguntar_ao_modelo("Explique rapidamente o que é Python."))
    except AzureLLMConfigError as e:
        print("Config incompleta:", e)