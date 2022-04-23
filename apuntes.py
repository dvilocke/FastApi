"""
****FastApi:
1.El framework mas veloz para el desarrollo web con Python
2.Creado por Sebastian Ramirez Colombiano
3.Codigo Abierto
4.Se utiliza en uber, office, netflix, windows

****Ubicación de FastApi en el ecosistema de Python

.Uvicorn: es una libreria de Python que funciona de servidor, es decir, permite que cualquier computadora se convierta
en un servidor

.Starlette: es un framework de desarrollo web de bajo nivel

Pydantic: Es un framework que permite trabajar con datos similar a pandas, pero este te
permite usar modelos los cuales aprovechara FastAPI para crear la API

Un framework parado sobre gigantes

para instalarlo -> pip install fastapi uvicorn

****como iniciar nuestra aplicacion:

uvicorn main:app --reload

--reload -> cada vez que nosotros modifiquemos algo en el codigo, no va hacer falta que abrir el navegador y se va a ver el cambio

**** Documentación interactiva
de base el framework documenta automaticamente tu API, swagger y Redoc

FastAPI también está parado sobre los hombros de OpenAPI, el cual es un conjunto de reglas que permite definir cómo describir, crear y visualizar APIs. Es un conjunto de reglas que permiten decir que una API está bien definida.
ㅤ
OpenAPI necesita de un software, el cual es Swagger, que es un conjunto de softwares que permiten trabajar con APIs. FastAPI funciona sobre un programa de Swagger el cual es Swagger UI, que permite mostrar la API documentada.
ㅤ
Acceder a la documentación interactiva con Swagger UI:
{localhost}/docs
ㅤ
Acceder a la documentación interactiva con Redoc:
{localhost}/redoc
"""


"""
DESARMANDO EL FRAMEWORK

PATH: es una routa (route o endpoint) la cual nosotros ingresamos seguido el dominio de nuestro aplicativo, sencillamente
es lo que ponemos a la derecha de nuestro dominio  myproject/API/
                                                   /DOMINIO//PATH/

Operation: Es un metodo http por el cual nos comunicamos, existen los siguientes:

1.Get: Obtener la informacion

2.Post: te envio la información de cliente a servidor

3.Put: Modificar/Actualizar la información que esta en el servidor

4.Delete: Eliminar

5.Options

6.Head

7.Patch
8.Trace

PATH OPERATIONS:
    .  
    .
    .-------> PATHS/ROUTES/ENDPOINTS : 
    .
    .
    .--------> OPERATIONS :
    
    
Un path operation decorator es el decorador que permite a una path operation function que está debajo, acceder a un 
path mediante una operation (método HTTP) y mostrar su contenido.



**** Path Parameters

colocar una variable dentro de un PATH -> DEBE PASARSE, ES DECIR, CUANDO SE LLAME A LA PATH DEBE PASARSE LA VARIABLE
ES OBLIGATORIA

Un path parameter es una variable incluida en la ruta url, con la cual especificamos la espera de un cierto dato para el 
envió hacia dicha ruta, una url puede contener varios path parameters


**** Query Parameters
colocar una variable dentro de un PATH -> pero esta vez no es obligatoria

son un conjunto definido de parámetros adjuntos al final de una URL . Son extensiones de la URL que se utilizan para 
ayudar a definir contenido o acciones específicos en función de los datos que se transmiten.

yo prodria pasarle opcionalmente a este PATH operation diciendo que yo quiero ahora que el usuario tenga una edad de tantos
años, eso se puede lograr de esta manera, puedo pasarle tambien la altura

PUT /users/{user_id}/details?age=20&height=184


**** Request Body y Response Body

Debes saber que bajo el protocolo HTTP existe una comunicación entre el usuario y el servidor. Esta comunicación está compuesta por cabeceras (headers) y un cuerpo (body). Por lo mismo, se tienen dos direcciones en la comunicación entre el cliente y el servidor y definen de la siguiente manera:

Request : Cuando el cliente solicita/pide datos al servidor.
Response : Cuando el servidor responde al cliente.
Request Body
Con lo anterior mencionado, Request Body viene a ser el cuerpo (body) de una solicitud del cliente al servidor.

Response Body
Con lo anterior mencionado, Response Body viene a ser el cuerpo (body) de una respuesta del servidor al cliente.


***** Modelos

Los modelos son la representación de una entidad en código, una entidad es un objeto de la vida real, que tiene ciertos atributos. Por ejemplo:

Carro: color, motor, año, marca
Persona: edad, nombres, apellidos, altura
Para poder crear modelos en el código se utiliza la librería Pydantic, importando la clase BaseModel:


con BaseModel voy hacer capaz de crear modelos en fastAPi

person : Person = Body(...) -> esto es un parametro de tipo Body, que es obligatorio

lo que quiere decir esto es que la persona que ese usando esta API va a tener que enviarle al servidor
un archivo json con la información del modelo que usamos


**** Validaciones: Query Parameters:
Las validaciones tal como se definen, nos sirven para comprobar si son correctos los parámetros entregados en cada una 
de las peticiones. Estas validaciones funcionan restringiendo o indicando el formato de entrega en cada una de 
las peticiones.

"""

























