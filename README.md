```sh
$ docker-compose build
```

```sh
$ docker-compose up -d
```

```sh
$ docker exec api_demo alembic init migrations
```

```sh
$ docker exec api_demo  alembic -c api/alembic.ini revision -m "baseline"
```