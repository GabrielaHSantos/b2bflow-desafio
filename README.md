# b2bflow-desafio

Desafio técnico para Estágio em Desenvolvimento Python na b2bflow.

A aplicação busca contatos cadastrados no Supabase e envia automaticamente
uma mensagem personalizada via WhatsApp para cada um, utilizando a Z-API.

## Setup da tabela

No SQL Editor do Supabase, execute:

```sql
CREATE TABLE contatos (
    id        BIGSERIAL PRIMARY KEY,
    nome      TEXT NOT NULL,
    telefone  TEXT NOT NULL
);
```

Para popular a tabela rapidamente com dados de teste, execute:

```
INSERT INTO contatos (nome, telefone) VALUES 
('Juliano', '5521999999999');
```


> **Obs.:** O campo `telefone` deve seguir o formato `5521999999999` (código do país + DDD + número).

## Variáveis de ambiente

Copie `.env.exemplo` para `.env` e preencha com suas credenciais:

```
SUPABASE_URL=https://SEU_PROJETO.supabase.co
SUPABASE_CHAVE=sua_anon_key
ZAPI_ID_INSTANCIA=seu_id_instancia
ZAPI_TOKEN=seu_token_instancia
```

## Como rodar

1. Crie e ative um ambiente virtual:

   - **Windows:** `python -m venv .venv` e `.venv\Scripts\activate`
   - **Linux/Mac:** `python3 -m venv .venv` e `source .venv/bin/activate`


2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute:

```bash
python main.py
```

## Evidências

### Mensagem recebida no WhatsApp
![Mensagem enviada](evidencias/mensagem_enviada.png)