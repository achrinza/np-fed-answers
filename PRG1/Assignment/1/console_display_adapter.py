from display_adapter import DisplayAdapter
from display_adapter import DisplayAdapterCalls
from adapter_manager import AdapterTypes

class ConsoleDisplayAdapter(DisplayAdapter):
    ADAPTER_TITLE = "ConsoleDisplayAdapter"
    ADAPTER_TYPE = AdapterTypes.display

    def __init__(self):
        pass

    def call(self, args, kwargs):
        action = args[0]
        action_data = args[1]
        if action == DisplayAdapterCalls.clear:
            return self._clear()
        elif action == DisplayAdapterCalls.show_text:
            return self._show_text(action_data)
        elif action == DisplayAdapterCalls.show_maze:
            return self._show_maze(action_data)

    def _clear(self):
        raise NotImplementedError

    def _show_text(self, text):
        print(text)

    def _show_maze(self, layout):
        for row in layout:
            print(row)
