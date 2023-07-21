# Fantasy Football Catalog

# Virtual environment setup
```shell
python3.10 -m venv venv
source venv/bin/activate
deactivate
```

# Docker setup
```shell
export DOCKER_BUILDKIT=1;
docker build --tag fantasy-football-catalog:latest --no-cache .;
docker compose run test
```

# Create a blank migration to add default data
```shell
docker compose run makemigrations --empty catalog
```
