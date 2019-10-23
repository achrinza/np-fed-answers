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
