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

# Test task running locally

Start rabbitmq
```shell
docker compose up rabbitmq
```

start redis and celery app
```shell
docker compose up -d redis
docker compose run migrate
docker compose run bash
celery --app fantasy_football_catalog.celery_app worker
```

Run in manage.py shell
```shell
docker compose run shell

from fantasy_football_catalog.apps.catalog.models import Team
from fantasy_football_catalog.apps.catalog.tasks import create_team
import pendulum

result = create_team.delay("Bengals")
result.status  # 'SUCCESS'

result = create_team.apply_async(args=('Seahawks',), eta=pendulum.now('UTC').add(minutes=1))
result.status  # 'PENDING', even if it works it may still be 'PENDING' bug?

for team in Team.objects.all():
  print(team.name)
```