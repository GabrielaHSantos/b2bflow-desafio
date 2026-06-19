import os 
import logging
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

def buscar_contatos(limite: int=3)->list[dict]:
    """
    busca os contatos cadastrados na tabela 'contatos' do Supabase e
    retorna uma lista com nome e telefone de cada contato
    """
    
    url=os.getenv("SUPABASE_URL")
    chave=os.getenv("SUPABASE_CHAVE")

    if not url or not chave:
        raise EnvironmentError("As variáveis de ambiente SUPABASE_URL e SUPABASE_CHAVE devem estar definidas no .env.")
    
    cliente = create_client(url, chave)
    resposta = cliente.table("contatos").select("nome,telefone").limit(limite).execute()

    logger.info(f"{len(resposta.data)} contatos encontrados no banco")
    return resposta.data