import pygame


def render_game(screen, screen_fill, active_piece, block_size, inactive_blocks, score, next_piece, saved_piece):
    screen.fill(screen_fill)

    board = pygame.Surface((500, 1000))
    board.fill((0, 0, 0))
    board_rect = board.get_rect()
    board_rect.center = (300, 550)

    screen.blit(board, board_rect)

    block_border = pygame.Surface((block_size, block_size))
    block_border.fill((200, 200, 220))

    for block in active_piece.blocks:
        block_surface = pygame.Surface((block_size-2, block_size-2))
        block_surface.fill(block.color)
        block_rect = pygame.Rect(
            block.location[0]+1, block.location[1]+1, block_size-2, block_size-2)
        border_rect = pygame.Rect(
            block.location[0], block.location[1], block_size, block_size)

        screen.blit(block_border, border_rect)
        screen.blit(block_surface, block_rect)

    for block in inactive_blocks:
        block_surface = pygame.Surface((block_size-2, block_size-2))
        block_surface.fill(block.color)
        block_rect = pygame.Rect(
            block.location[0]+1, block.location[1]+1, block_size-2, block_size-2)
        border_rect = pygame.Rect(
            block.location[0], block.location[1], block_size, block_size)

        screen.blit(block_border, border_rect)
        screen.blit(block_surface, block_rect)

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Score:',
                       True, (0, 0, 0), (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (675, 200)
    screen.blit(text, textRect)

    text2 = font.render(f'{score}',
                        True, (0, 0, 0), (255, 255, 255))
    textRect2 = text2.get_rect()
    textRect2.center = (675, 250)
    screen.blit(text2, textRect2)

    for block in next_piece.blocks:
        block_surface = pygame.Surface((block_size-2, block_size-2))
        block_surface.fill(block.color)
        block_rect = pygame.Rect(
            block.location[0]+1, block.location[1]+1, block_size-2, block_size-2)
        border_rect = pygame.Rect(
            block.location[0], block.location[1], block_size, block_size)

        screen.blit(block_border, border_rect)
        screen.blit(block_surface, block_rect)

    next_label = font.render('Next Piece:',
                             True, (0, 0, 0), (255, 255, 255))
    next_label_rect = next_label.get_rect()
    next_label_rect.center = (675, 350)
    screen.blit(next_label, next_label_rect)

    if saved_piece != 0:
        for block in saved_piece.blocks:
            block_surface = pygame.Surface((block_size-2, block_size-2))
            block_surface.fill(block.color)
            block_rect = pygame.Rect(
                block.location[0]+1, block.location[1]+1, block_size-2, block_size-2)
            border_rect = pygame.Rect(
                block.location[0], block.location[1], block_size, block_size)

            screen.blit(block_border, border_rect)
            screen.blit(block_surface, block_rect)

    saved_label = font.render('Saved Piece (C)',
                              True, (0, 0, 0), (255, 255, 255))
    saved_label_rect = saved_label.get_rect()
    saved_label_rect.center = (675, 700)
    screen.blit(saved_label, saved_label_rect)

    rot_label = font.render('Rotate (Z, X)',
                            True, (0, 0, 0), (255, 255, 255))
    rot_label_rect = rot_label.get_rect()
    rot_label_rect.center = (675, 1000)
    screen.blit(rot_label, rot_label_rect)
