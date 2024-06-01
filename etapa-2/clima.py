import requests
import logging
import os

# Configurar o logging para registrar erros em um arquivo de log apenas em caso de erro
log_filename = 'erros_clima.txt'

def configurar_logging():
    if not logging.getLogger().hasHandlers():
        logging.basicConfig(filename=log_filename, level=logging.ERROR, 
                            format='%(asctime)s - %(levelname)s - %(message)s')

def obter_clima(cidade, chave_api):
    # Construir a URL para a solicitação à API OpenWeatherMap com os parâmetros fornecidos
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric&lang=pt_br"
    try:
        # Fazer a solicitação GET para a API
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve erros na solicitação
        dados_clima = response.json()  # Converter a resposta para JSON

        # Verificar se a resposta contém um código de erro
        if dados_clima.get('cod') != 200:
            mensagem_erro = dados_clima.get('message', 'Erro desconhecido')
            configurar_logging()
            logging.error(f"Erro na solicitação: {mensagem_erro}")
            print(f"Erro na solicitação: {mensagem_erro}")
            return

        # Extrair as informações desejadas do JSON
        descricao_clima = dados_clima['weather'][0]['description']
        temperatura_atual = dados_clima['main']['temp']

        # Exibir os resultados no console
        print(f"Clima em {cidade}:")
        print(f"Descrição: {descricao_clima}")
        print(f"Temperatura Atual: {temperatura_atual}°C")
        
    except requests.exceptions.HTTPError as errh:
        if errh.response.status_code == 404:
            configurar_logging()
            logging.error(f"Cidade não encontrada: {cidade}")
            print(f"Cidade '{cidade}' não encontrada. Por favor, verifique o nome e tente novamente.")
        else:
            configurar_logging()
            logging.error(f"Erro HTTP: {errh}")
            print(f"Erro HTTP: {errh}")
    except requests.exceptions.ConnectionError as errc:
        configurar_logging()
        logging.error(f"Erro de Conexão: {errc}")
        print(f"Erro de Conexão: {errc}")
    except requests.exceptions.Timeout as errt:
        configurar_logging()
        logging.error(f"Erro de Timeout: {errt}")
        print(f"Erro de Timeout: {errt}")
    except requests.exceptions.RequestException as err:
        configurar_logging()
        logging.error(f"Erro: {err}")
        print(f"Erro: {err}")
    except KeyError as e:
        configurar_logging()
        logging.error(f"Chave não encontrada no JSON: {e}")
        print(f"Erro ao processar dados: {e}")

def main():
    # Solicitar ao usuário a cidade
    cidade = input("Digite o nome da cidade: ")
    # Sua chave de API para autenticação com a OpenWeatherMap
    chave_api = "15493ede9a83e0be32fd1b9dce9571ce"  # Substitua por sua chave de API da OpenWeatherMap
    
    # Chamar a função para obter e exibir o clima
    obter_clima(cidade, chave_api)

if __name__ == "__main__":
    # Ponto de entrada do script
    main()
