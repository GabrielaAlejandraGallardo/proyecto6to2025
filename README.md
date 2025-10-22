Grupo:1 Integrantes: Marco Fichetti, Nahiara Nieto y Benja Corina

Historia de usuario: https://docs.google.com/document/d/1jIe9Eq3tHq6z5T_yinMCVz96VfYXgomL7-2FqFp7OQ8/edit?usp=sharing

Casos de uso y casos de prueba: https://docs.google.com/document/d/1jIe9Eq3tHq6z5T_yinMCVz96VfYXgomL7-2FqFp7OQ8/edit?usp=sharing

Modelos Clase Nombre: Servicios
Clase Nombre: Servicios

| Nombre atributo   | Tipo de dato      |
|-------------------|-------------------|
| id_servicio       | Autofield         |
| descripcion       | IntegerField      |
| precio            | FloatField        |

Clase Nombre: Contrataciones
Nombre atributo | tipo de dato          |
|---------------|-----------------------|
id_administrador|   Autofield FK|       |
id_servicio     |   Autofield FK        |
id_contratacion |   Autofield PK        |
nombre-apellido |   TextField           |
senia           |   Floatfield          |
saldo           |   floatfield          |

Pruebas funcionales Unitarias y de Integración bajo Selenium:  https://docs.google.com/document/d/1jIe9Eq3tHq6z5T_yinMCVz96VfYXgomL7-2FqFp7OQ8/edit?usp=sharing


Pruebas de Performance o rendimiento:https://docs.google.com/document/d/1jIe9Eq3tHq6z5T_yinMCVz96VfYXgomL7-2FqFp7OQ8/edit?usp=sharing

________________________________________________________________________________________________


Grupo 2 Integrantes: Gonzalo, Antü y lucas

Historia de usuario:! https://docs.google.com/document/d/e/2PACX-1vQn37N4ttDof0rS3FvltWk2Rodd4Di40hPXEkdAFA1Ed5WKjV_w_cC8YMlClYZFnSXG-7MAFYtmr-jy/pub

Casos de Uso y de prueba: https://docs.google.com/document/d/e/2PACX-1vTJN_tfCB2AtQJ35I1-tm4Xmvwajwt5Q9QQ61CGstT5FL8Zhu2cUyzHgcNhlyPFr3bqmOxkhQWyGC-s/pub

Modelos Clase Nombre:cuotas de jugador 
| Nombre atributo   | Tipo de dato      |
|-------------------|-------------------|
| id_cuota          | AutoField         |
| id_evento         | ForeignKey        |
| nom               | CharField         |
| cuotaMe           | DateField         |
| fechap            | DateField         |
| importe           | FloatField        |

Pruebas funcionales Unitarias y de Integración bajo Selenium: 

Pruebas de Performance o rendimiento:
__________________________________________________________________________________

Grupo 3 
Integrantes: Axel Agustin Delsoglio, Abril Bustos, Uriel Capdevila y Elias Godoy. 

Historial de usuario: https://docs.google.com/document/d/1Xf1EZb7n0XtGJMPTMSYRVjTgE97q6SklVYZzDtXm9vg/edit?usp=sharing

Casos de Uso y Casos de Prueba: https://docs.google.com/document/d/1Xf1EZb7n0XtGJMPTMSYRVjTgE97q6SklVYZzDtXm9vg/edit?usp=sharing

Modelos Clase Nombre: Jugadores
| Nombre atributo | Tipo de dato | 
----------------------------------
| id              | AutoField    |
| DNI             | IntegerField |
| nom             | CharField    |
| fechan          | DateField    |
| altura          | FloatField   |
| peso            | FloatField   |
| cd              | CharField    |
| talla           | ForeignKey   |
| descripcion     | ForeignKey   |
| qr              | ImageField   |

Pruebas funcionales Unitarias y de Integración bajo Selenium: 

Pruebas de Performance o rendimiento:
_______________________

Grupo 4
Integrantes: Teo, Franco, juan, luciana

Historia de Usuario y Casos de uso:
https://docs.google.com/document/d/1kXqtq0SjL1fl1F63e_QgSFPpKCo7bz7oHtx5sjFouCk/edit?usp=sharing

Casos de Prueba:

https://docs.google.com/document/d/1Tyv7i1LYKgDrfkioOA2hKltpr8ggle6x/edit?usp=sharing&ouid=104322610521228299031&rtpof=true&sd=true


* Modelos
Clase Nombre:Eventos


|Nombre atributo      |  tipo de dato         |
|---------------------|-----------------------|
|id_evento            | AutoField    PK       |
| nombre_evento       | TextField             |
| fecha               | DataTimeFlied         |
| lugar               | TextField             |
| descripcion         | TextField             |
| id_Administrador    | IntegerField   FK     |
| fecha_creacion      | DataTimeField         |
| ultima_modificacion | DataTimeField         |
| estado              | TextField             |

Pruebas funcionales Unitarias y de Integración bajo Selenium:
https://docs.google.com/document/d/1NSutDIHI4d444MvBqQYlLqybN3gqtC5oLmU85ObSLRs/edit?usp=sharing


Pruebas de Performance o rendimiento: https://docs.google.com/document/d/1WJ7qGyZOpHeZvNcy8c3bnI849mF-Szb9Mf5XjCQPdk8/edit?usp=sharing

________________________________________________________________________________________________

Grupo 5
Integrantes:Moyano Ana, Alvaro Capdevila, Simon oyola, Alexa villada 

Historia de Usuario:https://docs.google.com/document/d/1ZPSIrqVMJD7ejSeNGMYLkku5SQ8dKEsICTMMt-bH5uc/edit?usp=sharing

Casos de Uso  y Casos de Prueba:https://docs.google.com/document/d/1HnpchmA9sOiAc5XKZigmrkwDr8Ja23_ml53VI9uOKBo/edit?usp=sharing


* Modelos
Clase Nombre: Socios



|Nombre atributo      | tipo de dato          |
|---------------------|-----------------------|
|id_socio             | AutoField       PK    |
|nombre_apellido_socio| TextField             |
| Direccion           | TextField             |
| telefono            | TextField             |
| id_Administrador    | IntegerField      FK  |
| fecha_registro      | DataTimeField         |
| ultima_actualizacion| DataTimeField         |
| estado              | TextField             |



Pruebas funcionales Unitarias e integración  bajo Selenium:
https://docs.google.com/document/d/1HnpchmA9sOiAc5XKZigmrkwDr8Ja23_ml53VI9uOKBo/edit?usp=sharing


Pruebas de Performance o Rendimiento: 

________________________________________________________________________________________________
Grupo 6 Integrantes: Valentin Chacoma, Khalil Maccagno, Aileen Koning

Historia de usuario:https://docs.google.com/document/d/1LBT1cmzwNFe60B2__iOJUBPxASC7cXkq_rjfWBvrgxY/edit?tab=t.0

Casos de Uso y Casos de Prueba:https://docs.google.com/document/d/1LBT1cmzwNFe60B2__iOJUBPxASC7cXkq_rjfWBvrgxY/edit?tab=t.0


* Modelos
Clase Nombre: Jugadores

|Nombre atributo        |  tipo de dato     |
|---------------------- |------------------ |
|id                     | Autofield   PK    |
|DNI                    | textfield         |
|nom                    | charfield         |
|fechan                 | integerfield      |
|altura                 | floatfield        |
|peso                   | floatfield        |
|dire                   | charfield         |
|cd                     | charfield         |
|talla                  | FK                |
|descripcion            | FK                |
|qr                     | imagefield        |

Pruebas funcionales Unitarias y de Integración bajo Selenium:
https://docs.google.com/document/d/14GYLFV5kouXbUlLYrkoqAXZFr9hLHfrGpebKX8MEuJA/edit?usp=sharing

Pruebas de Performance o rendimiento: 
_______________________________________________________________________

Grupo 7
Integrantes: Bautista Serrano, Ludmila Luna, Pablo Perez, Morena Castillo 

Historia de Usuario: https://docs.google.com/document/d/1Ut7-_JTwDnkPIYRu1wz8Iejjdz-rnOh6yzc12i7qtvU/edit?usp=sharing

Casos de Uso  y Casos de Prueba: https://docs.google.com/document/d/1lyKOMc_kxi-8WzulgupKY_lzSceKHnSB0i5jMzGOCgw/edit?usp=sharing

Equipo 3, el link que han presentado  en casos de Uso y casos prueba es de otro equipoEquipo y para otro requerimientos
Requerimiento: Contrataciones


CATEGORIAS:Voley,Basquet,Tela,Patin,Yoga,Pileta,Funcional,Frontal
competitivo pot categoria de voley y basquet.
formativas juntas ,femenino y masculino
Sub 13,sub 15 y 17,Desarrollo y Primera


Modelo Clase: Deportes

| Nombre atributo       | Tipo de dato             |
| --------------------- | -------------------------|
| id\_deporte           | Primay Key               |
| iddescripciondeporte  | ForeignKey               |
| idCategoria           | ForeignKey               |
| horario               | DateTimeField            |

| Nombre atributo   | Tipo de dato             |
| ----------------- | ------------------------  
| idcategoria       | primary_key              |
| descripcion       | CharField                |

Pruebas funcionales Unitarias  y de Integración bajo Selenium:

Pruebas de Performance o rendimiento:
________________________________________________________________________________________________

Grupo 8
Integrantes: Octavio valles, Santino Gadea y Fernando López 

Historia de Usuario:https://docs.google.com/document/d/1_q2GTvpaEPmQ4I0n5rEYUpU0H-Br2dbrBbeiLvGO7e0/edit?usp=drivesdk

Casos de Uso  y Casos de Prueba:
https://docs.google.com/document/d/1_q2GTvpaEPmQ4I0n5rEYUpU0H-Br2dbrBbeiLvGO7e0/edit?usp=drivesdk

* Modelo clase: Cuotas Socios
  
| Nombre atributo    | Tipo de dato             |
| ------------------ | ------------------------ |
| idCuota	           |  AutoField PK            |
| id                 |  ForeignKey FK           |
| nom                |	CharField               |
| cuotaMes           |	DateField               |
| fechap             |	DateField               |
| importe   	       |  DateField               |



Pruebas funcionales Unitarias y de Integración bajo Selenium:

Pruebas de Performance o rendimiento:
