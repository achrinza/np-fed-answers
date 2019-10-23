from display_adapter import DisplayAdapter
from display_adapter import DisplayAdapterCalls
from adapter_manager import AdapterTypes
from di_container import DIContainerKeys,inject
from maze import Maze
from sense_hat import SenseHat

class SensehatDisplayAdapter(DisplayAdapter):
    ADAPTER_TITLE = "SensehatDisplayAdapter"
    ADAPTER_TYPE = AdapterTypes.display

    def __init__(self):
        self._sensehat = SenseHat()
        self._maze = inject(DIContainerKeys.maze, Maze)
        self._sensehat.low_light = True

    def call(self, args, kwargs):
        action = args[0]
        try:
            action_data = args[1]
        except:
            action_data = None

        if action == DisplayAdapterCalls.clear:
            self._clear()
        elif action == DisplayAdapterCalls.show_text:
            self._show_text(action_data)
        elif action == DisplayAdapterCalls.show_maze:
            self._show_maze(action_data)

    def _clear(self):
        self._sensehat.clear()

    def _show_text(self, text):
        raise NotImplementedError

    def _show_maze(self, layout):
        self._clear()
        layout = self._maze.render()

        if not(len(layout) == 8 and len(layout[0]) == 8):
            display_center = self._maze.character_coords
            display_start_delta = {
                "x": display_center["x"] - 4,
                "y": display_center["y"] - 4
            }
        else:
            display_start_delta = {
                "x": 0,
                "y": 0
            }

        for row_count, row in enumerate(layout):
            for pixel_count, pixel in enumerate(row):
                if row_count >= display_start_delta["y"] and \
                    pixel_count >= display_start_delta["x"] and \
                    row_count - display_start_delta["y"] <= 7 and \
                    pixel_count - display_start_delta["x"] <= 7:
                    if pixel == "O":
                        pixel_color = (0, 0, 0)
                    elif pixel == "X":
                        pixel_color = (190, 190, 190)
                    elif pixel == "A":
                        pixel_color = (0, 255, 0)
                    elif pixel == "B":
                        pixel_color = (0, 0, 255)
                    else:
                        pixel_color = (0, 0, 0)

                # if row_count - display_start_delta["y"] > 7 or \
                #     pixel_count - display_start_delta["x"] > 7:
                #     pixel_color = (190, 190, 190)

                    self._sensehat.set_pixel(pixel_count - display_start_delta["x"], row_count - display_start_delta["y"], pixel_color)
