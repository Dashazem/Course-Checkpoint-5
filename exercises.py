#Cree un bucle For de Python.
numbers = [1, 2, 3, 4]

for number in numbers:
    print(number)

#Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.
def suma(num1, num2, num3):
    return num1 + num2 + num3 


resultado = suma(2, 8, 10)
print(resultado)

#Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.
suma_de_num = lambda num1, num2, num3: num1 + num2 + num3

print(suma_de_num(5, 13, 7))

#Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.
nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']

count = 0

for nombre_de_lista in lista_nombre:
    if nombre == nombre_de_lista:
        print('El valor de la variable coincide con el valor de la lista')  
    else:
        count += 1
        if count == len(lista_nombre):
            print('Ningún valor de la lista coincide con el valor de la variable')

