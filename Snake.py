import pygame
from random import randrange

try:
    pygame.init()
except:
    print("Erro! o modulo pygame nao foi iniciado com sucesso.")

#CONSTANTES COM TAMANHO DA TELA
WIDTH = 640
HEIGHT = 480
#CLOCK É UMA CLASSE QUE AUXILIA PARA O MOTOR, COMO LIMITAR OS FRAMES
CLOCK = pygame.time.Clock()
r = randrange(0, 200, 1)
g = randrange(0, 200, 1)
b = randrange(0, 255, 1)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
tam = 10
cobra_comp = 1
#JANELA, RECEBE TUPLA PARAM
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#TITULO DA JANELA, PODE RECEBER SEGUNDO PARAM QUE É O ICONE
pygame.display.set_caption("Snake")
font = pygame.font.SysFont(None, 25)
tittle = pygame.font.SysFont(None, 80)
init = True
over = False
sair = True
pos_y = 0
pos_x = 0

def apple(pos_x, pos_y):
    
    pygame.draw.rect(WIN, RED, [pos_x, pos_y, tam,tam])

def snake(cobraXY):
    for XY in cobraXY:
        #FUNCAO PARA DESENNHAR UM RETANGULO NA TELA
        pygame.draw.rect(WIN, GREEN, [XY[0], XY[1], tam,tam])

def text(font, msg, color, pos):
    texto = font.render(msg, True, color)
    WIN.blit(texto, pos)
    
def game():
    global r, g, b, cobra_comp, over, sair, pos_x, pos_y
    pos_x = randrange(0 , WIDTH -10, 10)
    pos_y = randrange(0 , HEIGHT -10, 10)
    maca_x = randrange(0 , WIDTH -10, 10)
    maca_y = randrange(0 , HEIGHT -10, 10)
    vel_x = 0
    vel_y = 0
    vel = 10
    cobraXY = []
    amount_ticks = 13
    
    #LOOP DO GAME
    while sair:
        
        WIN.fill((r,g,b))

        while over:
            WIN.fill(BLACK)
            text(tittle, "GAME OVER", RED, [WIDTH - 495, HEIGHT /4])        
            text(font, "high score:", GREEN, [WIDTH -380, HEIGHT /2])
            text(font, str(cobra_comp), GREEN, [WIDTH -285, HEIGHT /2])
            text(font, "press enter to continue or esc to exit", RED, [WIDTH -468, HEIGHT /1.1])
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    if events.key == pygame.K_RETURN:
                        cobra_comp = 1
                        pos_x = randrange(0 , WIDTH -10, 10)
                        pos_y = randrange(0 , HEIGHT -10, 10)
                        maca_x = randrange(0 , WIDTH -10, 10)
                        maca_y = randrange(0 , HEIGHT -10, 10)
                        vel_x = 0
                        vel_y = 0
                        vel = 10
                        cobraXY = []
                        amount_ticks = 13                        
                        over = False
                                
                                                        
                        
                pygame.display.update()
                CLOCK.tick(15)
        
            
    #foreach para capturar os eventos do game
        for events in pygame.event.get():
            print(events)
            
    #se o tipo do evento for quit, sai do loop e encerra a janela
            if events.type == pygame.QUIT:
                sair = False

    #verifica o tipo do evento e depois o o key pressionado
            elif events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    sair = False
                
                if events.key == pygame.K_LEFT and vel_x != tam or events.key == pygame.K_a and vel_x != tam:
                    vel_y = 0
                    vel_x = -vel
                if events.key == pygame.K_RIGHT and vel_x != -tam or events.key == pygame.K_d and vel_x != -tam:
                    vel_y = 0
                    vel_x = vel
                if events.key == pygame.K_UP and vel_y != tam or events.key == pygame.K_w and vel_y != tam:
                    vel_x = 0
                    vel_y = -vel
                if events.key == pygame.K_DOWN and vel_y != -tam or events.key == pygame.K_s and vel_y != -tam:
                    vel_x = 0
                    vel_y = vel

        #REGRAS PARA GAME OVER
        if pos_x > WIDTH or pos_x < 0 or pos_y > HEIGHT or pos_y < 0:
            over = True
        if any(bloco == cobra_ini for bloco in cobraXY[:-1]):
            over = True
            print("colidiu")
            
        
        pos_x += vel_x
        pos_y += vel_y

        cobra_ini = []
        cobra_ini.append(pos_x)
        cobra_ini.append(pos_y)
        cobraXY.append(cobra_ini)
        
        if len(cobraXY) > cobra_comp:
            del cobraXY[0]
        

        snake(cobraXY)
        if pos_x == maca_x and pos_y == maca_y:
            maca_x = randrange(0 , WIDTH -10, 10)
            maca_y = randrange(0 , HEIGHT -10, 10)
            cobra_comp += 1
            r = randrange(0, 200, 1)
            g = randrange(0, 200, 1)
            b = randrange(0, 255, 1)
            if amount_ticks <= 60:
                amount_ticks += 1
            else:
                amount_ticks = 30
            
        apple(maca_x, maca_y)
        text(font, "points :", WHITE, [0, 0])
        text(font, str(cobra_comp), WHITE, [70, 1])
    #FUNCAO QUE ATUALICA A TELA A CADA FRAME, SE PASSADO UM OBJ COMO PARAM
    #ATUALIZA APENAS ELE
        pygame.display.update()
    #FUNÇÃO QUE LIMITA OS FRAMES
        CLOCK.tick(amount_ticks)

while (init):
    text(tittle, "SNAKE", (r,g,b), [WIDTH - 435, HEIGHT /4])        
    text(font, "PRESS ENTER", RED, [WIDTH -385, HEIGHT /1.2])
    text(font, "Made by: Natan Marçal, github:NatanRib", WHITE, [WIDTH -485, HEIGHT -20])
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if events.key == pygame.K_RETURN:
                init = False
    if r < 200:
        r += 5
    else:
        r = randrange(0, 200, 1)
    if g < 200:
        g += 5
    else:
        g = randrange(0, 200, 1)
    if b < 240:
        b += 5
    else:
        b = randrange(0, 255, 1)
    pygame.display.update()
    CLOCK.tick(15)
    
game()
pygame.quit()
quit()


