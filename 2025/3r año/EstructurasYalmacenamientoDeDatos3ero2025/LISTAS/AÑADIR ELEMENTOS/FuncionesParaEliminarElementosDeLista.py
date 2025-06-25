listaDeseos=["comer helado", "correr", "bailar","pintar",2,2.3,True, False]#CREAMOS LISTA DESEOS Y LE ASIGNAMOS 4 ELEMENTOS
#                   0           1           2      3
print(listaDeseos)#MOSTRAMOS LO QUE HAY DENTRO LA LISTA DESEOS

listaDeseos.pop()

print(listaDeseos)

listaDeseos.append("cantar")

listaDeseos.pop(0)

print(listaDeseos)



if "bailar" in listaDeseos:
  listaDeseos.remove("bailar")
  print("EL ELEMENTO SE ELIMINÓ CON ÉXITO")
else: 
    print("ESE ELEMENTOS NO SE ENCUENTRA EN LA LISTA")  
  
print(listaDeseos)
