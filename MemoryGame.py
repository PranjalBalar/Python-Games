# -*- coding: utf-8 -*-

#This is a simple Memory Game
#To play: Click on any cards and try to match the hidden value of the cards

import simpleguitk
import random

def new_game():
    global card_lst, exposed, state, turn
    global x1 
    x1 = -1
    lst = range(8)
    card_lst = lst + lst
    random.shuffle(card_lst)
    exposed = [False] * 16
    state = 0 
    turn = 0
    
def mouseclick(pos):
    global x1, exposed, state, card1, card2, card_lst, turn
    selected_card = pos[0] / 50
    exposed[selected_card] = True
    if state == 0:
        card1 = selected_card
        state = 1 
    elif state == 1:
        card2 = selected_card
        turn += 1
        state = 2
    elif state == 2: 
        if card_lst[card1] != card_lst[card2]:
            exposed[card1] = False
            exposed[card2] = False
        state = 1
        card1 = selected_card
    label.set_text('Turns = ' + str(turn))
    
def draw(canvas):
    global x1, exposed
    x  = 0   
    for i in range(len(card_lst)):
        if exposed[i] == True: 
             canvas.draw_text(str (card_lst[i]), [x + 15, 50], 40, 'Red')    
        else:
            canvas.draw_polygon([[x, 0], [x + 45, 0], [x + 45, 100], [x, 100]], 5, 'Green', 'White')    
        x += 50
        
frame = simpleguitk.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

new_game()
frame.start()