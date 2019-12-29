# -*- coding: utf-8 -*-

#This program creates a stopwatch game where when you stop the watch at any exact multiple of 5 seconds, you get a point.
import simpleguitk

# define global variables

t_elapse = 0
t_attempts = 0
suc_attp = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    d = t % 10
    x = t // 10
    a = x // 60
    y = x % 60
    b = y // 10
    c = y % 10
    return str(a) + ":" + str(b) + str(c) + "." + str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    timer.start()
    
def stop():
    timer.stop()
    global t_attempts
    global suc_attp
    if t_elapse % 50 == 0:
        suc_attp += 1
        t_attempts += 1
    else:    
        t_attempts += 1
    
def reset():
    global t_elapse
    global t_attempts
    global suc_attp
    t_elapse = 0
    t_attempts = 0
    suc_attp = 0

# define event handler for timer with 0.1 sec interval

def timer():
    global t_elapse
    t_elapse = t_elapse + 1
    
# define draw handler

def draw(canvas):
    global t_elapse
    text = format(t_elapse)
    canvas.draw_text(text, [200, 200], 50, 'White')
    canvas.draw_text(str(suc_attp), [50, 50], 30, 'Green')
    canvas.draw_text(' /', [60, 50], 30, 'Green')
    canvas.draw_text(str(t_attempts), [80, 50], 30, 'Green')
    
# create frame

frame = simpleguitk.create_frame("Stopwatch", 500, 500)

# register event handlers

timer = simpleguitk.create_timer(100, timer)
button1 = frame.add_button("Start", start, 100)
button2 = frame.add_button("Stop", stop, 100)
button3 = frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)

# start frame

frame.start()
