import pytest

from di_container import DIContainerKeys, inject
from adapter_manager import AdapterManager, AdapterTypes
from game import Game

class PytestDisplayAdapter:
    ADAPTER_TITLE = "PytestDisplayAdapter"
    ADAPTER_TYPE = AdapterTypes.display

    def call(self, *args, **kwargs):
        pass


class TestGame:
    game = Game()
    
    def test_game_start(self):
        assert callable(self.game.start)
