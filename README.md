# Franco Pietrokovsky - Bienvenido a mi PI.


### Este proyecto tiene como consigna el crear una **RESTful API** utilizando los siguientes Datasets como fuente de información:

- Circuitos.
- Constructores.
- Conductores.
- Carreras.
- Resultados.
- Tiempo de vuelta.
- Tiempos de tramos de vuelta.


## Tareas que esta API debe poder realizar:

- Retornar el año en el que se realizaron más carreras. ✔️
- Retornar el piloto con mayor cantidad de primeros puestos. ✔️
- Retornar el circuito más recorrido. ✔️
- Retornar el piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British. ✔️


## Para cumplir con estas tareas utilicé:

- FastAPI.
- Uvicorn.
- SQLAlchemy.
- PyMySQL.
- Pydantic.
- MySQL.
- Hostinger.
- Railway.


## Plus:

Como adicional, incluí la ruta ~~[https://henryapi.up.railway.app/dev/{token}](https://henryapi.up.railway.app/{token}/devs)~~, donde (con propósitos de prueba) se deberá reemplazar **{token}** por **FKpdbdj7kg**.
La misma también incluye una Excepción HTTP al utilizar un Token no válido.


## Procedimiento:


1. Creé el servidor MySQL en Hostinger.

2. Usando SQLAlchemy y PyMySQL creé un engine conectando al database. También instancié la clase MetaData de SQLAlchemy, para luego utilizarla en la creación de las tablas en el servidor MySQL.

3. Las tablas están conformadas por un nombre de tabla y las clases Column, String, Integer y Float (también de SQLAlchemy). A la misma se le asigna a la instancia de MetaData.

4. Armé los esquemas correspondientes (uno por cada tabla) que posteriormente serían utilizados a la hora de ingestar y/o consultar.

5. Normalicé los Datasets utilizados, para posteriormente ingestarlos dentro del DataBase.

6. Declaré las variables dentro del archivo "alias.py" (asignando modelos y sus métodos, al igual que funciones de SQLAlchemy) con el propósito de obtener una mejor legibilidad.

7. Dentro del archivo "api.py" (main) instancié la clase FastAPI, cargué el archivo "tokens.json", y declaré las funciones de tipo GET.

8. Cargué mis archivos en el repositorio en cuestión, para posteriormente hostear mi API en la plataforma [Railway](https://railway.app/).


## Resultado:

### ~~Esta es mi [API](https://henryapi.up.railway.app/)~~ (OFFLINE).
