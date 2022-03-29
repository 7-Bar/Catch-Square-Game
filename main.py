import pygame
import random
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Catch square game")
icon = pygame.image.load("square logo (2).png")
mixer.music.load("mixkit-game-level-music-689 (1).wav")
mixer.music.play(-1)
pygame.display.set_icon(icon)

player = pygame.image.load("square smaller.png")
yellow = pygame.image.load("square yellow.jpg")
score_sound = mixer.Sound("B5XWP5Y-total-score-(new).wav")
move_sound = mixer.Sound("mixkit-player-jumping-in-a-video-game-2043 (1).wav")

running = True
start = True
yellow_places_X = ["50", "100", "150", "200", "250", "300", "350", "400"]
yellow_places_Y = ["50", "100", "150", "200", "250", "300"]
player_X = 0
player_Y = 0
yellow_X = 0
yellow_Y = 0
move = 50
score = 0

font = pygame.font.Font("freesansbold.ttf", 32)


def show_score(x, y):
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (x, y))


def player_move(x, y):
    screen.blit(player, (x, y))


def yellow_move(x, y):
    screen.blit(yellow, (x, y))


print("Catch Square Game")
print("Created by Bar on 2022/3/28")

while running:

    screen.fill((0, 180, 200))

    if start:
        yellow_X = int(yellow_places_X[random.randint(0, 7)])
        yellow_Y = int(yellow_places_Y[random.randint(0, 5)])
        yellow_move(yellow_X, yellow_Y)
        start = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_Y -= move
                move_sound.play()
            if event.key == pygame.K_s:
                player_Y += move
                move_sound.play()
            if event.key == pygame.K_a:
                player_X -= move
                move_sound.play()
            if event.key == pygame.K_d:
                player_X += move
                move_sound.play()
            if event.key == pygame.K_UP:
                player_Y -= move
                move_sound.play()
            if event.key == pygame.K_DOWN:
                player_Y += move
                move_sound.play()
            if event.key == pygame.K_LEFT:
                player_X -= move
                move_sound.play()
            if event.key == pygame.K_RIGHT:
                player_X += move
                move_sound.play()

        if player_X <= 50:
            player_X = 50
        elif player_X >= 400:
            player_X = 400

        if player_Y >= 300:
            player_Y = 300
        elif player_Y <= 50:
            player_Y = 50

        if player_X == yellow_X and player_Y == yellow_Y:
            yellow_X = int(yellow_places_X[random.randint(0, 7)])
            yellow_Y = int(yellow_places_Y[random.randint(0, 5)])
            yellow_move(yellow_X, yellow_Y)
            score_sound.play()
            score += 1

    yellow_move(yellow_X, yellow_Y)
    player_move(player_X, player_Y)
    show_score(10, 10)
    pygame.display.update()
