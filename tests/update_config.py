# Pretor/1.0 - @edpomacedo - tests/update_config.py

import os
import yaml

# Obtém o diretório do script atual
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

CONFIG_FILE = 'config.py'
CONFIG_PATH = os.path.join(os.path.dirname(SCRIPT_DIR), CONFIG_FILE)  # Atualizado para a raiz do projeto
CONFIGURATIONS_PATH = os.path.join(SCRIPT_DIR, '..', 'configurations')

# Verifica se o arquivo config.py já existe e o importa
try:
    import config
except ImportError:
    config = None

def update_config():
    # Lista de arquivos YAML na pasta configurations
    yaml_files = [f for f in os.listdir(CONFIGURATIONS_PATH) if f.endswith('.yaml')]

    # Cria um dicionário para armazenar todas as configurações
    all_configurations = {}

    # Loop através dos arquivos YAML
    for yaml_file in yaml_files:
        yaml_file_path = os.path.join(CONFIGURATIONS_PATH, yaml_file)

        # Carregando dados do arquivo YAML
        with open(yaml_file_path, 'r') as file:
            yaml_data = yaml.safe_load(file)

        # Removendo a chave principal correspondente ao nome do arquivo
        config_name = yaml_file.split('.')[0].upper() + '_CONFIG'  # Extraindo o nome da configuração
        yaml_data = list(yaml_data.values())[0]

        # Atualizando configurações existentes com novos dados
        if config:
            config_section = getattr(config, config_name, {})  # Obtendo a configuração atual
            yaml_data.update({key: config_section.get(key, '') for key in config_section.keys()})

        # Adicionando dados ao dicionário geral de configurações
        all_configurations[config_name] = yaml_data

    # Atualizando o arquivo config.py
    with open(CONFIG_PATH, 'w') as config_file:
        config_file.write("# Pretor/1.0 - @edpomacedo - config.py\n\n")

        for config_name, config_data in all_configurations.items():
            config_file.write(f"{config_name} = {config_data}\n\n")

    print("Configurações atualizadas com sucesso.")

if __name__ == '__main__':
    update_config()
