#Basic game to understand pygame

import pygame, sys, random

#General Setup
pygame.init()
clock = pygame.time.Clock()

def ball_animation():
    global ball_speed_x,ball_speed_y,player_score,opponent_score
    ball.x+= ball_speed_x
    ball.y+= ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y*= -1
    if ball.right >= screen_width:
        opponent_score+=1
        pygame.mixer.Sound.play(score_sound)
        ball_reset()
    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        player_score+=1
        ball_reset()

    if ball.colliderect(player) and ball_speed_x > 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.right - player.left) <= 10:    
            ball_speed_x *= -1
        if abs(ball.bottom - player.top) <= 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player.bottom) <= 10 and ball_speed_y < 0:
            ball_speed_y *= -1

    if ball.colliderect(opponent) and ball_speed_x < 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.left - opponent.right) <= 10:    
            ball_speed_x *= -1
        if abs(ball.bottom - opponent.top) <= 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - opponent.bottom) <= 10 and ball_speed_y < 0:
            ball_speed_y *= -1

def player_animation():
    global player_speed
    player.y += player_speed
    if player.top < 0:
        player.top = 0
    if player.bottom > screen_height:
        player.bottom = screen_height

def opponent_animation():
    global opponent_speed
    if opponent.top <= ball.y:
        opponent.y += opponent_speed
    if opponent.bottom >= ball.y:
        opponent.y -= opponent_speed
    if opponent.top <= 10:
        opponent.top = 10
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_reset():
    global ball_speed_y,ball_speed_x,reset
    ball.center = (screen_width/2,screen_height/2)
    ball_speed_x *= random.choice((1,-1))
    ball_speed_y *= random.choice((1,-1))
    reset = True
#Setting up the screen
screen_height = 760
screen_width = 1080
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong")

#Game Rectangles
ball = pygame.Rect(screen_width//2 - 15,screen_height//2 - 15,30,30)
player = pygame.Rect(screen_width - 20, screen_height//2 - 70,10,140)
opponent = pygame.Rect(10, screen_height//2 - 70,10,140)

bg_color = pygame.Color("grey12")
light_grey = (200,200,200)

#Speeds
ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7

#Score
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf",32)

#Sound
pong_sound = pygame.mixer.Sound("pong.ogg")
score_sound = pygame.mixer.Sound("score.ogg")
#Timer
reset = False
while True:
    #Input checking

    # if reset:
    #     for countdown in range(3,0,-1):
    #         print(countdown)
    #         start = game_font.render(f'{countdown}',False,light_grey)
    #         screen.blit(start,(300,300))
    #         pygame.time.wait(1000)
    #         pygame.display.flip()
    #         clock.tick(60) #frames per second
    #     reset = False
    for event in pygame.event.get():  #all user input in pygame are events
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    #Determining new coordinates
    ball_animation()
    player_animation()
    opponent_animation()
    #Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen,light_grey,(screen_width//2,0),(screen_width//2,screen_height))

    #Text
    player_text = game_font.render(f'{player_score}',False,light_grey)
    screen.blit(player_text,(563,470))

    opponent_text = game_font.render(f'{opponent_score}',False,light_grey)
    screen.blit(opponent_text,(503,470))
    #Updating the Window
    pygame.display.flip()
    clock.tick(60) #frames per second