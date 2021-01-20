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
def snake(snake_list, lead_x, lead_y):
    for XnY in snake_list:
        pygame.draw.rect(win, PURPLE, [
            XnY[0], XnY[1], block_size, block_size])
        pygame.draw.rect(win, RED, [
            lead_x, lead_y, block_size, block_size])


def main():
    exit_game = False
    over = False

    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0

    body = []
    snake_length = 1

    target_x = round(random.randrange(
        0, display_width - block_size)/block_size)*block_size
    target_y = round(random.randrange(
        0, display_height - block_size)/block_size)*block_size

    while not exit_game:
        # ゲーム終了後の処理
        while over:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        main()
                    if event.key == pygame.K_q:
                        exit_game = True
                        over = False
                elif event.type == pygame.QUIT:
                    exit_game = True
                    over = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            over = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        win.fill(WHITE)
        pygame.draw.rect(win, BLACK, [
                         target_x, target_y, block_size, block_size])

        head = [lead_x, lead_y]
        body.append(head)

        if len(body) > snake_length:
            del body[0]

        # 頭が身体と接触するとゲーム終了
        for eachSegment in body[:-1]:
            if eachSegment == head:
                over = True

        # 身体の色更新
        snake(body, lead_x, lead_y)

        #
        # if lead_x == target_x and lead_y == target_y:
        if head == [target_x, target_y]:
            target_x = round(random.randrange(
                0, display_width - block_size)/block_size)*block_size
            target_y = round(random.randrange(
                0, display_height - block_size)/block_size)*block_size
            snake_length += 1

        pygame.display.update()

        clock.tick(speed)
    # ゲーム終了
    pygame.quit()


if __name__ == '__main__':
    main()
