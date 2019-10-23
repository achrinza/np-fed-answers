from control_adapter import ControlAdapter
from control_adapter import ControlAdapterCalls
from control_adapter import ControlAdapterUserInputDirectionals
from adapter_manager import AdapterTypes
from sense_hat import SenseHat

class SensehatControlAdapter:
    ADAPTER_TITLE = "SensehatControlAdapter"
    ADAPTER_TYPE = AdapterTypes.control

    def __init__(self):
        self._sense = SenseHat()

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
        user_input = self._sense.stick.wait_for_event()
        print(user_input.direction)

        if user_input.action in ["pressed", "held"]:
            if user_input.direction == "up":
                return ControlAdapterUserInputDirectionals.up
                # return ControlAdapterUserInputDirectionals.left
            elif user_input.direction == "down":
                return ControlAdapterUserInputDirectionals.down
                # return ControlAdapterUserInputDirectionals.right
            elif user_input.direction == "right":
                return ControlAdapterUserInputDirectionals.right
                # return ControlAdapterUserInputDirectionals.down
            elif user_input.direction == "left":
                return ControlAdapterUserInputDirectionals.left
                # return ControlAdapterUserInputDirectionals.up
            elif user_input.direction == "middle" and user_input.action == "held":
                return "M"
            else:
                return ""
        else:
            return ""


    def _get_userinput_string(self, prompt):
        raise NotImplementedError
