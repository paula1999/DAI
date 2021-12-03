# Ejecución
Si en algun momento se cambia el Dockerfile, hay que hacer

`docker-compose build`


Para poner en marcha la aplicación, hay que ejecutar

`docker-compose up`

En otra terminal, abrimos una sesión de bash en el contenedor de mongo:

`#> docker-compose exec mongo /bin/bash`

y en la terminal del contenedor:

`#> mongorestore --drop dump`

que restaturará la base de datos 'SampleCollections' con las collecciones que tenga.

La dirección es `http://127.0.0.1:5000/`




Paula Villanueva Núñez