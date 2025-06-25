lista=["comer helado", "correr", "bailar",]
#elementoAremplazar=lista.index("comer helado")
#lista[elementoAremplazar]="comer pizza"
print(lista)
elementoQueDeseoRemplazar=input("INGRESE ELEMENTO QUE DESEA REEMPLAZAR:")
if elementoQueDeseoRemplazar in lista:
    elementoAremplazar=lista.index(elementoQueDeseoRemplazar)
    nuevoElemento=input("INGRESE NUEVO ELEMENTO:")
    lista[elementoAremplazar]=nuevoElemento
elif elementoQueDeseoRemplazar not in lista:
       print("EL ELEMENTO", elementoQueDeseoRemplazar,"NO SE ENCUENTRA EN LA LISTA")
       otroElementoDeseoRemplazar=input("INGRESE OTRO ELEMENTO A REEMPLAZAR:")
       if otroElementoDeseoRemplazar in lista:
           elementoAremplazar=lista.index(otroElementoDeseoRemplazar)
           nuevoElemento=input("INGRESE NUEVO ELEMENTO:")
           lista[elementoAremplazar]=nuevoElemento 
       else:
           print("EL ELEMENTO", otroElementoDeseoRemplazar,"NO SE ENCUENTRA EN LA LISTA")
           print("=( los elementos que deseo reemplazar no se encontraron en la lista")
print(lista)