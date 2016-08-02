Construir los containers
```sh
$ docker-compose build
```

Levantar la aplicación (Testear en puerto 8010)
```sh
$ docker-compose up -d
```

Generar directorios y archivos de configuración de alembic
```sh
$ docker exec api_demo alembic init migrations
```

Generar scripts de migración vacios
```sh
$ docker exec api_demo  alembic -c api/alembic.ini revision -m "test"
```