import logging

from django.conf import settings
from django.utils.module_loading import import_string

from fantasy_football_catalog.apps.catalog.models import Team

celery_app = import_string(settings.CELERY_APP)
logger = logging.getLogger(__name__)


# TODO: Remove this. For now this is just for testing
# TODO: Create update player
# eventually tasks should be for updating information, potentially through a third party data collector
@celery_app.task(
    bind=True, name="fantasy_football_catalog.apps.catalog.tasks.create_team"
)
def create_team(
    _self,
    name: str,
):
    Team.objects.create(
        name=name,
    )
    logging.info(f"Team created: {name} [create_team]")
    return name
