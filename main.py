def obtenerNumeroMayor(listadoDeNumeros):
  numeroMAyor=0
  for elemento in listadoDeNumeros:
    if elemento > numeroMAyor:
     numeroMAyor=elemento 
      #recordar que el retur es el fin del cilo for
  return numeroMAyor


print("que honda")
numeros = []
print("ingerse 5 numeros")
for iterador in range(5):
  print(iterador)
  numeroIngresado=int(input("ingrese numero "+str(iterador+1)+":" ))
  numeros.append(numeroIngresado)
  

respuesta=obtenerNumeroMayor(numeros)
print("el numero mayor es: "+str(respuesta))
