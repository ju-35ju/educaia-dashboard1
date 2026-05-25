from faker import Faker
import pandas as pd
import random

fake = Faker('pt_BR')

cidades = [
    "Teresina",
    "Fortaleza",
    "São Luís",
    "Recife",
    "Salvador"
]

disciplinas = [
    "Matemática",
    "Python",
    "IA",
    "Marketing",
    "Banco de Dados"
]

lista = []

for i in range(1500):
    lista.append({
        "nome": fake.name(),
        "cidade": random.choice(cidades),
        "idade": random.randint(18, 35),
        "disciplina": random.choice(disciplinas),
        "nota": round(random.uniform(5, 10), 1),
        "horas_estudo": random.randint(1, 10),
        "engajamento": random.randint(50, 100)
    })


df = pd.DataFrame(lista)
df.to_csv("data/estudantes.csv", index=False)

print("Dados gerados com sucesso")