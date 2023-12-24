# Pretor/1.0 - @edpomacedo - main.py
import sys
sys.path.append("modules")
sys.path.append("operations")
sys.path.append("utils")

from uploader import processar_arquivos
from utils.logger import logger  # Importando o logger

def main():
    processar_arquivos()

if __name__ == "__main__":
    main()
