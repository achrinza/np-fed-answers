from control_adapter import ControlAdapter
from control_adapter import ControlAdapterCalls
from control_adapter import ControlAdapterUserInputDirectionals
from adapter_manager import AdapterTypes

class ConsoleControlAdapter:
    ADAPTER_TITLE = "ConsoleControlAdapter"
    ADAPTER_TYPE = AdapterTypes.control

    def __init__(self):
        pass

    def call(self, args, kwargs):
        action = args[0]

        try:
            prompt = args[1]
        except Exception:
            prompt = ""

        if action == ControlAdapterCalls.get_userinput_directional:
            return self._get_userinput_directional(prompt)
        elif action == ControlAdapterCalls.get_userinput_string:
            return self._get_userinput_string(prompt)

    def _get_userinput_directional(self, prompt):
        user_input = self._get_userinput_string(prompt).upper()

        if user_input == "W":
            return ControlAdapterUserInputDirectionals.up
        elif user_input == "S":
            return ControlAdapterUserInputDirectionals.down
        elif user_input == "A":
            return ControlAdapterUserInputDirectionals.left
        elif user_input == "D":
            return ControlAdapterUserInputDirectionals.right
        else:
            return user_input


    def _get_userinput_string(self, prompt):
        return input(prompt)
