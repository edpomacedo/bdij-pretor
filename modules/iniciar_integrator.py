# Pretor/1.2 - @edpomacedo - modules/iniciar_integrator.py
from config import MEDIAWIKI_CONFIG, OAUTH_CONFIG
from wikibaseintegrator import WikibaseIntegrator, wbi_login
from wikibaseintegrator.wbi_config import config 

# Configuração do WikibaseIntegrator
config['MEDIAWIKI_API_URL'] = MEDIAWIKI_CONFIG['api_url']
config['USER_AGENT'] = MEDIAWIKI_CONFIG['user_agent']

# Criação de objeto de login com OAuth1
login = wbi_login.OAuth1(
    consumer_token=OAUTH_CONFIG['consumer_key'],
    consumer_secret=OAUTH_CONFIG['consumer_secret'],
    access_token=OAUTH_CONFIG['access_token'],
    access_secret=OAUTH_CONFIG['access_token_secret']
)

# Inicialização do WikibaseIntegrator com login
wbi = WikibaseIntegrator(login=login)