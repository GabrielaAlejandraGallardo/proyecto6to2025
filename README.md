Grupo:1 Integrantes: Marco Fichetti, Nahiara Nieto y Benja Corina

Historia de usuario: https://docs.google.com/document/d/1jIe9Eq3tHq6z5T_yinMCVz96VfYXgomL7-2FqFp7OQ8/edit?usp=sharing

Casos de uso y casos de prueba: https://docs.google.com/document/d/1jIe9Eq3tHq6z5T_yinMCVz96VfYXgomL7-2FqFp7OQ8/edit?usp=sharing

Modelos Clase Nombre: Servicios
Clase Nombre: Servicios

| Nombre atributo   | Tipo de dato      |
|-------------------|-------------------|
| id_servicio       | autofield         |
| descripcion       | integerField      |
| precio            | floatField        |

Clase Nombre: Contrataciones
Nombre atributo | tipo de dato          |
|---------------|-----------------------|
id_administrador| autofield FK|         |
id_servicio     |  autofield FK         |
id_contratacion |  autofield PK         |
nombre-apellido |  text                 |
senia           |   floatfield          |
saldo           |   floatfield          |

________________________________________________________________________________________________


Grupo 2 Integrantes: Gonzalo, Antü y lucas

Historial de usuario:!

Casos de Uso: https://lucid.app/lucidchart/dfcd86d7-2de8-4fde-8307-0370d333ff13/edit?viewport_loc=-471%2C160%2C2465%2C1118%2C0_0&invitationId=inv_56be0290-abfd-4fcb-81e0-17673f9362ed

Modelos Clase Nombre:cuotas de usuario 
||-----------------------|----------------| Nombre atributo   | Tipo de dato      |
|-------------------|-------------------|
| id_cuota          | AutoField(PK      |
| id_jugador        | ForeignKey        |
| Monto             | FloatField        |
| Fecha_emision     | DateTimeField     |
| Fecha_vencimiento | DateTimeField     |
| Estado            | TextField         |
| Fecha_pago        | DateTimeField     |

__________________________________________________________________________________
Grupo 3 Integrantes:

Historial de usuario:

Casos de Uso y Casos de Prueba:

Modelos Clase Nombre: Nombre atributo | tipo de dato | |---------------|-------------------| |---------------|-------------------| |---------------|-------------------| |---------------|-------------------| |---------------|-------------------| |---------------|-------------------| |---------------|-------------------| |---------------|-------------------| |---------------|-------------------| |---------------|-------------------|





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






________________________________________________________________________________________________
Grupo 6 Integrantes: Valentin Chacoma, Khalil Maccagno, Aileen Koning

Historial de usuario:https://docs.google.com/document/d/1LBT1cmzwNFe60B2__iOJUBPxASC7cXkq_rjfWBvrgxY/edit?tab=t.0

Casos de Uso y Casos de Prueba:https://docs.google.com/document/d/1LBT1cmzwNFe60B2__iOJUBPxASC7cXkq_rjfWBvrgxY/edit?tab=t.0


* Modelos
Clase Nombre: Jugadores
|Nombre atributo        |  tipo de dato     |
|-----------------------|-------------------|
|id-jugadores           |Autofield   PK     |
|nom                    |textfield          |
|dni                    |integerfield       |
|fechan                 |date               |
|altura                 |double             |
|peso                   |double             |
|dire                   |varchar            |
|cd                     |varchar            |
|qr                     |varchar            |
|descripcion-id         |bigint             |
|talla-id               |bigint             |

________________________________________________________________________________________________

Grupo 7
Integrantes: Bautista Serrano, Ludmila Luna, Pablo Perez, Morena Castillo 

Historia de Usuario: https://docs.google.com/document/d/1Ut7-_JTwDnkPIYRu1wz8Iejjdz-rnOh6yzc12i7qtvU/edit?usp=sharing

Casos de Uso  y Casos de Prueba: https://docs.google.com/document/d/1lyKOMc_kxi-8WzulgupKY_lzSceKHnSB0i5jMzGOCgw/edit?usp=sharing

CATEGORIAS:Voley,Basquet,Tela,Patin,Yoga,Pileta,Funcional,Frontal
competitivo pot categoria de voley y basquet.
formativas juntas ,femenino y masculino
Sub 13,sub 15 y 17,Desarrollo y Primera


Modelo Clase: Deportes

| Nombre atributo       | Tipo de dato             |
| --------------------- | -------------------------|
| id\_deporte           | PK de campo automático   |
| nombre\_deporte       | Campo de texto           |
| descripcion           | Campo de texto           |
| cupos\_disponibles    | Campo entero             |
| fecha\_creacion       | Campo de tiempo de datos |
| ultima\_actualizacion | Campo de tiempo de datos |

| Nombre atributo   | Tipo de dato             |
| ----------------- | ------------------------ |
| id\_categoria     | PK de campo automático   |
| nombre\_categoria | Campo de texto           |
| descripcion       | Campo de texto           |
| edad\_minima      | Campo entero             |
| edad\_maxima      | Campo entero             |
| fecha\_creacion   | Campo de tiempo de datos |

________________________________________________________________________________________________

Grupo 8
Integrantes: Octavio valles, Santino Gadea y Fernando López 

Historia de Usuario:https://docs.google.com/document/d/1_q2GTvpaEPmQ4I0n5rEYUpU0H-Br2dbrBbeiLvGO7e0/edit?usp=drivesdk

Casos de Uso  y Casos de Prueba:
https://docs.google.com/document/d/1_q2GTvpaEPmQ4I0n5rEYUpU0H-Br2dbrBbeiLvGO7e0/edit?usp=drivesdk

* Modelo clase: Cuotas
  
| Nombre atributo    | Tipo de dato             |
| ------------------ | ------------------------ |
| id_cuota	         |  AutoField PK            |
| id_socio	v        |  IntegerField FK         |
| mes_correspondiente|	CharField               |
| anio_correspondiente|	IntegerField            |
| monto_total        |	FloatField              |
| fecha_pago	       |  DateTimeField           |
| estado_pago	       |  TextField               | 
| fecha_registro     |	DateTimeField           |
| ultima_modificacion|  DateTimeField           | 
