from __future__ import annotations

import typing

import pygame

from settings import (
    NUM_COLUMN,
    NUM_ROW,
    GRID,
    Position,
    GRID_COLOR,
    WHITE,
)

if typing.TYPE_CHECKING:
    from snake import Snake


def draw_background(screen: pygame.Surface):
    for i in range(NUM_COLUMN):
        for j in range(NUM_ROW):
            grid_rect = pygame.Rect((i * GRID, j * GRID), (GRID, GRID))
            color = GRID_COLOR[(j + i) % 2]
            pygame.draw.rect(screen, color, grid_rect)


def draw_object(
    screen: pygame.Surface, color: tuple[int, int, int], position: Position
):
    rect = pygame.Rect(position, (GRID, GRID))
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, WHITE, rect, 1)


def show_info(screen: pygame.Surface, snake: Snake, scores: list[int]):
    font = pygame.font.SysFont("malgungothic", 40)
    score = snake.length - 3
    text = font.render(f"점수: {score} 최고 점수: {max(scores)}", True, WHITE)
    screen.blit(text, (20, 20))
