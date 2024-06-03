import time

#Encontrar o maior valor na lista - Exemplo 1
lista = [17, 3, 11, 5, 1, 9, 7, 15, 18]
maior_numero = lista[0] #Recebeu o número 17

for i in range(1, len(lista)):
    if lista[i] > maior_numero:
        maior_numero = lista[i]

print("O maior número da lista é:", maior_numero)

#Exemplo2
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 18]
maior = my_list[0]
for i in my_list:
    if i > maior:
        maior = i

print("Maior valor 2:", maior)

#Exemplo3
ultima_lista = my_list[:]
mel = ultima_lista[0]

for i in ultima_lista[1:]:
    if i > mel:
        mel = i
print("Maior valor 3:", mel)

#Encontrar a localização de um determinado elemento dentro da lista
frutas = ["abacaxi", "maçã", "pêra", "mamão", "uva", "melancia"]

elemento = "melancia"
achado = False

for i in range(len(frutas)):
    achado = frutas[i] == elemento
    if achado:
        break

if achado:
    print("Elemento encontrado no indice:", i)
else:
    print("Não encontrado!!!")


time.sleep(2)