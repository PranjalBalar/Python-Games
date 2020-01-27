# -*- coding: utf-8 -*-

#This is a clssic pong game
#To Play: Player1 - use 'up' and 'down' arrows to control their sidebar; Player2 - use 'w' and 's' keys to move sidebar up and down respectively.
import simpleguitk
import random

WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

def spawn_ball(direction):
    global LEFT, RIGHT
    global ball_pos, ball_vel 
    ball_pos = [WIDTH/2, HEIGHT/2]
    vel_x = random.randrange(2, 4)
    vel_y = random.randrange(2, 4)
    if direction == LEFT:
        vel_x *= -1 
    ball_vel = [vel_x, vel_y]
     

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  
    global score1, score2  
        
    score1 = 0
    score2 = 0
    
    spawn_ball(1)
    
    paddle1_pos = 0
    paddle2_pos = 0
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if (ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS):
        ball_vel[1] *= -1
    if (ball_pos[0] <= PAD_WIDTH + BALL_RADIUS):
        if (ball_pos[1] >= paddle1_pos and ball_pos[1] <= paddle1_pos + 80):
            ball_vel[0] *= -1 
        else:
            spawn_ball(RIGHT)
            score2 += 1
    if (ball_pos[0] >= WIDTH - (PAD_WIDTH + BALL_RADIUS)):
        if (ball_pos[1] >= paddle2_pos and ball_pos[1] <= paddle2_pos + 80):
             ball_vel[0] *= -1
        else:
            spawn_ball(LEFT)
            score1 += 1
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    

    if (paddle1_pos >= HEIGHT - PAD_HEIGHT):
        paddle1_pos = HEIGHT - PAD_HEIGHT
    if (paddle2_pos >= HEIGHT - PAD_HEIGHT):
        paddle2_pos = HEIGHT - PAD_HEIGHT
    if ( paddle1_pos <= 0):
        paddle1_pos = 0
    if ( paddle2_pos <= 0):
        paddle2_pos = 0
    
    paddle1_pol = ([0, paddle1_pos], [0, paddle1_pos + 80], [8, paddle1_pos + 80], [8, paddle1_pos])
    paddle2_pol = ([WIDTH, paddle2_pos], [WIDTH, paddle2_pos + 80], [WIDTH - 8,paddle2_pos + 80], [WIDTH - 8, paddle2_pos])

    canvas.draw_polygon(paddle1_pol, 2, 'White', 'White')
    canvas.draw_polygon(paddle2_pol, 2, 'White', 'White')
    
    canvas.draw_text(str(score1), [150, 50], 50, 'yellow')
    canvas.draw_text(str(score2), [450, 50], 50, 'yellow')
        
def keydown(key):
    global paddle1_pos, paddle2_pos
    if key == simpleguitk.KEY_MAP["s"]:
        paddle1_pos += 30
    if key == simpleguitk.KEY_MAP["down"]:
        paddle2_pos += 30

def keyup(key):
    global paddle1_pos, paddle2_pos
    if key == simpleguitk.KEY_MAP["w"]:
        paddle1_pos -= 30
    if key == simpleguitk.KEY_MAP["up"]:
        paddle2_pos -= 30
    
frame = simpleguitk.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', new_game, 200)

new_game()
frame.start()
