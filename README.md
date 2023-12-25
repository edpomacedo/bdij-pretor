# BDIJ-PRETOR/1.2

![doi:10.5281/zenodo.10429686](https://zenodo.org/badge/DOI/10.5281/zenodo.10429686.svg)

O PRETOR é um projeto desenvolvido para automatizar a postagem e gerenciamento de conteúdo na **Base de Dados de Institutos Jurídicos**, utilizando a API MediaWiki.

## Funcionalidades

Na atual versão, o PRETOR oferece as seguintes funcionalidades:

1. **Processar Ementas:**
   - Processa arquivos de texto (.txt) contendo ementas da jurisprudência.
   - Realiza o registro das ementas na BDIJ.

2. **Processar Informativos:**
   - Processa arquivos de texto (.txt) contendo informações do inteiro teor de julgados publicados em informativos.
   - Realiza o registro do texto dos informativos por instituto jurídico na BDIJ.

3. **Criar Artigos de Legislação:**
   - Processa um intervalo entre 'Art. x' e 'Art. y' de uma dada norma jurídica.
   - Realiza o registro dos dispositivos informados como Lexemas e os vincula a uma norma jurídica segundo o QID.

## Estrutura

O projeto PRETOR é estruturado em módulos para melhor organização e reutilização de código.

A estrutura geral pode ser assim entendida:

- `documents/`: Contém subdiretórios para distribuição dos arquivos a serem processados;
- `modules/`: Contém módulos específicos para funções individuais;
- `operations/`: Contém operações específicas do sistema, isto é, rotinas a serem executadas;
- `snippets/`: Contém fragmentos de código que potencialmente serão reutilizados;
- `tests/`: Contém comandos para testar a operacionalidade do sistema;
- `utils/`: Contém utilitários gerais, como a configuração de logs etc.

## Configurações

Antes de utilizar o PRETOR, é necessário configurar as credenciais OAuth no arquivo de configuração (`config.py`).

Certifique-se de fornecer as informações corretas para permitir a autenticação segura.

### Como Usar

1. Clone o repositório para o seu ambiente local.
2. Configure as credenciais OAuth no arquivo `config.py`.
3. Execute o script principal (`main.py`) para selecionar a operação desejada.

## Requisitos

Certifique-se de ter as dependências necessárias instaladas.

Utilize o seguinte comando para instalar as dependências:

```bash
pip install -r requirements.txt
```

## Contribuições

Contribuições são bem-vindas!

Sinta-se à vontade para abrir problemas, enviar solicitações de recebimento ou propor melhorias no código.

1. Faça um fork do projeto
2. Crie uma branch para a sua feature (`git checkout -b feature/nova-feature`)
3. Faça commit das suas alterações (`git commit -am 'Adicione uma nova feature'`)
4. Faça push para a branch (`git push origin feature/nova-feature`)
5. Crie um novo Pull Request

## Licença

Copyright 2023 EDPO AUGUSTO FERREIRA MACEDO

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.