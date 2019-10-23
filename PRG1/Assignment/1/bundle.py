from abc import ABC
from abc import abstractmethod
import csv
import copy
import json
import os
import sys
try:
    from sense_hat import SenseHat
    sensehat_compat = True
except ModuleNotFoundError:
    sensehat_compat = False
import time

# START di_container.py

class DIContainerKeys:
    leaderboard = "DIRECT_LEADERBOARD"
    maze = "DIRECT_MAZE"
    menu = "DIRECT_MENU"
    character = "DIRECT_CHARACTER"
    
    display_manager = "MAANGER_DISPLAY"
    control_manager = "MANAGER_CONTROL"
    error_handler = "HANDLER_ERROR"

class DIContainer:
    container = {}

    def __init__(self):
        pass

    @classmethod
    def add(cls, key, injectable, *args, **kwargs):
        try:
            is_key_exists = cls.container[key]
            is_key_exists = True
        except KeyError:
            is_key_exists = False

        if not is_key_exists:
            cls.container[key] = injectable(*args, *kwargs)

    @classmethod
    def get(cls, key):
        return cls.container[key]


def inject(key, injectable, *args, **kwargs):
    DIContainer.add(key, injectable, *args, *kwargs)
    return DIContainer.get(key)

# END di_container.py

# START adapter_manager.py

class AdapterTypes():
    control = "CONTROL"
    display = "DISPLAY"

class AdapterManager():
    def __init__(self):
        # Initialize the adapter list
        self._adapters = []

    def add(self, adapter):
        # Check if an adapter has already been initialized
        if len(self._adapters) > 0:
            # Check if an incompatible adapter type is added
            if adapter.ADAPTER_TYPE != self._adapters[0]["type"]:
                raise TypeError("Adapter type mismatch.")

        self._adapters.append({
            "title": adapter.ADAPTER_TITLE,
            "type": adapter.ADAPTER_TYPE,
            "cls": adapter()
        })

    def flush(self):
        self._adapters = []

    def call(self, *args, **kwargs):
        for adapter_count, adapter in enumerate(self._adapters, 1):
            try:
                return adapter["cls"].call(args, kwargs)
            except Exception as e:
                # If all adapters have been exhausted and raised an error,
                # raise the last adapter's error.
                if adapter_count > len(self._adapters):
                    raise e

# END adapter_manager.py

# START adapter.py

class Adapter(ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    def call(self):
        raise NotImplementedError

# END adapter.py

# START control_adapter.py

class ControlAdapterCalls:
    def __init__(self):
        pass

    get_userinput_directional = "GET_USERINPUT_DIRECTIONAL"
    get_userinput_string = "GET_USERINPUT_STRING"

class ControlAdapterUserInputDirectionals:
    def __init__(self):
        pass

    up = "UP"
    down = "DOWN"
    left = "LEFT"
    right = "RIGHT"

class ControlAdapter(Adapter, ABC):
    ADAPTER_TYPE = "ControlAdapter"

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    def call(self):
        raise NotImplementedError

    @abstractmethod
    def _get_userinput_directional(self):
        raise NotImplementedError

    @abstractmethod
    def _get_userinput_string(self):
        raise NotImplementedError

# END control_adapter.py

# START display_adapter.py

class DisplayAdapterCalls:
    clear = "CLEAR"
    show_text = "SHOW_TEXT"
    show_maze = "SHOW_MAZE"

class DisplayAdapter(Adapter, ABC):
    ADAPTER_TYPE = "DisplayAdapter"
    
    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    def call(self):
        raise NotImplementedError

    @abstractmethod
    def _clear(self):
        raise NotImplementedError

    @abstractmethod
    def _show_text(self):
        raise NotImplementedError

    @abstractmethod
    def _show_maze(self):
        raise NotImplementedError

# END display_adapter.py

# START console_control_adapter.py

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

# END console_control_adapter.py

# START console_display_adapter.py

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

# END console_display_adapter.py

# START sensehat_control_adapter.py

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
                return ControlAdapterUserInputDirectionals.left
            elif user_input.direction == "down":
                return ControlAdapterUserInputDirectionals.right
            elif user_input.direction == "right":
                return ControlAdapterUserInputDirectionals.down
            elif user_input.direction == "left":
                return ControlAdapterUserInputDirectionals.up
            elif user_input.direction == "middle" and user_input.action == "held":
                return "M"
            else:
                return ""
        else:
            return ""


    def _get_userinput_string(self, prompt):
        raise NotImplementedError

# END sensehat_control_adapter.py

# START sensehat_display_adapter.py

class SensehatDisplayAdapter(DisplayAdapter):
    ADAPTER_TITLE = "SensehatDisplayAdapter"
    ADAPTER_TYPE = AdapterTypes.display

    def __init__(self):
        self._sensehat = SenseHat()
        self._maze = inject(DIContainerKeys.maze, Maze)
        self._sensehat.low_light = True

    def call(self, args, kwargs):
        action = args[0]
        action_data = args[1]
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
        layout = self._maze.render()

        if not(len(layout) == 8 and len(layout[0]) == 8):
            display_center = self._maze.character_coords
            display_start_delta = {
                "x": display_center["x"] - 8,
                "y": display_center["y"] - 8
            }
        else:
            display_start_delta = {
                "x": 0,
                "y": 0
            }

        for row_count, row in enumerate(layout):
            for pixel_count, pixel in enumerate(row):
                if row_count >= display_start_delta["x"] and \
                    pixel_count >= display_start_delta["y"]:
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

                self._sensehat.set_pixel(row_count - display_start_delta["x"], pixel_count - display_start_delta["y"], pixel_color)

# END sensehat_display_adapter.py

# START character.py

class CharacterDirectionals:
    up = "UP"
    down = "DOWN"
    left = "LEFT"
    right = "RIGHT"

# END character.py

# START maze.py

class MazeBlocks():
    wall = "X"
    ground = "O"
    character = "A"
    start_point = "A"
    end_point = "B"

class Maze:
    def __init__(self, layout = None, character_start_point_coords = {"x": 0, "y": 0}):
        self.start_point_coords = None
        self.end_point_coords = None
        self._layout = None

        if layout is None:
            self.load(self.generate(8, 8))
        else:
            self.load(layout)

        self.character_coords = {
            "x": character_start_point_coords["x"],
            "y": character_start_point_coords["y"]
        }

        self.character_move_count = 0

    def generate(self, width, height, **kwargs):
        try:
            character_coords = kwargs["character_coords"]
        except KeyError:
            character_coords = {
                "x": 0,
                "y": 0
            }

        try:
            end_point_coords = kwargs["end_point_coords"]
        except KeyError:
            end_point_coords = {
                "x": width - 1,
                "y": height - 1
            }

        layout = [["O" for i in range(width)] for i in range(height)]

        layout[character_coords["y"]][character_coords["x"]] = "A"
        layout[end_point_coords["y"]][end_point_coords["x"]] = "B"
        
        return layout

    def load(self, layout):
        self._layout = layout
        self.start_point_coords = None
        self.end_point_coords = None
        start_point_coords = None
        end_point_coords = None

        for maze_row_count, maze_row in enumerate(layout):
            try:
                start_point_coords = {"x": maze_row.index("A"), "y": maze_row_count}

                if self.start_point_coords is not None:
                    raise TypeError("Multiple start positions.")

                self.start_point_coords = start_point_coords
                self.character_god_teleport(start_point_coords["x"], start_point_coords["y"])
                self._layout[maze_row_count][maze_row.index("A")] = "O"
            except ValueError:
                if maze_row_count == len(layout):
                    raise TypeError("No start point position.")

            try:
                end_point_coords = {"x": maze_row.index("B"), "y": maze_row_count}
                
                if self.end_point_coords is not None:
                    raise TypeError("Multiple end positions.")

                self.end_point_coords = end_point_coords
                self._layout[maze_row_count][maze_row.index("B")] = "O"
            except ValueError:
                if maze_row_count == len(layout):
                    raise TypeError("No end point position.")

    def load_file(self, layout_file_path):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), layout_file_path)) as f:
            layout = []
            for line in list(csv.reader(f)):
                layout.append(list(line[0]))

            self.load(layout)

    def render(self):
        character_coords = self.character_coords
        layout_render = copy.deepcopy(self._layout)
        layout_render[character_coords["y"]][character_coords["x"]] = "A"
        layout_render[self.end_point_coords["y"]][self.end_point_coords["x"]] = "B"
        return layout_render

    def is_occupiable(self, item):
        if item == MazeBlocks.wall:
            return False
        else:
            return True

    def is_inbounds(self, x, y):
        if 0 <= x and 0 <= y and \
                len(self._layout) > y and len(self._layout[y]) > x:
            return True
        else:
            return False

    def export(self, export_path):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), export_path), "w") as f:
            for row in self.render():
                for char in row:
                    f.write(char)

                f.write("\n")

    def set_block(self, x, y, new_block):
        if new_block in [MazeBlocks.start_point, MazeBlocks.end_point]:
            raise TypeError("New block cannot be a start point or an end point block.")

        if self.is_inbounds(x, y):
            self._layout[y][x] = new_block
        else:
            raise IndexError("New block location is outside the map.")

    def set_startpoint_coords(self, x, y):
        if self.is_inbounds(x, y):
            self.start_point_coords = {
                "x": x,
                "y": y
            }
        else:
            raise IndexError("New start point position coordinates out of range.")

    def set_endpoint_coords(self, x, y):
        if self.is_inbounds(x, y):
            self.end_point_coords = {
                "x": x,
                "y": y
            }
        else:
            raise IndexError("New end point position coordinates out of range.")

    def character_move(self, direction):
        """
        Moves the character either UP, DOWN, LEFT or RIGHT.

        direction -- Takes in CharacterDirection()
        """
        maze_layout = self._layout

        future_coords = {
            "x": copy.deepcopy(self.character_coords["x"]),
            "y": copy.deepcopy(self.character_coords["y"])
        }

        if direction == CharacterDirectionals.up:
            future_coords["y"] = future_coords["y"] - 1
        elif direction == CharacterDirectionals.down:
            future_coords["y"] = future_coords["y"] + 1
        elif direction == CharacterDirectionals.left:
            future_coords["x"] = future_coords["x"] - 1
        elif direction == CharacterDirectionals.right:
            future_coords["x"] = future_coords["x"] + 1

        self.character_move_count += 1

        if not self.is_inbounds(future_coords["x"], future_coords["y"]):
            raise IndexError("Invalid move: Out of bounds")

        if self.is_occupiable(maze_layout[future_coords["y"]][future_coords["x"]]):
            self.character_coords = future_coords
        else:
            raise IndexError("Invalid move: Blocked path")

    def character_god_teleport(self, x, y):
        self.character_coords = {
            "x": x,
            "y": y
        }

    def character_won(self):
        if self.end_point_coords == self.character_coords:
            return True
        else:
            return False

    def character_reset(self):
        self.character_coords = self.start_point_coords
        self.character_move_count = 0

# END maze.py

# START menu.py

class Menu:
    def __init__(self):
        pass

    def render(self, menu):
        """Renders and returns a string of the rendered menu.

        Arguments:

        menu --> The menu object.

        Example menu object:

        {
            "meta": {
                "title": ""
            },
            "sections": [
                "meta": {
                    "title": ""
                },
                "items": [
                    {
                        "meta": {
                            "title": "Item title",
                            "key": "Item key"
                        }
                    }
                ]
            ]
        }
        """
        # Get the menu title.
        try:
            menu_title = menu["meta"]["title"]
        except KeyError:
            # If menu title not found, set to a default title.
            menu_title = "??????????"

        render = "\n" + menu_title
        render += "\n" + "=" * len(menu_title) + "\n"

        # Loop through each section
        item_count_offset = 1
        for section in menu["sections"]:
            try:
                section_title = section["meta"]["title"]
            except KeyError:
                section_title = ""

            if section_title != "":
                render += f"{section_title}\n"
                render += "-" * len(section_title) + "\n"

            for item in section["items"]:
                try:
                    item_key = item["meta"]["key"]
                except KeyError:
                    item_key = item_count_offset
                    item_count_offset += 1

                item_title = item["meta"]["title"]

                render += f"[{item_key}] {item_title}\n"

            render += "\n"

        return render

# END menu.py

# START error_handler.py

class ErrorHandler:
    def __init__(self):
        self.display_manager = inject(DIContainerKeys.display_manager, AdapterManager)

    def new_error(self, error, errorPretty = "See FULL ERROR below."):
        error_msg = f"ERROR ====================\n{errorPretty}"
        if error != "":
            error_msg += f"\nFULL ERROR ==========\n{error}"
                
        error_msg += "\n=========================="
        return self.display_manager.call(DisplayAdapterCalls.show_text, error_msg)

# END error_handler.py

# START leaderboard.py

class Leaderboard:
    def __init__(self, filename):
        self._filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)
        self._load_file()
        self._score_init = 1000
        self._maze = inject(DIContainerKeys.maze, Maze)

    def add_entry(self, name, duration, step_count, medium):
        """Adds a "score" entry to the scoreboard

        name = The person's name
        duration = The number of seconds the game ran for
        step_count = How many steps (including invalid steps) taken during the game
        """

        # Get the currently-loaded maze layout
        maze_layout = self._maze.render()

        # Check if the maze layout has already been added to the leaderboard.
        is_board_exists = False

        for board in self._board:
            if board["layout"] == maze_layout:
                is_board_exists = True

        # If maze layout does not exist on scoreboard,
        # Add it to the scoreboard.
        if not is_board_exists:
            self._board.append({
                "layout": maze_layout,
                "scores": []
            })

        # Go through each maze layout (AKA "board")
        # and find the matching board.
        # Then append the new "score" entry.
        for board_count, board in enumerate(self._board):
            if board["layout"] == maze_layout:
                self._board[board_count]["scores"].append({
                    "name": name,
                    "duration": duration,
                    "step_count": step_count,
                    "medium": medium
                })

        self._write_file()

    def _load(self, board):
        board.sort(key = lambda board: sum([len(row) for row in board["layout"]]))
        self._board = board

    def get_layout(self, layout_id):
        if 0 < layout_id:
            return self._board[layout_id - 1]["layout"]
        else:
            raise IndexError("Out of range.")

    def _load_file(self):
        try:
            with open(self._filepath) as f:
                fdata = json.loads(f.read())
                if 1 <= fdata["meta"]["version"] < 2:
                    self._load(fdata["leaderboard"])
                else:
                    raise TypeError("Incompatible leaderboard file version.")
        except TypeError as e:
            raise e
        except Exception as e:
            # raise e
            raise TypeError("Corrupted leaderboard file.")
            # self._load([])

    def _write_file(self):
        with open(self._filepath, "w") as f:
            # Convert the list into a dict. to prepare for export to JSON.
            board = {
                "meta": {
                    "version": 1
                },
                "leaderboard": self._board
            }
            f.writelines(json.dumps(board))

    def render(self, **kwargs):
        self._load_file()

        try:
            load_scores = kwargs["load_scores"]
        except KeyError:
            load_scores = True

        if self._board == []:
            return "No leaderboard."

        board_render = "\nLEADERBOARD"

        for board_count, board in enumerate(self._board):
            board_render += "\n\n" + "=" * 77 + "\n\n"
            board_render += "({}) ".format(board_count + 1)
            if board["layout"] == self._maze.render():
                board_render += "(Currently loaded board)"

            board_render += "\n\n"
            
            for row in board["layout"]:
                board_render += "{}\n".format(row)

            if load_scores:
                board_render += "\n{:25} | {:<10} | {:<10} | {:<10} | {:<10}\n".format("Name", "Time (s)", "Steps", "Score", "Medium")
                board_render += "-" * 25 + "-+-" + "-" * 10 + "-+-" + "-" * 10 + "-+-" + "-" * 10 + "-+-" + "-" * 10
                board["scores"].sort(key = lambda score: self._calc_score(score["duration"], score["step_count"]), reverse = True)
                
                for entry in board["scores"]:
                    name = entry["name"]
                    duration = entry["duration"]
                    step_count = entry["step_count"]
                    medium = entry["medium"]
                    score = self._calc_score(entry["duration"], entry["step_count"])

                    # Some aesthetics checks
                    if score < 0:
                        score = "< 0"

                    if len(name) > 25:
                        name = name[:22] + "..."

                    if duration > 99999999:
                        duration = "99999999+"

                    if step_count > 99999999:
                        step_count = "99999999+"

                    if medium == 1:
                        medium = "Console"
                    elif medium == 2:
                        medium = "Sensehat"
                    else:
                        medium = "N/A"

                    board_render += "\n{:25} | {:>10} | {:>10} | {:>10} | {:10}".format(name, duration, step_count, score, medium)

        board_render += "\n\n" + "=" * 77 + "\n"

        return board_render

    def _calc_score(self, duration, step_count):
        return self._score_init - 10 * step_count - 1 * duration

# END learboard.py

# START game.py

class GameEscapeCodes:
    main_menu = "ESCAPECODE_MAINMENU"
    maze_config_menu = "ESCAPECODE_CONFIGMENU"
    

class Game:
    """

    - Dependency Breakdown -

    AdapterManager - Manages the adapters used. For example, the adapter manager can manage which DisplayAdapter is used to show maze/text/etc. (Console or Sensehat) based on their priority.

    DisplayManager - Instance of AdapterManager; Manages specifically the DisplayAdapters (The thing that shows stuff).

    ControlManager - Instance of AdapterManager; Manages specifically the ControlAdapters (The thing that gets user input).

    Menu - Renders a standardised menu layout based on the provided menu object/dict.

    Character - Manages the movement, win status, step history and everything else about the game's character.

    Maze - Manages the loading, storing, export, modification, validation and everything else about the game's maze

    Leaderboard - Manages the leaderboard.
    """

    def __init__(self):
        self._leaderboard_filename = "leaderboard.json"
        self._auth_code_admin = None

        print("MAZE GAME BOOTSRAPPER ---------")
        print("ENV STATUS CHECK -----")
        print("Admin Auth Code - " + ("ENABLED" if self._auth_code_admin is not None else "DISABLED"))
        print("SenseHat - " + ("ENABLED" if sensehat_compat else "DISABLED"))
        print("Leaderboard - " + self._leaderboard_filename)
        print("----------------------")

        # Initialization of ControlManager and DisplayManager

        self._control_manager = inject(DIContainerKeys.control_manager, AdapterManager)
        self._control_manager.add(ConsoleControlAdapter)
        self._display_manager = inject(DIContainerKeys.display_manager, AdapterManager)
        self._display_manager.add(ConsoleDisplayAdapter)

        # Initialization of other deps.

        self._error_handler = inject(DIContainerKeys.error_handler, ErrorHandler)

        self._maze = inject(DIContainerKeys.maze, Maze)
        self._menu = inject(DIContainerKeys.menu, Menu)
        
        # Leaderboard init.
        # Handles "corrupted" leaderboard files.
        self._leaderboard = None
        self._leaderboard_compat = False
        while self._leaderboard is None:
            try:
                self._leaderboard = inject(DIContainerKeys.leaderboard, Leaderboard, self._leaderboard_filename)
                self._leaderboard_compat = True
            except TypeError as e:
                self._error_handler.new_error(e)
                menu_obj = {
                    "meta": {
                        "title": "LEADERBOARD LOAD FAIL RESOLVER MENU"
                    },
                    "sections": [
                        {
                            "items": [
                                {
                                    "meta": {
                                        "title": "Disable leaderboard",
                                        "key": "D"
                                    }
                                },
                                {
                                    "meta": {
                                        "title": "Reset leaderboard",
                                        "key": "R"
                                    }
                                }
                            ]
                        }
                    ]
                }
                user_choice = None
                while user_choice is None:
                    self._display_manager.call(DisplayAdapterCalls.show_text, "\nThere was an issue with loading the leaderboard. (Check error above)")
                    menu_render = self._menu.render(menu_obj)
                    self._display_manager.call(DisplayAdapterCalls.show_text, menu_render)
                    user_choice = self._control_manager.call(ControlAdapterCalls.get_userinput_string, "Enter option: ").upper()

                    if user_choice == "D":
                        self._leaderboard_compat = False
                        self._leaderboard = "DISABLED"
                    elif user_choice == "R":
                        user_choice = self._control_manager.call(ControlAdapterCalls.get_userinput_string, "Are you sure? [Y/N] ").upper()

                        if user_choice == "Y":
                            # Overwrite leaderboard file.
                            with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), self._leaderboard_filename), "w") as f:
                                f.writelines(json.dumps({
                                    "meta": {
                                        "version": 1
                                    },
                                    "leaderboard": []
                                }))
                        else:
                            user_choice = None
                    else:
                        self._error_handler.new_error("Invalid user input")

    def start(self):
        """Game ticker
        
        Runs the game indefinitely. 
        """

        while True:
            try:
                self._main_menu()
            except KeyboardInterrupt:
                if self._auth_code_admin is not None:
                    print()
                    print("AUTHORIZATION ==========")
                    try:
                        auth_code = input("ADMIN AUTH CODE: ")
                    except KeyboardInterrupt:
                        print()
                        auth_code = None
                    if auth_code == self._auth_code_admin:
                        sys.exit()
                    else:
                        print("INVALID ADMIN AUTH CODE")
                else:
                    print()
                    print("=================")
                    print("KeyboardInterrupt")
                    print("Exiting...")
                    print("=================")
                    sys.exit()

    def _main_menu(self):
        """Provides the user the main menu options and runs the respective functions
        """

        # The menu object for "main menu"
        menu_dict = {
            "meta": {
                "title": "MAIN MENU"
            },
            "sections": [
                {
                    "items": [
                        {
                            "meta": {
                                "title": "Read and load maze from file"
                            },
                            "function": self._maze_load_file
                        },
                        {
                            "meta": {
                                "title": "View maze"
                            },
                            "function": self._maze_render
                        },
                        {
                            "meta": {
                                "title": "Play maze game",
                            },
                            "function": self._maze_play
                        },
                        {
                            "meta": {
                                "title": "Configure current maze"
                            },
                            "function": self._maze_configure
                        },
                        {
                            "meta": {
                                "title": "Export maze to file",
                            },
                            "function": self._maze_export
                        },
                        {
                            "meta": {
                                "title": "Create new maze",
                            },
                            "function": self._maze_generate
                        },
                        {
                            "meta": {
                                "title": ("[DISABLED] " if not sensehat_compat else "") + "Play maze using SenseHAT"
                            },
                            "function": self._maze_play_sensehat
                        },
                        {
                            "meta": {
                                "title": ("[DISABLED] " if not self._leaderboard_compat else "") + "View Leaderboard"
                            },
                            "function": self._leaderboard_view
                        }
                    ]
                },
                {
                    "items": [
                        {
                            "meta": {
                                "title": "Exit",
                                "key": 0
                            }
                        }
                    ]
                },
                # {
                #     "meta": {
                #         "title": "Extras"
                #     },
                #     "items": [
                #         {
                #             "meta": {
                #                 "title": "Load maze from leaderboard"
                #             },
                #             "function": self._maze_load_leaderboard
                #         }
                #     ]
                # }
            ]
        }

        # Get the menu render from Menu
        menu_render = self._menu.render(menu_dict)

        # Keep prompting the user for a choice until a valid value is keyed.
        user_choice = None
        while user_choice is None:
            # Use DisplayManager to call "show_text" to show menu render
            self._display_manager.call(DisplayAdapterCalls.show_text, menu_render)

            try:
                user_choice = int(self._control_manager.call(ControlAdapterCalls.get_userinput_string, "Enter your option: ")) - 1
            except ValueError as e:
                self._error_handler.new_error(e, "Invalid user option; Non-int.")
                continue
            
            # Check if the user choice is "exit"
            if user_choice == -1:
                sys.exit()
            
            # Check if user choice is within range of first menu section
            elif user_choice < len(menu_dict["sections"][0]["items"]):
                menu_dict["sections"][0]["items"][user_choice]["function"]()

            # # Check if user choice is within range of third menu section.
            # elif user_choice < len(menu_dict["sections"][0]["items"]) + len(menu_dict["sections"][2]["items"]):
            #     menu_dict["sections"][2]["items"][user_choice - len(menu_dict["sections"][0]["items"])]["function"]()
            else:
                self._error_handler.new_error("", "Invalid user option; Out of range.")

    def _maze_render(self):
        maze_render = self._maze.render()
        self._display_manager.call(DisplayAdapterCalls.show_maze, maze_render)

    def _maze_load_file(self):
        self._display_manager.call(DisplayAdapterCalls.show_text, "Option [1] Read and load maze from file\n")
        file_path = self._control_manager.call(ControlAdapterCalls.get_userinput_string, "Enter the name of the data file: ")
        try:
            self._maze.load_file(file_path)
            self._display_manager.call(DisplayAdapterCalls.show_text, f"Number of lines read: {len(self._maze._layout)}")
        except Exception as e:
            self._error_handler.new_error(e, "Could not load file!")

    def _maze_generate(self):
        x, y = list(map(int, self._control_manager.call(ControlAdapterCalls.get_userinput_string, "Enter new maze dimensions (x, y): ").split(",")))
        
        return self._maze.load(self._maze.generate(x, y))

    def _maze_export(self):
        export_path = self._control_manager.call(ControlAdapterCalls.get_userinput_string, "Enter filename to save to: ")
        try:
            return self._maze.export(export_path)
        except FileNotFoundError as e:
            self._error_handler.new_error(e, "Error exporting maze.")
        except OSError as e:
            self._error_handler.new_error(e, "Error exporting maze.")

    def _maze_play(self, controls_menu = None, game_medium = 1):
        if controls_menu is None:
            controls_menu = {
                "meta": {
                    "title": "CONTROLS"
                },
                "sections": [
                    {
                        "items": [
                            {
                                "meta": {
                                    "title": "UP",
                                    "key": "W"
                                }
                            },
                            {
                                "meta": {
                                    "title": "DOWN",
                                    "key": "A"
                                }
                            },
                            {
                                "meta": {
                                    "title": "LEFT",
                                    "key": "S"
                                }
                            },
                            {
                                "meta": {
                                    "title": "RIGHT",
                                    "key": "D"
                                }
                            }
                        ]
                    },
                    {
                        "items": [
                            {
                                "meta": {
                                    "title": "MAIN MENU",
                                    "key": "M"
                                }
                            }
                        ]
                    }
                ]
            }

        game_start_time = time.time()
        while not self._maze.character_won():
            self._maze_render()
            menu_render = self._menu.render(controls_menu)
            self._display_manager.call(DisplayAdapterCalls.show_text, menu_render)
            user_direction = self._control_manager.call(ControlAdapterCalls.get_userinput_directional)

            try:
                if user_direction == ControlAdapterUserInputDirectionals.up:
                    self._maze.character_move(CharacterDirectionals.up)
                elif user_direction == ControlAdapterUserInputDirectionals.down:
                    self._maze.character_move(CharacterDirectionals.down)
                elif user_direction == ControlAdapterUserInputDirectionals.left:
                    self._maze.character_move(CharacterDirectionals.left)
                elif user_direction == ControlAdapterUserInputDirectionals.right:
                    self._maze.character_move(CharacterDirectionals.right)
            except IndexError as e:
                self._display_manager.call(DisplayAdapterCalls.show_text, e)

            if user_direction not in [
                        CharacterDirectionals.up,
                        CharacterDirectionals.down,
                        CharacterDirectionals.left,
                        CharacterDirectionals.right
                    ]:
                if user_direction.upper() == "M":
                    self._maze.character_reset()
                    return GameEscapeCodes.main_menu

        game_end_time = time.time()
        # Get the character move count before reset
        character_move_count = self._maze.character_move_count
        # Reset to get original maze layout for scoreboard and reset maze for next game.
        self._maze.character_reset()

        if self._leaderboard_compat:
            leaderboard_name = self._control_manager.call(ControlAdapterCalls.get_userinput_string, "Enter your name: ")
            self._leaderboard.add_entry(leaderboard_name, int(game_end_time) - int(game_start_time), character_move_count, game_medium)

    def _maze_play_sensehat(self):
        if not sensehat_compat:
            return self._error_handler.new_error("SenseHat module not initialised!")

        menu_obj = {
            "meta": {
                "title": "SENSEHAT CONTROLS"
            },
            "sections": [
                {
                    "items": [
                        {
                            "meta": {
                                "title": "UP",
                                "key": "JOYSTICK UP"
                            }
                        },
                        {
                            "meta": {
                                "title": "DOWN",
                                "key": "JOYSTICK DOWN"
                            }
                        },
                        {
                            "meta": {
                                "title": "LEFT",
                                "key": "JOYSTICK LEFT"
                            }
                        },
                        {
                            "meta": {
                                "title": "RIGHT",
                                "key": "JOYSTICK RIGHT"
                            }
                        }
                    ]
                },
                {
                    "items": [
                        {
                            "meta": {
                                "title": "MAIN MENU",
                                "key": "JOYSTICK LONG PRESS"
                            }
                        }
                    ]
                }
            ]
        }
        self._control_manager.flush()
        self._control_manager.add(SensehatControlAdapter)
        self._control_manager.add(ConsoleControlAdapter)
        self._display_manager.flush()
        self._display_manager.add(SensehatDisplayAdapter)
        self._display_manager.add(ConsoleDisplayAdapter)
        self._maze_play(menu_obj, 2)
        self._display_manager.call(DisplayAdapterCalls.clear)
        self._control_manager.flush()
        self._control_manager.add(ConsoleControlAdapter)
        self._display_manager.flush()
        self._display_manager.add(ConsoleDisplayAdapter)

    def _maze_configure(self):
        while True:
            configure_menu_options = {
                "meta": {
                    "title": "CONFIGURATION MENU"
                },
                "sections": [
                    {
                        "items": [
                            {
                                "meta": {
                                    "title": "Create wall"
                                },
                                "function": self._maze_configure_add_wall
                            },
                            {
                                "meta": {
                                    "title": "Create passageway"
                                },
                                "function": self._maze_configure_add_passageway
                            },
                            {
                                "meta": {
                                    "title": "Create start point"
                                },
                                "function": self._maze_configure_set_startpoint
                            },
                            {
                                "meta": {
                                    "title": "Create end point"
                                },
                                "function": self._maze_configure_set_endpoint
                            }
                        ]
                    },
                        {
                            "items": [
                                {
                                    "meta": {
                                        "title": "Exit to Main Menu",
                                        "key": "0"
                                    }
                                }
                            ]
                        }
                ]
            }


            user_option = None

            while user_option is None:
                maze_layout = self._maze.render()
                self._display_manager.call(DisplayAdapterCalls.show_maze, maze_layout)

                menu_render = self._menu.render(configure_menu_options)
                self._display_manager.call(DisplayAdapterCalls.show_text, menu_render)

                try:
                    user_option = int(self._control_manager.call(ControlAdapterCalls.get_userinput_string)) - 1
                except ValueError:
                    self._error_handler.new_error("Invalid user option")
                    user_option = None
                    continue

                if user_option == -1:
                    return GameEscapeCodes.main_menu

                if user_option <= len(configure_menu_options["sections"][0]["items"]):
                    submenu_user_option = configure_menu_options["sections"][0]["items"][user_option]["function"]()
                else:
                    self._error_handler.new_error("", "Invalid user option; Out of range.")
                    user_input = None
                    continue

                if submenu_user_option == GameEscapeCodes.main_menu:
                    return submenu_user_option

    def _maze_configure_option_menu(self, menu_title = "??????????"):
        configure_option_menu_options = {
            "meta": {
                "title": menu_title + " CONFIG MENU"
            },
            "sections": [
                {
                    "items": [
                        {
                            "meta": {
                                "title": "Enter the coordinates of the item you wish to change",
                                "key": "row , column"
                            }
                        },
                        {
                            "meta": {
                                "title": "Return to Configuration Menu",
                                "key": "B"
                            }
                        },
                        {
                            "meta": {
                                "title": "Return to the main menu",
                                "key": "M"
                            }
                        }
                    ]
                }
            ]
        }

        user_option = None
        while user_option is None:
            self._maze_render()
            menu_render = self._menu.render(configure_option_menu_options)
            self._display_manager.call(DisplayAdapterCalls.show_text, menu_render)

            user_option = self._control_manager.call(ControlAdapterCalls.get_userinput_string).upper()

            if user_option == "B":
                return GameEscapeCodes.maze_config_menu
            elif user_option == "M":
                return GameEscapeCodes.main_menu
            else:
                try:
                    return user_option.split(",")
                except TypeError:
                    user_option = None

    def _maze_configure_add_wall(self):
        user_option = self._maze_configure_option_menu("ADD WALL")

        if user_option in [GameEscapeCodes.main_menu, GameEscapeCodes.maze_config_menu]:
            return user_option

        self._maze.set_block(int(user_option[0]), int(user_option[1]), MazeBlocks.wall)

    def _maze_configure_add_passageway(self):
        user_option = self._maze_configure_option_menu("ADD PASSAGEWAY")

        if user_option in [GameEscapeCodes.main_menu, GameEscapeCodes.maze_config_menu]:
            return user_option

        self._maze.set_block(int(user_option[0]), int(user_option[1]), MazeBlocks.ground)

    def _maze_configure_set_startpoint(self):
        user_option = self._maze_configure_option_menu("SET STARTPOINT")

        if user_option in [GameEscapeCodes.main_menu, GameEscapeCodes.maze_config_menu]:
            return user_option

        self._maze.set_startpoint_coords(int(user_option[0]), int(user_option[1]))

    def _maze_configure_set_endpoint(self):
        user_option = self._maze_configure_option_menu("SET ENDPOINT")

        if user_option in [GameEscapeCodes.main_menu, GameEscapeCodes.maze_config_menu]:
            return user_option

        self._maze.set_endpoint_coords(int(user_option[0]), int(user_option[1]))

    def _leaderboard_view(self):
        if not self._leaderboard_compat:
            self._error_handler.new_error("Leaderboard disabled - Restart program to resolve the issue.", "Leaderboard disabled!", )
            return

        try:
            leaderboard_render = self._leaderboard.render()
            return self._display_manager.call(DisplayAdapterCalls.show_text, leaderboard_render)
        except TypeError as e:
            self._error_handler.new_error(e, "Failed to load leaderboard - This is usually caused by the leaderboard being modified while the game is running.")
            self._leaderboard_compat = False

    def _maze_load_leaderboard(self):
        leaderboard_render = self._leaderboard.render(load_scores = False)

        user_choice = None
        while user_choice is None:
            self._display_manager.call(DisplayAdapterCalls.show_text, leaderboard_render)
            try:
                user_choice = int(self._control_manager.call(ControlAdapterCalls.get_userinput_string, "Maze layout number (-1 to exit): "))
            except ValueError:
                self._error_handler.new_error("Invalid user input; Non-int.")

            if user_choice == -1:
                return GameEscapeCodes.main_menu

            try:
                self._maze.load(self._leaderboard.get_layout(user_choice))
            except IndexError:
                self._error_handler.new_error("Invalid user input; Out of range")
                user_choice = None

# END game.py

# START main.py

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    try:
        main()

    # Catch the earliest KeyboardInterrupt that Game() couldn't catch.
    except KeyboardInterrupt:
        print()
        print("=======================")
        print("Early KeyboardInterrupt")
        print("Exiting...")
        print("=======================")

# END main.py