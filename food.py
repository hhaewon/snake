from __future__ import annotations

import typing
import random

import pygame

from settings import RED, NUM_COLUMN, NUM_ROW, GRID
from utils import draw_object

if typing.TYPE_CHECKING:
    from snake import Snake


class Food:
    def __init__(self, snake: Snake):
        self.color = RED
        self.snake = snake
        self.randomize_position()

    def randomize_position(self):
        position = (
            random.randint(0, NUM_COLUMN - 1) * GRID,
            random.randint(0, NUM_ROW - 1) * GRID,
        )
        while position in self.snake.positions:
            position = (
                random.randint(0, NUM_COLUMN - 1) * GRID,
                random.randint(0, NUM_ROW - 1) * GRID,
            )
        self.position = position

    def draw(self, screen: pygame.Surface):
        draw_object(screen, self.color, self.position)
