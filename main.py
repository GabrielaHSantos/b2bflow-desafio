import logging
from cliente_supabase import buscar_contatos
from cliente_zapi import enviar_mensagem

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

def main():

    logger.info("Iniciando o processo de envio de mensagens...")

    try:
        contatos = buscar_contatos(limite=3)
    except Exception as error:
        logger.error(f"Erro ao buscar contatos: {error}")
        return
    
    if not contatos: 
        logger.info("Nenhum contato encontrado.")
        return
    for contato in contatos:
        nome = contato["nome"]
        telefone = contato["telefone"]
        mensagem = f"Olá {nome}, tudo bem com você?"

        try:
            resultado = enviar_mensagem(telefone, mensagem)
            logger.info(f"Mensagem enviada para {nome} ({telefone}): {resultado}")
        except Exception as error:
            logger.error(f"Erro ao enviar mensagem para {nome} ({telefone}): {error}")

    logger.info("Processo de envio de mensagens concluído.")

if __name__ == "__main__":
    main()