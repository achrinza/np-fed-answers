import json
import os

from di_container import DIContainerKeys, inject
from maze import Maze

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
