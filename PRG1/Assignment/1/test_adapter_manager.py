import pytest

from adapter import Adapter
from adapter_manager import AdapterManager

class DummyAdapter(Adapter):
    ADAPTER_TITLE = "PytestDummyAdapter"
    ADAPTER_TYPE = "DummyAdapter"

    def __init__(self):
        pass

    def call(self, args, kwargs):
        if len(args) > 0:
            return args[0]
        else:
            return kwargs

class TestAdapterManager():
    adapter_manager = AdapterManager()

    def test_add_args(self):
        self.adapter_manager.add(DummyAdapter)
        assert self.adapter_manager.call("FOOBAR") == "FOOBAR"

    def test_add_kwargs(self):
        self.adapter_manager.add(DummyAdapter)
        assert self.adapter_manager.call(FOO="BAR")["FOO"] == "BAR"

    def test_flush(self):
        self.adapter_manager.flush()
        assert self.adapter_manager.call() is None
