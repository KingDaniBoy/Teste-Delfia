import csv
import logging
import os

# Configurar o logging para registrar erros em um arquivo de log
logging.basicConfig(filename='erros.txt', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def processar_transacoes(input_file, output_file, valor_limite):
    try:
        # Verificar se o arquivo de entrada existe
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"O arquivo {input_file} não foi encontrado.")
        
        print(f"Lendo o arquivo: {input_file}")

        # Abrir o arquivo de entrada com codificação 'latin1' e delimitador ';'
        with open(input_file, mode='r', newline='', encoding='latin1') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            
            # Verificar e imprimir os cabeçalhos
            headers = reader.fieldnames
            print(f"Cabeçalhos encontrados: {headers}")
            transacoes_altas = []

            # Processar cada linha do arquivo CSV
            for row in reader:
                try:
                    valor_transacao = float(row['Valor da Transação'])
                    if valor_transacao > valor_limite:
                        transacoes_altas.append(row)
                except ValueError as e:
                    logging.error(f"Erro ao processar linha {row}: {e}")
                    print(f"Erro ao processar linha {row}: {e}")

        # Verificar se tem transações altas para salvar
        if transacoes_altas:
            print(f"Encontradas {len(transacoes_altas)} transações acima de ${valor_limite}. Salvando no arquivo: {output_file}")
            try:
                # Abrir o arquivo de saída com codificação 'latin1' e delimitador ';'
                with open(output_file, mode='w', newline='', encoding='latin1') as csvfile:
                    fieldnames = ['Nome do Cliente', 'Valor da Transação', 'Data da Transação']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
                    
                    # Escrever o cabeçalho e as transações filtradas
                    writer.writeheader()
                    writer.writerows(transacoes_altas)

                print(f"Processamento concluído. Transações acima de ${valor_limite} foram salvas em '{output_file}'.")
            except Exception as e:
                logging.error(f"Erro ao escrever o arquivo de saída: {e}")
                print(f"Erro ao escrever o arquivo de saída: {e}")
        else:
            print(f"Nenhuma transação acima de ${valor_limite} foi encontrada.")

    except FileNotFoundError as e:
        logging.error(f"Arquivo não encontrado: {e}")
        print(f"Erro: Arquivo '{input_file}' não encontrado.")
    except Exception as e:
        logging.error(f"Erro inesperado: {e}")
        print(f"Ocorreu um erro inesperado: {e}")

# Configurar os parâmetros do script utilizando o caminho dos seus arquivos
input_file = r'C:\Users\Family\Documents\DANIEL\Teste-Delfia\etapa-1\transacoes.csv'
output_file = r'C:\Users\Family\Documents\DANIEL\Teste-Delfia\etapa-1\transacoes_altas.csv'
valor_limite = 1000.0

# Executar o processamento das transações
processar_transacoes(input_file, output_file, valor_limite)
