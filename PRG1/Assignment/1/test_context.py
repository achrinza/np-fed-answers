import pytest

from context import Ctx
from maze import Maze
from adapter_manager import AdapterManager

class TestContext:
    adapter_manager = AdapterManager()
    ctx = Ctx()
    maze = Maze()

    @pytest.mark.parametrize("test_input,expected", [
        ("Test", "Test"),
        (adapter_manager, adapter_manager),
        (maze, maze)
    ])
    def test_context_state(self, test_input, expected):
        self.ctx.state["Test"] = test_input
        assert self.ctx.state["Test"] == expected
