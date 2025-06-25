#trabajo practico: en este trabajo practico deberan utilizar PSeint para diseñar un juego interactivo  , puede ser
#ideado de forma personall o buscar referencias o ideas en la web.En caso que la idea no sea personal  y se implementen componentes no utilizados
#en clases deberan saber e investigar su funcionamiento.
#Fecha de entrega jueves 14/11/24
print( "bienvenido, este es un juego de verdadero o falso, si usted cree que la respuesta es verdadera ponga 1 y si cree que no ponga 0 ")
# esta es falsa
Total=0
preg1=input(" En 1512 cristobal colon descubiro america  V/F: ")

if preg1=="F":
	print("correcto")
	Total=Total+1
else:
	 print("incorrecto")

# esta es falsa
preg2=input("en 1092 fue la tercera revolucion industrial V/F: ")

if preg2=="F":
	print("correcto")
	Total=Total+1
else:
	 print("incorrecto")

#esta es falsa
preg3=input( "2009 fue la segunda revolucion industrial V/F: ")
if preg3=="F":
 print("correcto")
 Total=Total+1
else:
	 print("incorrecto")
	
#es verdadera
preg4=input( "en 1506 cristobal colon murio V/F: ")
if preg4=="V":
	print("correcto")
	Total=Total+1
else:
	 print("incorrecto")
	
#es verdadera
preg5=input("en 1492 cristobal colon descubrio america V/F: ")
if preg5=="V":
	print("correcto")
	Total=Total+1
else:
	 print("incorrecto")
# es verdadera
preg6=input( "en 1939 fue la segunda guerra mundial V/F: ")
if preg6=="V":
	print("correcto")
	Total=Total+1
else:
	 print("incorrecto")

# es verdadera
preg7=input( "fue en 1914 empezo la primera guerra mundial V/F: ")
if preg7=="V":
	print("correcto")
	Total=Total+1
else:
	 print("incorrecto")

#es flasa
preg8=input( "en 1818 argentina se independizo V/F: ")
if preg8=="F":
	print("correcto")
	Total=Total+1
else:
	 print("incorrecto")
	# es falsa
preg9=input( "fue en el año 587  que fue la caida del imperio romano  V/F:" )
if preg5=="F":
	print("correcto")
	Total=Total+1
else:
	 print("incorrecto")
	# es verdadera
preg10=input("en 1789 fue la revulucion fransesa V/F: ")
if preg10=="V":
    print("correcto")
    Total=Total+1
else:
	 print("incorrecto")


if Total==10 or Total==9:
		print("usted es muy intilegente")
if Total==8:
		print( "usted es muy bueno en este juego")
if Total==7:
    print("usted es bueno en este juego")
if Total==6:
    print("usted puede mejorar")
if Total==4 or Total==5:
    print("usted tiene que mejorar mejorar")
if Total<4:
    print("usted debería estudiar")