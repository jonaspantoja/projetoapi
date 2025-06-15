import yfinance as yf
import csv
from datetime import datetime

# Lista de ações desejadas com seus tickers do Yahoo Finanças
acoes = {
    "VALE3": "VALE3.SA",
    "PETR4": "PETR4.SA",
    "BBDC4": "BBDC4.SA",
    "ITSA4": "ITSA4.SA",
}

# Nome do arquivo CSV
nome_arquivo = "cotacoes_acoes.csv"

# Abre o arquivo CSV para escrita
# Define o ponto e vírgula como delimitador (sep=';')
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo, delimiter=';')

    # Escreve o cabeçalho no CSV
    escritor.writerow(["Data", "Ação", "Ticker", "Preço de Fechamento (R$)"])

    for nome_acao, ticker in acoes.items():
        acao = yf.Ticker(ticker)
        cotacao = acao.history(period="1d")  # Último dia de negociação

        if cotacao.empty:
            print(f"Não foi possível obter a cotação de {nome_acao}.")
            continue

        # Última linha de cotação
        ultimo_registro = cotacao.iloc[-1]
        data = cotacao.index[-1].strftime("%Y-%m-%d")
        
        # Obtém o preço de fechamento, arredonda para 2 casas decimais
        preco_fechamento_numerico = round(ultimo_registro['Close'], 2)
        
    
        # Converte o número para string e substitui o ponto por vírgula
        preco_fechamento_formatado = str(preco_fechamento_numerico).replace('.', ',')

        # Escreve os dados no CSV
        escritor.writerow([data, nome_acao, ticker, preco_fechamento_formatado])
        print(f"Cotação de {nome_acao} salva.")

print(f"\nTodas as cotações foram salvas em '{nome_arquivo}'.")
