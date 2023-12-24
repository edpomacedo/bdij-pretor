# BDIJ-PRETOR/1.0

## Estrutura

```bash
├── configurations/
│   ├── mediawiki.yaml
│   ├── oauth.yaml
│   ├── sparql.yaml
│   ├── wikibase.yaml
├── documentos/
│   ├── legal_docs/
│   ├── wiki_content/
├── modules/
│   ├── api_handler.py
│   ├── data_parser.py
├── operations/
│   ├── page_management.py
│   ├── uploader.py
├── snippets/
│   ├── sparql_queries/
│   │   ├── assunto.rq
│   │   ├── classe.rq
│   │   ├── documento.rq
│   │   ├── movimento.rq
├── tests/
│   ├── authentication.py
├── utils/
│   ├── error_handler.py
│   ├── logger.py
├── venv/
├── .gitignore
├── config.py
├── main.py
```

## Bibliotecas

```bash
pip install PyYAML requests requests_oauthlib
```