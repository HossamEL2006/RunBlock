
# IMPORTATIONS :
import random
import pygame
from pygame.locals import *
from joueur import Joueur
from chrono import Chrono
from ball import *
import ball
import time
pygame.init()
# ----------------------------------------------------------------------------------------------------


# FONCTIONS :
# ----------------------------------------------------------------------------------------------------


# VARIABLES :


y_fond = 50


W, H = 500, 500 + y_fond
HW, HH = W/2, H/2
AREA = W * H

DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("RUN BLOCK")
DS_rect = DS.get_rect()

record = 0

tempDecreaseVelocity = 15

listeFenetres = ["mainmenu", "game", "gamover"]


CLOCK = pygame.time.Clock()


FPS = 30
RUNNING = True

fenetre = "mainmenu"


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# IMAGES
fond = pygame.image.load("assets/fond.png").convert()
gameOver = pygame.image.load("assets/gameover.png").convert_alpha()
SMALL_pixelated = pygame.font.Font("assets/pixelated.ttf", 15)
pixelated = pygame.font.Font("assets/pixelated.ttf", 30)
BIG_pixelated = pygame.font.Font("assets/pixelated.ttf", 60)

# MAINMENU
play_button = pygame.Rect(0, 150, 200, 70)
play_button.centerx = DS_rect.centerx
play_text = BIG_pixelated.render("PLAY", False, BLACK)
play_rect = play_text.get_rect()
play_rect.center = play_button.center

quit_button = pygame.Rect(140, 290, 200, 70)
quit_button.centerx = DS_rect.centerx
quit_text = BIG_pixelated.render("QUIT", False, BLACK)
quit_rect = play_text.get_rect()
quit_rect.center = quit_button.center

start = False


bouclesTermines = 0

rectPannel = pygame.Rect(0, 0, W, y_fond)


# ----------------------------------------------------------------------------------------------------


# MAIN LOOP
while RUNNING:

    # EVENEMENTS
    for event in pygame.event.get():
        if event.type == QUIT:
            RUNNING = False
        if event.type == USEREVENT:
            if fenetre == "game":
                num17 = random.randint(1, 2)
                if num17 == 1:
                    joueur1.decreaseVelocity()
                elif num17 == 2:
                    ball.decreaseVelocity()
        if event.type == KEYUP:
            if fenetre == "gameover":
                if event.key == K_SPACE:
                    fenetre = "game"
                    start = True

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if play_button.collidepoint(event.pos):
                    fenetre = "game"
                    start = True
                if quit_button.collidepoint(event.pos):
                    quit()

    # ----------------------------------------------------------------------------------------------------

    # LOGIQUE

    if fenetre == "game":

        if start == True:

            joueur1 = Joueur(W, H, HW, HH, y_fond)
            chrono = Chrono()
            listeBalls = []

            ball.velocity = 200

            listeBalls.append(Balld(W, H, HW, HH, y_fond, joueur1))
            listeBalls.append(Ballb(W, H, HW, HH, y_fond, joueur1))
            listeBalls.append(Ballg(W, H, HW, HH, y_fond, joueur1))
            listeBalls.append(Ballh(W, H, HW, HH, y_fond, joueur1))

            isPhaseFinish = False

            pygame.time.set_timer(USEREVENT, tempDecreaseVelocity * 1000)

            start = False

        chrono_actuel = chrono.getChrono()
        minutes = int(chrono_actuel//60)
        seconds = int(chrono_actuel) - (minutes * 60)
        centisecondes = int((chrono_actuel - int(chrono_actuel))*100)

        fps_actuel = CLOCK.get_fps()

        if not fps_actuel == 0:
            dt = 1/fps_actuel
            if fps_actuel <= 10:
                quit()
        else:
            dt = 0

        # print(fps_actuel)

        for i in listeBalls:
            i.gravite(dt)

        nombreDeBalls = len(listeBalls)
        for i in range(nombreDeBalls):
            # num10 nous permet de faire fonctionner la supression des balls hors screen
            num10 = nombreDeBalls - 1 - i
            j = listeBalls[num10]

            if j.verif() == True:
                isPhaseFinish = True
                listeBalls.pop(num10)
        if isPhaseFinish == True:
            listeBalls.append(Balld(W, H, HW, HH, y_fond, joueur1))
            listeBalls.append(Ballb(W, H, HW, HH, y_fond, joueur1))
            listeBalls.append(Ballg(W, H, HW, HH, y_fond, joueur1))
            listeBalls.append(Ballh(W, H, HW, HH, y_fond, joueur1))
            isPhaseFinish = False

        keys = pygame.key.get_pressed()

        if keys[K_d] or keys[K_RIGHT]:
            joueur1.right(dt)
        if keys[K_q] or keys[K_LEFT]:
            joueur1.left(dt)
        if keys[K_s] or keys[K_DOWN]:
            joueur1.low(dt)
        if keys[K_z] or keys[K_UP]:
            joueur1.high(dt)
        # if keys[K_h]:
        #     joueur1.health = 1000
        # if keys[K_j]:
        #     joueur1.velocity += 100
        joueur1.verif()

        for i in listeBalls:
            if i.collide():
                joueur1.health -= random.randint(1, 20)
        if joueur1.health <= 0:
            joueur1.health = 0

        pourcentageHealth = joueur1.health // 10

    # ----------------------------------------------------------------------------------------------------

    # AFFICHAGE

    if fenetre == "game":
        DS.fill(BLACK)
        DS.blit(fond, (0, y_fond))

        DS.blit(joueur1.image, joueur1.rect)
        for i in listeBalls:
            DS.blit(i.image, i.rect)

        pygame.draw.rect(DS, BLACK, rectPannel, 0)

        chrono_text = pixelated.render(
            f"Chrono : {minutes} : {seconds} : {centisecondes}", False, WHITE)
        fps_text = SMALL_pixelated.render(f"FPS : {round(fps_actuel, 1)}", False, BLACK)
        fps_rect = fps_text.get_rect()
        fps_rect.bottomright = DS_rect.bottomright
        vitesse_text = pixelated.render(f"Vitesse : {joueur1.velocity}", False, WHITE)
        # record_text = pixelated.render(f"Record : {record}", False, WHITE)
        # health_text = pixelated.render(f"Vie : {pourcentageHealth} %", False, WHITE)

        DS.blit(chrono_text, (10, 0))
        # DS.blit(health_text, (10, 50))
        DS.blit(fps_text, fps_rect)
        DS.blit(vitesse_text, (W/2, 0))
        # DS.blit(record_text, (W/2, 50))

    if fenetre == "gameover":
        DS.blit(gameOver, (0, y_fond))
        retry_text = pixelated.render(f"  press SPACE to retry  ", False, BLACK)
        retry_rect = retry_text.get_rect()
        retry_rect.midtop = DS_rect.midtop
        retry_rect.y = 350 + y_fond
        retry_rect.h += 5
        pygame.draw.rect(DS, WHITE, retry_rect, 0)
        DS.blit(retry_text, retry_rect)

    if fenetre == "mainmenu":
        pygame.draw.rect(DS, WHITE, play_button, 0)
        DS.blit(play_text, play_rect)
        pygame.draw.rect(DS, WHITE, quit_button, 0)
        DS.blit(quit_text, quit_rect)

    pygame.display.flip()
    # ----------------------------------------------------------------------------------------------------

    # FIX
    CLOCK.tick(FPS)
    if fenetre == "game":
        if pourcentageHealth <= 0:
            fenetre = "gameover"
    bouclesTermines += 1
    # ----------------------------------------------------------------------------------------------------


# QUIT
pygame.quit()
quit()
# ----------------------------------------------------------------------------------------------------
