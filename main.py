import os
import pandas as pd

lista_de_arquivos = os.listdir("./vendas")

tabela_de_vendas_completa = pd.DataFrame()

for arquivo in lista_de_arquivos:
    if "vendas" in arquivo.lower():
        caminho_do_arquivo = f"./vendas/{arquivo}"
        tabela = pd.read_csv(caminho_do_arquivo)
        # Juntando todas as tabelas de vendas em uma só
        tabela_de_vendas_completa = pd.concat(
            [tabela_de_vendas_completa, tabela])

# Calculando o produto mais vendido (em quantidade):

# Agrupando por nome do produto e somando as demais colunas
tabela_de_produtos = tabela_de_vendas_completa.groupby("Produto").sum()
# Pegando somente a coluna que somou as quantidades vendidas de cada produto
tabela_de_produtos = tabela_de_produtos[["Quantidade Vendida"]]
# Ordenando do produto mais vendido para o menos vendido
tabela_de_produtos = tabela_de_produtos.sort_values(
    by="Quantidade Vendida", ascending=False)
# Pegando o nome do produto mais vendido
produto_mais_vendido = tabela_de_produtos.index[0]
print(produto_mais_vendido)
