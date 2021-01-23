import pygame
import random

pygame.init()

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)

# 画面サイズ
display_width = 800
display_height = 600
win = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Slithery Snake")

# ゲームスピード
clock = pygame.time.Clock()
speed = 5

# 正方形のサイズ
block_size = 50


# 色を付ける　頭は赤　身体は紫
def snake(body, head):
    for XnY in body:
        pygame.draw.rect(win, PURPLE, [
            XnY[0], XnY[1], block_size, block_size])
        pygame.draw.rect(win, RED, [
            head[0], head[1], block_size, block_size])


def generate_block():
    x = round(random.randrange(
        0, display_width - block_size)/block_size)*block_size
    y = round(random.randrange(
        0, display_height - block_size)/block_size)*block_size
    return [x, y]


def main():
    exit_game = False
    game_over = False
    pause = False

    head_x = display_width/2
    head_y = display_height/2
    x_update = 0
    y_update = 0

    body = []
    snake_length = 1
    target = generate_block()

    while not exit_game:
        # ゲーム終了後の処理
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        main()
                    if event.key == pygame.K_q:
                        exit_game = True
                        game_over = False
                elif event.type == pygame.QUIT:
                    exit_game = True
                    game_over = False

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause = False
                    if event.key == pygame.K_q:
                        exit_game = True
                        game_over = False
                elif event.type == pygame.QUIT:
                    exit_game = True
                    game_over = False
                    pause = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_update = -block_size
                    y_update = 0
                elif event.key == pygame.K_RIGHT:
                    x_update = block_size
                    y_update = 0
                elif event.key == pygame.K_DOWN:
                    y_update = block_size
                    x_update = 0
                elif event.key == pygame.K_UP:
                    y_update = -block_size
                    x_update = 0
                elif event.key == pygame.K_SPACE:
                    pause = True

        # 頭が壁と接触するとゲーム終了
        if head_x >= display_width or head_x < 0 or head_y >= display_height or head_y < 0:
            game_over = True

        head_x += x_update
        head_y += y_update

        head = [head_x, head_y]
        body.append(head)
        if len(body) > snake_length:
            del body[0]

        win.fill(WHITE)
        pygame.draw.rect(win, BLACK, [
            target[0], target[1], block_size, block_size])

        # 頭が身体と接触するとゲーム終了
        for block in body[:-1]:
            if block == head:
                game_over = True

        # 身体の色更新
        snake(body, head)

        # 長くなる　同時　新しいブロックを生成
        if head == target:
            snake_length += 1
            target = generate_block()

        # ゲームを進む
        pygame.display.update()
        clock.tick(speed)
    # ゲーム終了
    pygame.quit()


if __name__ == '__main__':
    main()
