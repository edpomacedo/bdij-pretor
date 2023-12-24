# Pretor/1.1 - @edpomacedo - modules/validar_credenciais.py
from requests_oauthlib import OAuth1
from config import OAUTH_CONFIG

def validar_credenciais():
    # Utilizando as credenciais do arquivo de configuração
    consumer_key = OAUTH_CONFIG['consumer_key']
    consumer_secret = OAUTH_CONFIG['consumer_secret']
    access_token = OAUTH_CONFIG['access_token']
    access_token_secret = OAUTH_CONFIG['access_token_secret']

    # Configuração do cliente OAuth1
    oauth = OAuth1(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret
    )

    return oauth