### Construir los containers
```sh
$ docker-compose build
```

### Levantar la aplicación (Testear en puerto 8010)
```sh
$ docker-compose up -d
```

### Generar directorios y archivos de configuración de alembic
```sh
$ docker exec api_demo alembic init test_migrations
```

## Customizar la configuración según nuestro motor de base de datos
```sh
$ Editar:	api-demo/app/alembic.ini
$ Cambiar:	sqlalchemy.url = driver://user:pass@localhost/dbname
$ Por: 		sqlalchemy.url = postgresql://postgres:123456@yachay_postgres/yachay_demo
```

## Customizar el target de los modelos a migrar
```sh
$ Editar:	api-demo/app/test_migrations/env.py
$ Añadir:

import os, sys
sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))
from api import models
target_metadata = models.Base.metadata
```

### Generar scripts de migración según el modelo targeteado
```sh
$ docker exec api_demo  alembic -c alembic.ini revision --autogenerate -m "revision_demo"
```

## Verificar las funciones Upgrade y Downgrade de los scripts generados en
````sh
$ api-demo/app/test_migrations/versions/....
```

### Actualizar la database a la versión mas reciente
```sh
docker exec api_demo alembic upgrade head
```

### Actualizar la database una versión
```sh
docker exec api_demo alembic upgrade +1
```

### Retroceder una versión
```sh
docker exec api_demo alembic downgrade -1
```

### Retroceder a la versión básica
```sh
docker exec api_demo alembic downgrade base
```