# Pretor/1.3 - @edpomacedo - modules/criar_tabela_wikitext.py
def criar_tabela_wikitext(dados_tabela, cabeçalhos, contagem_resultados):
    tabela_wikitext = f"{{| class=\"wikitable sortable\" style=\"width:100%;\"\n|+ Número de resultados: {contagem_resultados}\n|-"
    tabela_wikitext += f"\n! {' !! '.join(cabeçalhos)}\n"

    for linha in dados_tabela:
        tabela_wikitext += "|-\n"
        tabela_wikitext += "| "
        tabela_wikitext += " || ".join(str(linha.get(coluna, '')) for coluna in cabeçalhos)
        tabela_wikitext += "\n"

    tabela_wikitext += "|}\n"
    return tabela_wikitext