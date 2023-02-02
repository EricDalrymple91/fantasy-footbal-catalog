import pytest
from django.db import connection, reset_queries
from django.db.utils import IntegrityError
from django.test.utils import override_settings


class TestTeam:
    def test_create_team(self, team_factory):
        team = team_factory()
        assert team.name == "Portland Bad Apples"

    def test_create_duplicate_team_name_errors(self, team_factory):
        team_factory()
        with pytest.raises(IntegrityError):
            team_factory()

    @override_settings(DEBUG=True)
    def test_create_team_query_count(self, team_factory):
        reset_queries()
        team_factory(name="Query Counters")
        assert len(connection.queries) == 1


class TestFantasyLeague:
    def test_create_fantasy_league(self, fantasy_league_factory):
        league = fantasy_league_factory()
        assert league.name == "Ball Hall"
        assert league.start_year == 2010

    def test_create_fantasy_league_with_invalid_start_year_errors(
        self, fantasy_league_factory
    ):
        with pytest.raises(IntegrityError):
            fantasy_league_factory(start_year=2101)


class TestFantasyTeam:
    def test_create_fantasy_team(self, fantasy_team_factory):
        fantasy_team = fantasy_team_factory()
        assert fantasy_team.name == "Healing Juice"
        assert fantasy_team.league.name == "Ball Hall"


class TestPlayer:
    def test_create_player(self, player_factory):
        player = player_factory()
        assert player.first_name == "Dak"
        assert player.fantasy_teams.count() == 1
