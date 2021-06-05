'''
PONG - Pretty Obsolete No-good Game

Really bad recreation of Pong in pygame. It supports 2 players (on one machine)
and has pretty much only the base game and sound with a basic score counter. I don't know Python,
GUI Programming, let alone game programming, this is supposed to be a crude learning project.

I have yet to learn collision detection and how to implement newtonian physics in games. Both
the collision detection and the physics are from really bad to non-existent.

'''

import pygame
import time
pygame.init()
pygame.mixer.get_init()

#standard/global declarations
window_w = 800
window_h = 600

white = (255, 255, 255)
black = (0, 0, 0)

FPS = 320

window = pygame.display.set_mode((window_w, window_h))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

hit_sound = pygame.mixer.Sound('./hit.wav')
wall_sound = pygame.mixer.Sound('./wall.wav')
score_sound = pygame.mixer.Sound('./score.wav')

blockAlive = True

rect_xpos = window_h/8
rect_ypos = window_w/2

rect = pygame.rect.Rect(rect_xpos, rect_ypos, 20, 80)

rect2 = pygame.rect.Rect(window_w/1.15, window_h/2, 20, 80)

font = pygame.font.SysFont(None, 25)

def show_text(msg, color, x, y):
    text = font.render(msg, True, color)
    window.blit(text, (x, y))

def pause():
    while True:
        if keyboard.read_key() == 'space':
            break

'''
handle_keys()

handles the keypresses/controls of the game, setting the paddles' properties.
'''
def handle_keys():
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        rect.top -= 2
    if key[pygame.K_DOWN]:
        rect.bottom += 2

    if key[pygame.K_a]:
        rect2.top -= 2
    if key[pygame.K_z]:
        rect2.bottom += 2

counter = [0, 0]

def restart_game():
    game_loop()

def game_loop():

    #variable declarations
    COLOR = 'white'
    COLORCOLLIDE = 'green'

    pos_x = window_w/2
    pos_y = window_h/2

    block_size = 20

    velocity = [1, 1]

    running = True

    while running:

        #main game loop
        ball = pygame.rect.Rect(pos_x, pos_y, 10, 10)
        collide = ball.colliderect(rect)
        collide2 = ball.colliderect(rect2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pos_x += velocity[0]
        pos_y += velocity[1]

        #score counter
        if pos_x + block_size > window_w:
            counter[1] += 1
            score_sound.play()
            restart_game()

        if pos_x < 0:
            counter[0] += 1
            score_sound.play()
            restart_game()

        #collision checking
        if pos_y + block_size > window_h or pos_y < 0:
            wall_sound.play()
            velocity[1] = -velocity[1]

        if collide and pos_x == rect.left:
            hit_sound.play()
            velocity[0] = -velocity[0]

        if collide2 and pos_x == rect2.left:
            hit_sound.play()
            velocity[0] = -velocity[0]
        
        if counter[0] >= 11:
            break
        
        if counter[1] >= 11:
            break

        # DRAW
        window.fill(black)
        pygame.draw.rect(window, white, rect)
        pygame.draw.rect(window, white, rect2)
        pygame.draw.rect(window, COLOR, ball)
        show_text(str(counter[0]), white, window_w/1.3, window_h/1.2)
        show_text(str(counter[1]), white, window_w/5, window_h/1.2)
        handle_keys()
        pygame.display.update()
        #clock.tick(FPS)

game_loop()