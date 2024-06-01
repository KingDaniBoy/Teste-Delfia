# Clima

Este script consulta a API do OpenWeatherMap para obter informações sobre o clima de uma cidade especificada pelo usuário.

## Pré-requisitos

Antes de executar o script, certifique-se de ter instalado os seguintes itens:

- [Python 3.6+](https://www.python.org/downloads/)
- [requests](https://pypi.org/project/requests/)

## Instalação

### 1. Clonar o repositório (ou baixar o arquivo clima.py)

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Instalar as dependências

Você pode instalar a biblioteca `requests` usando o `pip`. Abra o terminal e execute:

```bash
pip install requests
```

## Configuração

### 3. Obter uma chave de API do OpenWeatherMap

Você precisará de uma chave de API do OpenWeatherMap. Se você ainda não tem uma, pode se inscrever gratuitamente [aqui](https://home.openweathermap.org/users/sign_up).

### 4. Atualizar a chave de API no script

No arquivo `clima.py`, substitua `YOUR_API_KEY_HERE` pela sua chave de API. Encontre a linha com `chave_api = "15493ede9a83e0be32fd1b9dce9571ce"` e substitua `"15493ede9a83e0be32fd1b9dce9571ce"` pela sua chave.

```python
chave_api = "YOUR_API_KEY_HERE"
```

## Uso

### 5. Executar o script

No terminal, navegue até o diretório onde o arquivo `clima.py` está localizado e execute o seguinte comando:

```bash
python clima.py
```

### 6. Inserir o nome da cidade

Quando solicitado, digite o nome da cidade para a qual você deseja obter informações sobre o clima.

## Registro de Erros

Erros durante a execução do script serão registrados no arquivo `erros_clima.txt`.

## Exemplo

```text
Digite o nome da cidade: São Paulo
Clima em São Paulo:
Descrição: nublado
Temperatura Atual: 22°C
```

