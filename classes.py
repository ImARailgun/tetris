from typing import List, Tuple

block_size = 50
screen_size = width, height = 800, 1150
# spawn = 300, 50
# spawn = 625, 400


class Block:
    location = [0, 0]
    color = 255, 255, 255

    def __init__(self, location: List[int], color: Tuple[int, int, int]) -> None:
        self.color = color
        self.location = location


class Piece:
    blocks = []
    active = False
    rot_index = 0
    block_type = 0

    def __init__(self, block_type, spawn=(625, 400)) -> None:
        self.blocks = []
        self.active = True
        self.block_type = block_type
        x_spawn, y_spawn = spawn
        self.rot_index = block_type["rot_index"]

        # block type needs -> color, x and y transforms for 3 of the 4 blocks

        # depends on block type
        color = block_type["color"]

        # depends on block type
        self.blocks.append(Block([x_spawn, y_spawn], color))
        self.blocks.append(Block(
            [x_spawn + block_type["instructions"]["Two"][0] * block_size, y_spawn + block_type["instructions"]["Two"][1] * block_size], color))
        self.blocks.append(Block([x_spawn + block_type["instructions"]["Three"][0] * block_size,
                           y_spawn + block_type["instructions"]["Three"][1] * block_size], color))
        self.blocks.append(Block([x_spawn + block_type["instructions"]["Four"][0] * block_size,
                           y_spawn + block_type["instructions"]["Four"][1] * block_size], color))

    def rotate(self, direction: str, inactive_blocks: List) -> None:
        if not self.active:
            return

        if self.rot_index > 3:
            return

        origin = {
            "x": self.blocks[self.rot_index].location[0],
            "y": self.blocks[self.rot_index].location[1]
        }

        moves = []

        for block in self.blocks:
            current_x = block.location[0] - origin["x"]
            current_y = block.location[1] - origin["y"]

            new_x, new_y = 0, 0

            if direction == "right":
                new_x = current_y + origin["x"]
                new_y = -current_x + origin["y"]
            else:
                new_x = -current_y + origin["x"]
                new_y = current_x + origin["y"]

            moves.append((new_x, new_y, block))

        if (self.check_for_move(moves, screen_size, inactive_blocks)):
            for x, y, block in moves:
                block.location = [x, y]

    def move_down(self, inactive_blocks) -> None:
        if not self.active:
            return

        moves = []

        for block in self.blocks:
            moves.append((block.location[0], block.location[1] + 50, block))

        if (self.check_for_move(moves, screen_size, inactive_blocks)):
            for x, y, block in moves:
                block.location = [x, y]
        else:
            self.active = False

    def move_horizontal(self, direction: str, inactive_blocks) -> None:

        if not self.active:
            return

        moves = []

        for block in self.blocks:
            if direction == "right":
                moves.append(
                    (block.location[0] + 50, block.location[1], block))
            else:
                moves.append(
                    (block.location[0] - 50, block.location[1], block))

        if (self.check_for_move(moves, screen_size, inactive_blocks)):
            for x, y, block in moves:
                block.location = [x, y]

    def check_for_move(self, moves: List[Tuple[int, int, dict]], size: Tuple[int, int], inactive_blocks=[]):
        for move in moves:
            if move[0] < 50 or move[0] > size[0]-251:
                return False
            if move[1] < 50 or move[1] > size[1]-150:
                return False

            for block in inactive_blocks:
                if move[0] == block.location[0] and move[1] == block.location[1]:
                    return False

        return True
