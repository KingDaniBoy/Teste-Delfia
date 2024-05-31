import requests
import logging

# Configurar o logging para registrar erros em um arquivo de log
logging.basicConfig(filename='erros.txt', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def obter_clima(cidade, chave_api, unidade_temp):
    # Definir a unidade de temperatura na solicitação à API
    if unidade_temp.lower() == 'c':
        units = 'metric'  # Celsius
    elif unidade_temp.lower() == 'f':
        units = 'imperial'  # Fahrenheit
    else:
        print("Unidade de temperatura inválida. Usando Celsius por padrão.")
        units = 'metric'  # Celsius por padrão

    # Construir a URL para a solicitação à API OpenWeatherMap com os parâmetros fornecidos
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units={units}&lang=pt_br"
    try:
        # Fazer a solicitação GET para a API
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve erros na solicitação
        
        dados_clima = response.json()  # Converter a resposta para JSON

        # Extrair as informações desejadas do JSON
        descricao_clima = dados_clima['weather'][0]['description']
        temperatura_atual = dados_clima['main']['temp']

        # Exibir os resultados no console
        print(f"Clima em {cidade}:")
        print(f"Descrição: {descricao_clima}")
        print(f"Temperatura Atual: {temperatura_atual}°{unidade_temp.upper()}")
        
    except requests.exceptions.HTTPError as errh:
        if response.status_code == 404:
            print("Cidade não encontrada. Verifique o nome da cidade e tente novamente.")
        elif response.status_code == 401:
            print("Erro: Chave da API inválida. Verifique sua chave de API e tente novamente.")
        else:
            logging.error(f"HTTP Error: {errh}")
            print(f"Erro HTTP: {errh}")
    except requests.exceptions.ConnectionError as errc:
        logging.error(f"Error Connecting: {errc}")
        print(f"Erro de Conexão: {errc}")
    except requests.exceptions.Timeout as errt:
        logging.error(f"Timeout Error: {errt}")
        print(f"Erro de Timeout: {errt}")
    except requests.exceptions.RequestException as err:
        logging.error(f"Error: {err}")
        print(f"Erro: {err}")
    except KeyError as e:
        logging.error(f"Chave não encontrada no JSON: {e}")
        print(f"Erro ao processar dados: {e}")
    except Exception as e:
        logging.error(f"Erro inesperado: {e}")
        print(f"Erro inesperado: {e}")

def main():
    try:
        # Solicitar ao usuário a cidade
        cidade = input("Digite o nome da cidade: ")
        # Solicitar ao usuário a chave de API
        chave_api = input("Digite sua chave de API da OpenWeatherMap: ")
        # Solicitar ao usuário a unidade de temperatura desejada
        unidade_temp = input("Digite a unidade de temperatura desejada (Celsius 'C' ou Fahrenheit 'F'): ")

        # Chamar a função para obter e exibir o clima
        obter_clima(cidade, chave_api, unidade_temp)
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")
    except Exception as e:
        logging.error(f"Erro inesperado: {e}")
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    # Ponto de entrada do script
    main()
