productos=["jugo uva"]
print("Lista inicial",productos)
productos.append("Papel higienico")
productos.append("yogurt pera")
print("lista completa despues de usar append",productos)
productos.insert(0,"jabon en polvo")

print("Despues de usar insert: ",productos)
productos[1]="Rollo Cocina" #reemplazamos valor de elemento en la posición 1 conejo por liebre
print("Lista animales Despues de remplazar conjeo por Rollo cocina:", productos)