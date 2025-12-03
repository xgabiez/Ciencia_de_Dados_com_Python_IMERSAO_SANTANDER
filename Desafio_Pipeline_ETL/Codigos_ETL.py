##CÓDIGOS USADOS NO GOOGLE LAB PARA O PROCESSO DE ETL
## EXTRAÇÃO
import pandas as pd

df = pd.read_csv('SDW2025.csv')
user_ids = df['UserID'].tolist()
print(user_ids)

import json
with open('users_mock.json', 'r') as f:
    all_users = json.load(f)

users = [user for user in all_users if user["id"] in user_ids]
print(json.dumps(users, indent=2, ensure_ascii=False))

## TRASNFORMAÇÃO

import json

# 1. Carregar o arquivo JSON original
with open("users_mock.json", "r", encoding="utf-8") as f:
    users = json.load(f)

# 2. Mensagens personalizadas
messages = {
    "Gabrielly": "Gabrielly, seu saldo está em um ótimo nível! Que tal começar a investir uma parte para fortalecer ainda mais seu futuro financeiro?",
    "Marcos": "Marcos, você está mantendo um bom controle financeiro! Avalie investir uma parte do seu saldo para começar a construir uma reserva sólida.",
    "Ana Paula": "Ana Paula, pequenos passos fazem grande diferença. Que tal iniciar um investimento leve para fazer seu dinheiro começar a trabalhar por você?"
}

# 3. Criar o campo news para cada usuário
for index, user in enumerate(users):
    mensagem = messages.get(
        user["name"],
        "Aproveite nossas novas opções de investimento!"
    )
    
    user["news"] = [
        {
            "id": index + 1,
            "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/investments.svg",
            "description": mensagem
        }
    ]

# 4. Salvar o arquivo transformado
with open("user_mock_transformed.json", "w", encoding="utf-8") as f:
    json.dump(users, f, indent=2, ensure_ascii=False)

# 5. Exibir o JSON completo transformado — estrutura final
print("=== JSON TRANSFORMADO ===\n")
print(json.dumps(users, indent=2, ensure_ascii=False))

##LOAD

import json

# Carregar usuários transformados
with open("user_mock_transformed.json", "r", encoding="utf-8") as f:
    users = json.load(f)

# Função para simular um PUT na API
def update_user(user):
    # Aqui apenas exibimos o usuário atualizado
    # como se o PUT tivesse sido feito
    print(f"{user['id']}")
    return True  # sempre retorna sucesso

# Executar "envio" do load
print("=== LOAD: atualizando usuários no sistema final ===\n")
for user in users:
    success = update_user(user)
    print(f"User {user['name']} updated? {success}!\n")

# Salvar como arquivo final da pipeline
with open("user_mock_final.json", "w", encoding="utf-8") as f:
    json.dump(users, f, indent=2, ensure_ascii=False)

print("Arquivo 'user_mock_final.json' salvo com sucesso!")
