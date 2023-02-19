import pygame

from food import Food
from snake import Snake
from utils import draw_background, show_info
from settings import WINDOW_WIDTH, WINDOW_HEIGHT, WHITE


def play(screen: pygame.Surface, clock: pygame.time.Clock, scores: list[int]):
    snake = Snake()
    is_running = 1

    food_group = [Food(snake=snake) for _ in range(3)]
    scores.append(0)

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = 0
            if event.type == pygame.KEYDOWN:
                if event.key in snake.matched_direction:
                    snake.change_direction(event.key)

        clock.tick(9)
        draw_background(screen=screen)

        snake.move(screen=screen)
        is_running = not snake.is_collide()
        snake.check_position(foods=food_group)
        snake.draw(screen=screen)

        for food in food_group:
            food.draw(screen=screen)

        show_info(screen=screen, snake=snake, scores=scores)
        scores[-1] = snake.length - 3
        pygame.display.flip()


def gameover(screen: pygame.Surface):
    is_running = 1

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True

        font = pygame.font.SysFont("Algerian", 50)
        text = font.render("GAME OVER", True, WHITE)
        position = text.get_rect()
        position.center = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2
        screen.blit(text, position)

        font = pygame.font.SysFont("malgungothic", 25)
        text = font.render("Press space bar to play again", True, WHITE)
        position = text.get_rect()
        position.center = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50
        screen.blit(text, position)

        pygame.display.flip()
    return False


def main():
    pygame.init()
    pygame.display.set_caption("SNAKE GAME")
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    scores: list[int] = []
    play(screen=screen, clock=clock, scores=scores)
    play_again = gameover(screen=screen)
    while play_again:
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        play(screen=screen, clock=clock, scores=scores)
        play_again = gameover(screen=screen)


if __name__ == "__main__":
    main()
