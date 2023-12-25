# Pretor/1.5 - @edpomacedo - modules/salvar_noticia_markdown.py
def salvar_noticia_como_markdown(titulo, link, descricao, pubdate, content, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(f"---\n")
        arquivo.write(f"title: \"{titulo}\"\n")
        arquivo.write(f"link: \"{link}\"\n")
        arquivo.write(f"description: \"{descricao}\"\n")
        arquivo.write(f"pubdate: \"{pubdate}\"\n")
        arquivo.write(f"---\n\n")
        arquivo.write(f"## Conteúdo\n\n{content}\n")