# -*- coding: utf-8 -*-

from tkinter import*
import time

# TODO: Support another match_time ex. python3 main.py -s=60
def reset(event=None):
	global match_time
	for i in range(6):
		variables[i].set(0)

	seconds.set(match_time)
	minute.set(int(match_time/60))
	if match_time%60 < 10:
		seconds.set("0"+str(match_time%60))
	else:
		second.set(str(match_time%60))

	stop_flag = False

def count_time():
	global stop_flag

	global seconds
	global minute
	global second
	global root

	if not stop_flag and seconds.get() != 0:
		# if seconds == 15:
		# TODO: buzu

		seconds.set(seconds.get()-1)
		minute.set(int((seconds.get())/60))
		if seconds.get()%60 < 10:
			second.set("0"+str(seconds.get()%60))
		else:
			second.set(str(seconds.get()%60))
		root.after(1000, count_time)
	
	# if seconds == 0:
	# TODO: buzu

def key(event):
	global variables
	global stop_flag

	global start_canvas
	global stop_canvas

	global root
	global is_initial

	global will_red_remove
	global will_blue_remove

	RED_PLUS_S = 'd'
	RED_MINUS_S = 'c'
	RED_PLUS_C1 = 'a'
	RED_MINUS_C1 = 'z'
	RED_PLUS_C2 = 's'
	RED_MINUS_C2 = 'x'

	BLUE_PLUS_S = 'h'
	BLUE_MINUS_S = 'b'
	BLUE_PLUS_C1 = 'k'
	BLUE_MINUS_C1 = 'm'
	BLUE_PLUS_C2 = 'j'
	BLUE_MINUS_C2 = 'n'

	RED_SENSHU = 'q'
	BLUE_SENSHU = 'o'

	if event.char == RED_PLUS_S:
		tmp = variables[0].get()
		variables[0].set(tmp+1)
	elif event.char == RED_MINUS_S:
		tmp = variables[0].get()
		if tmp == 0:
			return
		variables[0].set(tmp-1)
	elif event.char == RED_PLUS_C1:
		variables[1].set(variables[1].get()+1)
	elif event.char == RED_MINUS_C1:
		tmp = variables[1].get()
		if tmp == 0:
			return
		variables[1].set(tmp-1)
	elif event.char == RED_PLUS_C2:
		variables[2].set(variables[2].get()+1)
	elif event.char == RED_MINUS_C2:
		tmp = variables[2].get()
		if tmp == 0:
			return
		variables[2].set(tmp-1)
	# blue
	elif event.char == BLUE_PLUS_S:
		variables[3].set(variables[3].get()+1)
	elif event.char == BLUE_MINUS_S:
		tmp = variables[3].get()
		if tmp == 0:
			return
		variables[3].set(tmp-1)
	elif event.char == BLUE_PLUS_C1:
		variables[4].set(variables[4].get()+1)
	elif event.char == BLUE_MINUS_C1:
		tmp = variables[4].get()
		if tmp == 0:
			return
		variables[4].set(tmp-1)
	elif event.char == BLUE_PLUS_C2:
		variables[5].set(variables[5].get()+1)
	elif event.char == BLUE_MINUS_C2:
		tmp = variables[5].get()
		if tmp == 0:
			return
		variables[5].set(tmp-1)
	elif event.char == RED_SENSHU:
		if not will_red_remove:
			red_senshu_canvas.create_oval(10, 10, 80, 80, fill="red")
		else:
			red_senshu_canvas.create_oval(10, 10, 80, 80, fill="black")
		will_red_remove = not will_red_remove
	elif event.char == BLUE_SENSHU:
		if not will_blue_remove:
			blue_senshu_canvas.create_oval(10, 10, 80, 80, fill="blue")
		else:
			blue_senshu_canvas.create_oval(10, 10, 80, 80, fill="black")
		will_blue_remove = not will_blue_remove
	elif event.char == ' ':
		if stop_flag:
			stop_flag = False
			start_canvas.create_oval(10, 30, 60, 80, fill="orange")
			stop_canvas.create_oval(10, 30, 60, 80, fill="black")
		else:
			stop_flag = True
			start_canvas.create_oval(10, 30, 60, 80, fill="black")
			stop_canvas.create_oval(10, 30, 60, 80, fill="orange")
		root.after(500, count_time)
	elif event.char == 'R':
		reset()


######## MAIN #########
is_initial = True
stop_flag = True
match_time = 90
will_red_remove = False
will_blue_remove = False

root = Tk()
variables = []
# variables are
# 0: red score
# 1: red c1
# 2: red c2
# 3: blue score
# 4: blue c2
# 5: blue c1
for i in range(6):
	variables.append(IntVar())

seconds = IntVar()
minute = IntVar()
second = StringVar()

if is_initial:
	reset()
	is_initial = False

root.attributes("-fullscreen", True)
root.configure(bg="black")

frame = Frame(root,bg="black")
frame.focus_set()
frame.bind("<Key>", key)

frame.pack()

CHAR_SIZE = 270
S_CHAR_SIZE = 100
SS_CHAR_SIZE = 70

# TODO: Add a senshu
red_score_frame = Frame(frame,highlightbackground="red", highlightcolor="red", highlightthickness=10)
red_score_frame.pack(side=LEFT, padx=5, pady=3)
Label(red_score_frame, textvariable=variables[0], bg="black",fg="yellow",font=(u'MS ゴシック', CHAR_SIZE), padx=200).pack()

blue_score_frame = Frame(frame,highlightbackground="blue", highlightcolor="blue",highlightthickness=10)
blue_score_frame.pack(padx=5, pady=3)
Label(blue_score_frame, textvariable=variables[3], bg="black",fg="yellow",font=(u'MS ゴシック', CHAR_SIZE), padx=200).pack()

# RED
leftframe = Frame(root, bg="black")
leftframe.pack( side = LEFT )

## RED C1 at grid 0,0
red_c1_frame = Frame(leftframe,highlightbackground="red", highlightcolor="red", highlightthickness=10)
red_c1_frame.grid(row=0,column=0,padx=1)
Label(red_c1_frame, textvariable=variables[1], bg="black",fg="yellow",font=(u'MS ゴシック', CHAR_SIZE)).pack()

## String "C-1" at grid 1,0
Label(leftframe, text="C-1", bg="black", fg="white", font=(u'MS ゴシック', SS_CHAR_SIZE)).grid(row=1, column=0)

## RED C2 at grid 0,1
red_c2_frame = Frame(leftframe,highlightbackground="red", highlightcolor="red", highlightthickness=10)
red_c2_frame.grid(row=0, column=1, padx=1)
Label(red_c2_frame, textvariable=variables[2], bg="black",fg="yellow",font=(u'MS ゴシック', CHAR_SIZE)).pack()

## String "C-2" at grid 1,1
Label(leftframe, text="C-2",bg="black", fg="white", font=(u'MS ゴシック', SS_CHAR_SIZE)).grid(row=1, column=1)

# BLUE
rightframe = Frame(root, bg="black")
rightframe.pack( side = RIGHT )

## BLUE C2 at grid 0,0
blue_c2_frame = Frame(rightframe,highlightbackground="blue", highlightcolor="blue", highlightthickness=10)
blue_c2_frame.grid(row=0,column=0,padx=1)
Label(blue_c2_frame, textvariable=variables[4], bg="black",fg="yellow",font=(u'MS ゴシック', CHAR_SIZE)).pack()

## String "C-2" at grid 1,0
Label(rightframe, text="C-2", bg="black", fg="white", font=(u'MS ゴシック', SS_CHAR_SIZE)).grid(row=1, column=0)

## BLUE C1 at grid 0,1
blue_c1_frame = Frame(rightframe,highlightbackground="blue", highlightcolor="blue", highlightthickness=10)
blue_c1_frame.grid(row=0, column=1, padx=1)
Label(blue_c1_frame, textvariable=variables[5], bg="black",fg="yellow",font=(u'MS ゴシック', CHAR_SIZE)).pack()

## String "C-1" at grid 1,1
Label(rightframe, text="C-1",bg="black", fg="white", font=(u'MS ゴシック', SS_CHAR_SIZE)).grid(row=1, column=1)

# Senshu & Timer & Start-Stop light
bottomframe = Frame(root, bg="black")
bottomframe.pack( side = BOTTOM )

## Senshu
senshu_frame = Frame(bottomframe, bg="black")
senshu_frame.pack()

red_senshu_canvas = Canvas(senshu_frame, width=100, height=80, bg="black", highlightthickness=0)
red_senshu_canvas.grid(row=0, column=0)
red_senshu_canvas.create_oval(10, 10, 90, 90, fill="black")

Label(senshu_frame, text="先取",bg="black", fg="white", font=(u'MS ゴシック', S_CHAR_SIZE)).grid(row=0, column=1)

blue_senshu_canvas =Canvas(senshu_frame, width=100, height=80, bg="black",highlightthickness=0)
blue_senshu_canvas.grid(row=0, column=2)
blue_senshu_canvas.create_oval(10, 10, 90, 90, fill="black")


## Timer
timer_frame = Frame(bottomframe)
timer_frame.pack()

Label(timer_frame, textvariable=minute, bg="black",fg="lime", font=(u'MS ゴシック', CHAR_SIZE-30)).pack(side=LEFT)
Label(timer_frame, text=":", bg="black",fg="lime", font=(u'MS ゴシック', CHAR_SIZE-30)).pack(side=LEFT)
Label(timer_frame, textvariable=second, bg="black",fg="lime", font=(u'MS ゴシック', CHAR_SIZE-30)).pack()

## start/stop light
ss_frame = Frame(bottomframe, bg="black")
ss_frame.pack()

start_canvas = Canvas(ss_frame, width=60, height=80, bg="black", highlightthickness=0)
start_canvas.grid(row=0, column=0)
start_canvas.create_oval(10, 30, 60, 80, fill="black")

Label(ss_frame, text="start-stop",bg="black", fg="white", font=(u'MS ゴシック', S_CHAR_SIZE)).grid(row=0, column=1)

stop_canvas =Canvas(ss_frame, width=60, height=80, bg="black",highlightthickness=0)
stop_canvas.grid(row=0, column=2)
stop_canvas.create_oval(10, 30, 60, 80, fill="orange")

root.mainloop()
