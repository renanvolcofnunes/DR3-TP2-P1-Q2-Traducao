# Parte 1 - Q2 - Helsinki-NLP

## Descricao
API de traducao do ingles para o frances.

## Requisitos
Python 3.14 e dependencias listadas em requirements.txt.

## Instalacao
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    python -m pip install -r requirements.txt

## Execucao
    python -m uvicorn main:app --reload --port 8001

## Documentacao da API
http://127.0.0.1:8001/docs

## Endpoint
POST /translate

## Exemplo de requisicao
    {"text":"Hello, how are you today?"}

## Observacoes
Modelo Helsinki-NLP/opus-mt-en-fr executado localmente.
