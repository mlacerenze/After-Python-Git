# Repaso de listas
names = ['Marcos', 'Pedro', 'Cristian', 'Leandro', 'Adam', 'Darwin']

# Que tipo de dato estoy mostrando (type())
print(type(names))

# Slicing
print(names[::2]) # muestro los nombres cada 2
print(names[3:]) # muestra del tercer elemento hasta el final 

# Mostramos los nombres usando for
for i in names: # declaro una variable (i) que recorra todos los elementos (lista de nombres) y los valla mostrando (print())
  print(i)

# Insertar elemento en una lista (2 formas)
# 1- A través de indices
names.insert(2, 'Franco') # Llamo a la lista, indicandole que inserte, en la posición 2 a 'Franco'
print('\n\n', names)

# 2- Insertando a lo ultimo
names.append('Alejando') # Llamo a la lista, indicandole que inserte AL FINAL a 'Alejandro"
print('\n\n', names)

# Eliminar un elemento de la lista (2 formas)
# 1- Remove
names.remove('Franco')
print('\n\n', names)

# 2- pop
deleted = names.pop() # pop elimina el ultimo elemento
print('\n\nElemento eliminado (ultimo)', deleted)
print(names)





