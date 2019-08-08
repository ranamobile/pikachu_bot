Copy the env.example file to .env and edit the variables.

```
cp env.example .env
```

Start up the service.

```
docker-compose up -d
```

Access the container.

```
docker-compose exec pikabot /bin/bash
```
