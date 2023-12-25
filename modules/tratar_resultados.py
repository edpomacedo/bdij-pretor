# Pretor/1.3 - @edpomacedo - modules/tratar_resultados.py
def tratar_resultados(dados_tabela, tipo_resultado):
    for linha in dados_tabela:
        for chave in linha:
            if isinstance(linha[chave], str) and linha[chave].startswith("https://web.bdij.com.br/entity/"):
                entity_id = linha[chave][len("https://web.bdij.com.br/entity/"):]
                reference_id = entity_id.replace("-", "#")  # Substituir "-" por "#"

                if tipo_resultado == "Lexeme":
                    linha[chave] = f"[[Lexeme:{reference_id}|{entity_id}]]"
                elif tipo_resultado == "Item":
                    linha[chave] = f"[[Item:{reference_id}|{entity_id}]]"
                elif tipo_resultado == "Property":
                    linha[chave] = f"[[Property:{reference_id}|{entity_id}]]"

    return dados_tabela