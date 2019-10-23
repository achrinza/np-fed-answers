class CtxStates:
    leaderboard = "DIRECT_LEADERBOARD"
    maze = "DIRECT_MAZE"
    menu = "DIRECT_MENU"
    
    display_manager = "MAANGER_DISPLAY"
    control_manager = "MANAGER_CONTROL"
    error_handler = "HANDLER_ERROR"


class Ctx:
    """Context & World State

    This class simply handles storing the "World State".

    The "World State" is a "global" variable that can be
    accessed anywhere in the program. This allows for
    different parts of the programme to access each other.

    This means that the "Game" class will initialize
    everything into the "World State" and the other
    classes will just read "known variables" from the
    "World State".

    For example, when "Game" initializes the "Maze"
    class, The "Maze" will be stored under
    Ctx().state["maze"], where all of its methods and
    variables are accessible by other parts of the
    programme that know how and need to interact with
    Maze.

    For example, the "Maze" class will be able to call
    Character().position to find the current location of
    the character when Maze().render() is called.

    This works the other way too! The "Character" class
    will be able to call Maze().layout() to find out if
    it can move forwards, backwards, left or right.
    """
    state = {}

    def __init__(self):
        pass
