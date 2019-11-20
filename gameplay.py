import pygame
import random
import support
import enemy_2
pygame.init()


def make_screen_game(screen):
    x_nave = 30
    y_nave = 200
    ovni_sprite = pygame.image.load("content/nave_teste.png")
    background = "nebula.jpg"
    pygame.display.set_caption("Gameplay")
    bg = pygame.image.load("content/{}".format(background))

    ovnis = []
    spawn_chance = 0.04  # Chance de spawnar um ET

    shoot = []

    game = True

    while game:
        screen.blit(bg, (0, 0))
        support.draw_nave(screen, x_nave, y_nave)

        if(random.random() < spawn_chance):
            ovnis.append(enemy_2.make_ovni(3))
        enemy_2.update_ovni(screen, ovni_sprite, ovnis)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_nave -= 15
                if event.key == pygame.K_DOWN:
                    y_nave += 15
                if event.key == pygame.K_LEFT:
                    x_nave -= 15
                if event.key == pygame.K_RIGHT:
                    x_nave += 15
                if event.key == pygame.K_SPACE:
                    shoot.append(support.make_shot(3, x_nave, y_nave))

        support.update_shot(screen, shoot)
        pygame.display.flip()
        pygame.display.update()
