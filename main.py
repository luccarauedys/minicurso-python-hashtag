import os
import pandas as pd

lista_de_arquivos = os.listdir("./vendas")

tabela_de_vendas_completa = pd.DataFrame()

for arquivo in lista_de_arquivos:
    if "vendas" in arquivo.lower():
        caminho_do_arquivo = f"./vendas/{arquivo}"
        tabela = pd.read_csv(caminho_do_arquivo)
        tabela_de_vendas_completa = pd.concat(
            [tabela_de_vendas_completa, tabela])

# 1. Calculando o produto mais vendido (em quantidade):

tabela_de_produtos = tabela_de_vendas_completa.groupby("Produto").sum()
tabela_de_produtos = tabela_de_produtos[["Quantidade Vendida"]]
tabela_de_produtos = tabela_de_produtos.sort_values(
    by="Quantidade Vendida", ascending=False)

produto_mais_vendido = tabela_de_produtos.index[0]
print(f"PRODUTO MAIS VENDIDO: {produto_mais_vendido}")

# 2. Calculando o produto com maior faturamento

tabela_de_vendas_completa["Faturamento"] = tabela_de_vendas_completa["Quantidade Vendida"] * \
    tabela_de_vendas_completa["Preco Unitario"]

tabela_faturamento = tabela_de_vendas_completa.groupby("Produto").sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]]
tabela_faturamento = tabela_faturamento.sort_values(
    by="Faturamento", ascending=False)

produto_maior_faturamento = tabela_faturamento.index[0]
print(f"PRODUTO COM MAIOR FATURAMENTO: {produto_maior_faturamento}")

# 3. Calcular a loja com maior faturamento

tabela_lojas = tabela_de_vendas_completa.groupby("Loja").sum()
tabela_lojas = tabela_lojas[["Faturamento"]]
tabela_lojas = tabela_lojas.sort_values(
    by="Faturamento", ascending=False)

loja_maior_faturamento = tabela_lojas.index[0]
print(f"LOJA COM MAIOR FATURAMENTO: {loja_maior_faturamento}")
