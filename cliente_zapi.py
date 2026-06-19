import os
import logging
import requests
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

def enviar_mensagem(telefone: str, mensagem: str)->dict:
    """
    envia uma mensagem de texto via WhatsApp usando a API da Z-API e 
    retorna o resultado da requisição em formato de dicionario. 
    """
    id_instancia = os.getenv("ZAPI_ID_INSTANCIA")
    token_instancia = os.getenv("ZAPI_TOKEN")

    if not id_instancia or not token_instancia:
        raise EnvironmentError("As variáveis de ambiente ZAPI_ID_INSTANCIA e ZAPI_TOKEN devem estar definidas no .env.")
    
    url = f"https://api.z-api.io/instances/{id_instancia}/token/{token_instancia}/send-text"


    resposta = requests.post(
        url,
        json={"phone": telefone, "message": mensagem},
        headers={"Content-Type": "application/json"},
        timeout=10,
    )
    resposta.raise_for_status()
    return resposta.json()
     

