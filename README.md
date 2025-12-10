# 📘 Desafio 1 --- ETL com Python

**Imersão Ciência de Dados com Python**

Este projeto implementa um processo completo de **ETL (Extract,
Transform, Load)** utilizando dados mockados, transformações com Python
e simulação de carga, devido às limitações das APIs fornecidas.

------------------------------------------------------------------------

## 📥 1. Extract --- Extração de Dados

Os dados iniciais foram extraídos de um arquivo local `user_mock.json`.

``` python
import json

with open("user_mock.json", "r") as file:
    users = json.load(file)
```

Nesta etapa:

-   Carregamos o JSON original.
-   Validamos a estrutura.
-   Preparamos os dados para as transformações.

------------------------------------------------------------------------

## 🔄 2. Transform --- Transformação dos Dados

As transformações aplicadas incluíram:

✔ **Adição de novos atributos**\
Criamos a chave `account_balance` para simular saldo bancário:

``` python
for user in users:
    user["account_balance"] = 1000
```

✔ **Ajustes e limpeza**

-   Padronização de campos.\
-   Correção de estruturas incompletas.\
-   Preparação para o carregamento.

❗ **Adaptação necessária**\
A API da OpenAI não pôde ser utilizada devido a erro no Colab (chave não
reconhecida).\
➡ A solução foi criar manualmente os enriquecimentos textuais que seriam
gerados automaticamente.

------------------------------------------------------------------------

## 📤 3. Load --- Carga dos Dados

Foi tentada a integração com a API SDW2023 usando PUT, conforme
instruído no desafio.

``` python
def update_user(user):
    response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
    return True if response.status_code == 200 else False

for user in users:
    success = update_user(user)
    print(f"User {user['name']} updated? {success}!")
```

❗ **Adaptação necessária**\
A API estava indisponível, resultando em erros.\
➡ A solução foi manter o código, mas considerar a carga como simulada e
prosseguir com o armazenamento local.

✔ **Salvamento dos arquivos finais**

**JSON final:**

``` python
with open("user_mock_final.json", "w") as file:
    json.dump(users, file, indent=2)
```

**CSV final:**

``` python
import pandas as pd

df = pd.DataFrame(users)
df.to_csv("user_mock_final.csv", index=False)
```

------------------------------------------------------------------------

## 📦 Arquivos Gerados no Projeto

-   `user_mock.json` --- dados originais (Extract)\
-   `user_mock_final.json` --- dados transformados (Transform)\
-   `user_mock_final.csv` --- tabela final (Load local)\
-   Código ETL completo no notebook

------------------------------------------------------------------------

## 🔁 O que é um Pipeline ETL?

Um pipeline ETL segue três etapas principais:

-   **E --- Extract**: Buscar dados em APIs, bancos ou arquivos.\
-   **T --- Transform**: Limpar, enriquecer, corrigir, padronizar.\
-   **L --- Load**: Enviar dados prontos para outro sistema (API, banco
    de dados, datalake).

Mesmo não conseguindo usar a API real, o processo foi mantido usando
**Load local**, preservando a lógica do desafio.

------------------------------------------------------------------------

## 🧰 Tecnologias Utilizadas

-   Python\
-   Pandas\
-   JSON\
-   Requests\
-   Google Colab\
-   Git / GitHub

------------------------------------------------------------------------

## ⭐ Conclusão

Apesar das limitações técnicas (API da OpenAI e API SDW2023
indisponíveis), o objetivo do desafio foi atingido com sucesso:

-   O ETL foi implementado.\
-   A carga foi simulada.\
-   Os arquivos finais foram gerados corretamente.\
-   Todas as etapas do pipeline foram seguidas.
