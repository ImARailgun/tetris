import sys
import pygame
from classes import Block, Piece, block_size, screen_size
from block_types import block_types
import random
import time
from functions import render_game

pygame.init()
pygame.display.set_caption('Tetris')

clock = pygame.time.Clock()

screen_fill = 255, 255, 255

screen = pygame.display.set_mode(screen_size)

active_piece = Piece(random.choice(list(block_types.values())))
for block in active_piece.blocks:
    block.location[0] -= 375
    block.location[1] -= 350

inactive_blocks = []

fall_speed = 1000
timer = 0
score = 0

last_held = time.time()

game_not_over = True

next_piece = Piece(random.choice(list(block_types.values())))

saved_piece = 0

while True:
    if game_not_over:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print(event)
                if event.key == 122:
                    active_piece.rotate("left", inactive_blocks)
                if event.key == 120:
                    active_piece.rotate("right", inactive_blocks)
                if event.key == 1073741905:
                    active_piece.move_down(inactive_blocks)
                    last_held = time.time()
                    timer = 0
                if event.key == 1073741903:
                    active_piece.move_horizontal("right", inactive_blocks)
                    last_held = time.time()
                if event.key == 1073741904:
                    active_piece.move_horizontal("left", inactive_blocks)
                    last_held = time.time()
                if event.key == 99 and active_piece.active:
                    if saved_piece != 0:
                        old_active = active_piece
                        active_piece = Piece(saved_piece.block_type, (300, 50))

                        saved_piece = Piece(old_active.block_type, (625, 725))
                    else:
                        saved_piece = Piece(
                            active_piece.block_type, (625, 725))

                        for block in next_piece.blocks:
                            block.location[0] -= 325
                            block.location[1] -= 350

                        active_piece = next_piece

                        next_piece = Piece(random.choice(
                            list(block_types.values())))

        timer = timer + clock.tick_busy_loop()

        if timer > fall_speed:
            active_piece.move_down(inactive_blocks)
            timer = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            if time.time() - last_held > .1:
                active_piece.move_down(inactive_blocks)
                last_held = time.time()
                timer = 0
        if keys[pygame.K_RIGHT]:
            if time.time() - last_held > .1:
                active_piece.move_horizontal("right", inactive_blocks)
                last_held = time.time()
        if keys[pygame.K_LEFT]:
            if time.time() - last_held > .1:
                active_piece.move_horizontal("left", inactive_blocks)
                last_held = time.time()

        render_game(screen, screen_fill, active_piece,
                    block_size, inactive_blocks, score, next_piece, saved_piece)

        if not active_piece.active:
            for block in active_piece.blocks:
                inactive_blocks.append(block)

            time.sleep(.3)

            tetris_check = {}
            for block in inactive_blocks:
                if str(block.location[1]) in tetris_check:
                    tetris_check[str(block.location[1])] += 1
                else:
                    tetris_check[str(block.location[1])] = 1

            rows_to_remove = []

            for y, number in tetris_check.items():
                if number == 10:
                    rows_to_remove.append(int(y))

            remove_blocks = []
            for block in inactive_blocks:
                if block.location[1] in rows_to_remove:
                    remove_blocks.append(block)

                if len(rows_to_remove) > 0:
                    if block.location[1] < rows_to_remove[0]:
                        block.location[1] = block.location[1] + \
                            block_size * len(rows_to_remove)

            for block in remove_blocks:
                inactive_blocks.remove(block)

            if len(remove_blocks) > 1:
                score += 1000 * (len(rows_to_remove) ** len(rows_to_remove))
                render_game(screen, screen_fill, active_piece,
                            block_size, inactive_blocks, score, next_piece, saved_piece)
                time.sleep(.2)

            for block in active_piece.blocks:
                if block.location[1] == 50:
                    game_not_over = False

            for block in next_piece.blocks:
                block.location[0] -= 325
                block.location[1] -= 350

            active_piece = next_piece

            next_piece = Piece(random.choice(list(block_types.values())))

            timer = 0
    else:
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render('GAME OVER',
                           True, (0, 0, 0), (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (300, 400)
        screen.blit(text, textRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    pygame.display.flip()
