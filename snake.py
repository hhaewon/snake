from __future__ import annotations

import random
import typing

import pygame

from settings import (
    BLUE2,
    BLUE3,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    Position,
    GRID,
    NUM_COLUMN,
    NUM_ROW,
    NORTH,
    SOUTH,
    WEST,
    EAST,
)
from utils import draw_object

if typing.TYPE_CHECKING:
    from food import Food


class Snake:
    def __init__(self):
        self.length = 3
        self.colors = (BLUE2, BLUE3)
        self.positions: list[Position] = [
            (GRID * (NUM_COLUMN // 2), GRID * (NUM_ROW // 2))
        ]
        self.matched_direction: dict[int, tuple[int, int]] = {
            pygame.K_UP: NORTH,
            pygame.K_DOWN: SOUTH,
            pygame.K_LEFT: WEST,
            pygame.K_RIGHT: EAST,
        }
        self.direction = random.choice([NORTH, EAST, WEST, SOUTH])

    @property
    def head_position(self):
        return self.positions[0]

    def move(self, screen: pygame.Surface):
        head = self.head_position
        x, y = self.direction

        next_position = ((head[0] + (x * GRID)), (head[1] + (y * GRID)))

        self.positions.insert(0, next_position)
        if len(self.positions) > self.length:
            self.positions.pop(-1)

    def draw(self, screen: pygame.Surface):
        for index, position in enumerate(self.positions):
            draw_object(screen=screen, color=self.colors[index % 2], position=position)

    def change_direction(self, key: int):
        arrowkey: tuple[int, int] = self.matched_direction[key]
        if (-arrowkey[0], -arrowkey[1]) == self.direction:
            return
        else:
            self.direction = arrowkey

    def check_position(self, foods: list[Food]):
        for food in foods:
            if self.head_position == food.position:
                self.length += 1
                food.randomize_position()

    def is_collide(self):
        is_duplicate_position = len(self.positions) != len(set(self.positions))
        x, y = self.head_position
        is_over_window = x >= WINDOW_WIDTH or x < 0 or y >= WINDOW_HEIGHT or y < 0
        return is_duplicate_position or is_over_window
