import copy
import csv
import os
import time

from di_container import inject

from character import CharacterDirectionals

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
        if width < 2 or height < 2:
            return ValueError("Invalid size; Maze dimensions too small")

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
            self.character_god_teleport(x, y)
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