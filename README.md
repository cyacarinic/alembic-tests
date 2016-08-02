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
Editar:		api-demo/app/alembic.ini
Cambiar:	sqlalchemy.url = driver://user:pass@localhost/dbname
Por: 		sqlalchemy.url = postgresql://postgres:123456@yachay_postgres/yachay_demo

```

### Generar scripts de migración vacios
```sh
$ docker exec api_demo  alembic -c alembic.ini revision -m "revision_demo"
```

## Funciones de Upgrade y Downgrade para los scripts generados
````sh
def upgrade():
    op.create_table(
        'Users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('guid', sa.String(), unique=True, nullable=False),
        sa.Column('email', sa.String(), unique=True),
        sa.Column('password', sa.String(), unique=True)
    )


def downgrade():
    op.drop_table('User')
```

### Actualizar la database
```sh
docker exec api_demo alembic upgrade head
```