from numpy import mean
from random import randint
import matplotlib.pyplot as plt

QTD = 10
data = {}
medias = []

for c in range(QTD):
    notas = []
    nome = input("Digite o nome do aluno: ").title()
    nota1 = float(input(f"Digite a primeira nota de {nome}: "))
    nota2 = float(input(f"Digite a segunda nota de {nome}: "))
    nota3 = float(input(f"Digite a terceira nota de {nome}: "))
    nota4 = randint(0,10)
    notas.append(nota1), notas.append(nota2), notas.append(nota3), notas.append(nota4)
    media = mean(notas)
    medias.append(media)

    data['Nome'] = nome
    data['Nota 1'] = nota1
    data['Nota 2'] = nota2
    data['Nota 3'] = nota3
    data['Nota Extra'] = nota4
    data['Média'] = media


x = list(range(1,QTD+1))
y = medias

plt.plot(x, y, marker='o')
plt.title("Médias dos Alunos")
plt.xlabel("Alunos")
plt.ylabel("Médias")
plt.show()
