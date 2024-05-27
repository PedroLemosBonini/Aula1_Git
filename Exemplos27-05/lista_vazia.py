import time

my_list = [] #criando uma lista vazia

for i in range(5):
    my_list.append(i + 1)

print(my_list)

#Lista vazia 2
my_list2 = [] #Criando uma segunda lista vazia

for i in range(5):
    my_list2.insert(0, i + 1)

print(my_list2)

#Terceira lista
my_list3 = [10, 1, 8, 3, 5]

total = 0

for i in range(len(my_list3)):
    total = total + my_list3[i]

print(total)

total = 0
for i in my_list3:
    total += i

print(total)

#Reordenando a lista
# my_list3[0], my_list3[4] = my_list3[4], my_list3[0]
# my_list3[1], my_list3[3] = my_list3[3], my_list3[1]

# print(my_list3)

#Reordenando sem saber o tamanho da lista
tl = len(my_list3)
for i in range(tl // 2):
    my_list3[i], my_list3[tl - i - 1] = my_list3[tl - i - 1], my_list3[i]

print(my_list3)

time.sleep(2) 