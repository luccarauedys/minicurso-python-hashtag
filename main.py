import os
import pandas as pd
import plotly.express as px

lista_de_arquivos = os.listdir("./vendas")

tabela_de_vendas_completa = pd.DataFrame()

for arquivo in lista_de_arquivos:
    if "vendas" in arquivo.lower():
        caminho_do_arquivo = f"./vendas/{arquivo}"
        tabela = pd.read_csv(caminho_do_arquivo)
        tabela_de_vendas_completa = pd.concat(
            [tabela_de_vendas_completa, tabela])

# Calculando o produto mais vendido (em quantidade):

tabela_de_produtos = tabela_de_vendas_completa.groupby(
    "Produto", as_index=False).sum()
tabela_de_produtos = tabela_de_produtos[["Produto", "Quantidade Vendida"]]
tabela_de_produtos = tabela_de_produtos.sort_values(
    by="Quantidade Vendida", ascending=False)

grafico_produtos = px.bar(
    tabela_de_produtos, x="Produto", y="Quantidade Vendida")
grafico_produtos.show()

# Calculando o produto com maior faturamento

tabela_de_vendas_completa["Faturamento"] = tabela_de_vendas_completa["Quantidade Vendida"] * \
    tabela_de_vendas_completa["Preco Unitario"]

tabela_faturamento = tabela_de_vendas_completa.groupby(
    "Produto", as_index=False).sum()
tabela_faturamento = tabela_faturamento[["Produto", "Faturamento"]]
tabela_faturamento = tabela_faturamento.sort_values(
    by="Faturamento", ascending=False)

grafico_produtos_faturamento = px.bar(
    tabela_faturamento, x="Produto", y="Faturamento")
grafico_produtos_faturamento.show()

# Calculando a loja com maior faturamento

tabela_lojas = tabela_de_vendas_completa.groupby("Loja", as_index=False).sum()
tabela_lojas = tabela_lojas[["Loja", "Faturamento"]]
tabela_lojas = tabela_lojas.sort_values(by="Faturamento", ascending=False)

grafico_lojas_faturamento = px.bar(tabela_lojas, x="Loja", y="Faturamento")
grafico_lojas_faturamento.show()
