import time

# def hi_everybody(my_list):
#     for name in my_list:
#         print("Oi,", name)
 
# hi_everybody(["Tina", "Gabi", "João"])

def criar_lista(n):
    lista = []
    for i in range(n):
        lista.append(i)
    return lista

print(criar_lista(10))

global a 
a = 1
 
def fun():
    a = 2
    print(a)
 
 
a = 3
fun()
print(a)

time.sleep(3)