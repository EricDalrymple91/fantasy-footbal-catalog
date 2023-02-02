import pendulum
import pytest

from fantasy_football_catalog.apps.catalog.models import (
    FantasyLeague,
    FantasyTeam,
    Player,
    Team,
)


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture
def team_factory():
    class Factory:
        def __call__(self, name="Portland Bad Apples"):
            return Team.objects.create(name=name)

    return Factory()


@pytest.fixture
def fantasy_league_factory():
    class Factory:
        def __call__(self, name="Ball Hall", start_year=2010):
            return FantasyLeague.objects.create(name=name, start_year=start_year)

    return Factory()


@pytest.fixture
def fantasy_team_factory(fantasy_league_factory):
    class Factory:
        def __call__(self, name="Healing Juice"):
            league = fantasy_league_factory()
            return FantasyTeam.objects.create(name=name, league=league)

    return Factory()


@pytest.fixture
def player_factory(team_factory, fantasy_team_factory):
    class Factory:
        def __call__(self, **kwargs):
            team = team_factory()
            fantasy_team = fantasy_team_factory()
            player = Player.objects.create(
                first_name="Dak",
                last_name="Prescott",
                position="QB",
                height=74,
                weight=238,
                college="Mississippi State",
                nfl_draft_pick=135,
                birthdate=pendulum.datetime(1993, 7, 29),
                team=team,
            )
            player.fantasy_teams.add(fantasy_team)
            return player

    return Factory()
