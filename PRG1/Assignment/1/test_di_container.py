import pytest

from adapter_manager import AdapterManager
from di_container import DIContainer, inject
from maze import Maze
from menu import Menu

class TestDIContainer:
    test_key = "Test"

    @pytest.mark.parametrize("test_input,expected", [
        (AdapterManager, AdapterManager),
        (Maze, Maze),
        (Menu, Menu)
    ])
    def test_dicontainer_add(self, test_input, expected):
        DIContainer.container = {}
        DIContainer.add(self.test_key, test_input)
        assert isinstance(DIContainer.get(self.test_key), expected)

    def test_dicontainer_add_override(self):
        DIContainer.container = {}
        test_value_initial = Maze
        test_value_override = AdapterManager
        DIContainer.container = {}
        DIContainer.add(self.test_key, test_value_initial)
        DIContainer.add(self.test_key, test_value_override)
        assert isinstance(DIContainer.get(self.test_key), Maze)


class TestDIContainerInject:
    test_key = "Test"

    @pytest.mark.parametrize("test_input,expected", [
        (AdapterManager, AdapterManager),
        (Maze, Maze),
        (Menu, Menu)
    ])
    def test_dicontainer_inject(self, test_input, expected):
        DIContainer.container = {}
        inject_return = inject(self.test_key, test_input)

        assert isinstance(inject_return, expected) and isinstance(DIContainer.get(self.test_key), expected)

    def test_dicontainer_inject_override(self):
        DIContainer.container = {}
        test_value_initial = Maze
        test_value_override = AdapterManager
        inject_return_initial = inject(self.test_key, test_value_initial)
        inject_return_override = inject(self.test_key, test_value_override)
        assert isinstance(inject_return_initial, Maze) and inject_return_initial == inject_return_override
