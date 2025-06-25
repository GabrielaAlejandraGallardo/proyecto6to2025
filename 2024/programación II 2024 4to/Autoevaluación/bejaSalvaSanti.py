lacteo=[]




carnes=[]




verduras=[]




legumbres=[]




menu=input("1-cargar productos   2-mostrar productos en stock  ")
if menu=="1":
    productos=input("Que productos quiere cargar: A-Lacteos  B-Carnes  C-Verduras  D-Legumbres ")
   
    if productos=="A":
        lac=input("introduzca el producto: ")
   
        lacteo.append(lac)
   
    elif productos=="B":
        car=input("introduzca el producto: ")




        carnes.append(car)
   
    elif productos=="C":
        verd=input("introduzca el producto: ")
     


        verduras.append(verd)




    elif productos=="D":
        legum=input("introduzca el producto: ")




        legumbres.append(legum)




elif menu=="B":
    mostrar=input("que productos quieres mostrar  1-Lacteos  2-Carnes  3-Verduras  4-Legumbres   ")
    if mostrar=="A":
        print(lacteo)
    
