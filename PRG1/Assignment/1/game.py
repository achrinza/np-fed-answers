import json
import os
import sys
import time

from di_container import DIContainerKeys, inject

from error_handler import ErrorHandler

from character import CharacterDirectionals
from leaderboard import Leaderboard
from maze import Maze
from maze import MazeBlocks
from menu import Menu

from adapter_manager import AdapterManager

from control_adapter import ControlAdapterCalls, \
    ControlAdapterUserInputDirectionals
from console_control_adapter import ConsoleControlAdapter

from display_adapter import DisplayAdapterCalls
from console_display_adapter import ConsoleDisplayAdapter

try:
    from sensehat_control_adapter import SensehatControlAdapter
    from sensehat_display_adapter import SensehatDisplayAdapter
    sensehat_compat = True
except ModuleNotFoundError:
    sensehat_compat = False

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
                {
                    "meta": {
                        "title": "Extras"
                    },
                    "items": [
                        {
                            "meta": {
                                "title": "Load maze from leaderboard"
                            },
                            "function": self._maze_load_leaderboard
                        }
                    ]
                }
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

            # Check if user choice is within range of third menu section.
            elif user_choice < len(menu_dict["sections"][0]["items"]) + len(menu_dict["sections"][2]["items"]):
                menu_dict["sections"][2]["items"][user_choice - len(menu_dict["sections"][0]["items"])]["function"]()

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
        try:
            x, y = list(map(int, self._control_manager.call(ControlAdapterCalls.get_userinput_string, "Enter new maze dimensions (x, y): ").split(",")))
        except:
            self._error_handler.new_error("Invalid coordinates")

        try:
            return self._maze.load(self._maze.generate(x, y))
        except Exception as e:
            self._error_handler.new_error("Failed to generate maze")

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

        try:
            self._maze.set_block(int(user_option[0]), int(user_option[1]), MazeBlocks.wall)
        except Exception as e:
            self._error_handler.new_error(e, "Failed to add block")

    def _maze_configure_add_passageway(self):
        user_option = self._maze_configure_option_menu("ADD PASSAGEWAY")

        if user_option in [GameEscapeCodes.main_menu, GameEscapeCodes.maze_config_menu]:
            return user_option

        try:
            self._maze.set_block(int(user_option[0]), int(user_option[1]), MazeBlocks.ground)
        except Exception as e:
            self._error_handler.new_error(e, "Failed to add block")

    def _maze_configure_set_startpoint(self):
        user_option = self._maze_configure_option_menu("SET STARTPOINT")

        if user_option in [GameEscapeCodes.main_menu, GameEscapeCodes.maze_config_menu]:
            return user_option

        try:
            self._maze.set_startpoint_coords(int(user_option[0]), int(user_option[1]))
        except Exception as e:
            self._error_handler.new_error(e, "Failed to add block")

    def _maze_configure_set_endpoint(self):
        user_option = self._maze_configure_option_menu("SET ENDPOINT")

        if user_option in [GameEscapeCodes.main_menu, GameEscapeCodes.maze_config_menu]:
            return user_option

        try:
            self._maze.set_endpoint_coords(int(user_option[0]), int(user_option[1]))
        except Exception as e:
            self._error_handler.new_error(e, "Failed to add block")

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
                self._error_handler.new_error("Invalid user input; Out of range.")
                user_choice = None
            except TypeError:
                self._error_handler.new_error("Invalid user input; Non-int.")
                user_choice = None
