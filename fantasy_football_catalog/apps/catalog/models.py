import uuid
from datetime import datetime, timezone

from django.db import models


class CommonModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Team(CommonModel):
    name = models.CharField(max_length=128, unique=True)


class FantasyLeague(CommonModel):
    name = models.CharField(max_length=128, unique=True)
    start_year = models.IntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(start_year__gte=2000) & models.Q(start_year__lte=2100),
                name="Start year is between 2000 and 2100",
            )
        ]


class FantasyTeam(CommonModel):
    name = models.CharField(max_length=128)
    league = models.ForeignKey(FantasyLeague, null=False, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "name",
                    "league",
                ],
                name="unique_fantasy_team_name_in_league",
            ),
        ]


class Player(CommonModel):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    position = models.CharField(
        choices=(
            ("QB", "QB"),
            ("WR", "WR"),
            ("RB", "RB"),
            ("TE", "TE"),
            ("IDP", "IDP"),
        ),
        default="QB",
        max_length=3,
    )
    height = models.PositiveSmallIntegerField()  # In inches
    weight = models.PositiveSmallIntegerField()  # In lbs
    college = models.CharField(null=True, max_length=128)
    nfl_draft_pick = models.PositiveSmallIntegerField()
    birthdate = models.DateTimeField()

    team = models.ForeignKey(
        Team, related_name="roster", null=False, on_delete=models.PROTECT
    )

    fantasy_teams = models.ManyToManyField(FantasyTeam, related_name="roster")

    @property
    def height_str(self) -> str:
        return f"{self.height // 12}ft {self.height % 12}in"

    @property
    def age(self):
        today = datetime.now(timezone.utc)
        return (today.year - self.birthdate.year) - (
            (today.month, today.day) < (self.birthdate.month, self.birthdate.day)
        )
