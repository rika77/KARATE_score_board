# -*- coding: utf-8 -*-

from tkinter import*
import threading
import time

# TODO: Support another match_time ex. python3 main.py -s=60
def reset(event=None):
	global match_time
	for i in range(6):
		variables[i].set(0)

	seconds.set(match_time)
	minute.set(int(match_time/60))
	second.set(match_time%60)

	stop_flag = False
	thread = None

def count_time():
	global stop_flag

	global seconds
	global minute
	global second

	while not stop_flag and seconds.get() != 0:
		# if seconds == 15:
		# TODO: buzu
		time.sleep(1)
		tmp = seconds.get()
		seconds.set(tmp-1)
		minute.set(int((tmp-1)/60))
		second.set((tmp-1)%60)

	# if seconds == 0:
	# TODO: buzu

def key(event):
	global variables
	global stop_flag
	global thread

	global start_canvas
	global stop_canvas

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

	# red
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
	elif event.char == ' ':
		if not thread:
			thread = threading.Thread(target=count_time)
			stop_flag = False
			thread.start()
			start_canvas.grid(row=0, column=0)
			stop_canvas.grid_forget()
		else:
			stop_flag = True
			thread=None
			stop_canvas.grid(row=0, column=2)
			start_canvas.grid_forget()
	elif event.char == 'R':
		reset()

is_initial = True
stop_flag = False
thread = None
match_time = 90

root = Tk()
variables = []
for i in range(6):
	variables.append(IntVar())

seconds = IntVar()
minute = IntVar()
second = IntVar()


if is_initial:
	reset()
	is_initial = False

root.attributes("-fullscreen", True)
root.configure(bg="black")

frame = Frame(root,bg="black")
frame.focus_set()
frame.bind("<Key>", key)

frame.pack()

CHAR_SIZE = 300
S_CHAR_SIZE = 100
SS_CHAR_SIZE = 70

# TODO: Add a senshu
red_score_frame = Frame(frame,highlightbackground="red", highlightcolor="red", highlightthickness=10)
red_score_frame.pack(side=LEFT, padx=5, pady=3)
Label(red_score_frame, textvariable=variables[0], bg="black",fg="yellow",font=(u'MS ゴシック', CHAR_SIZE), padx=200).pack()

blue_score_frame = Frame(frame,highlightbackground="blue", highlightcolor="blue",highlightthickness=10)
blue_score_frame.pack(padx=5, pady=3)
Label(blue_score_frame, textvariable=variables[3], bg="black",fg="yellow",font=(u'MS ゴシック', CHAR_SIZE), padx=200).pack()

leftframe = Frame(root, bg="black")
leftframe.pack( side = LEFT )

# grid 0,0
red_c1_frame = Frame(leftframe,highlightbackground="red", highlightcolor="red", highlightthickness=10)
red_c1_frame.grid(row=0,column=0,padx=1)
Label(red_c1_frame, textvariable=variables[1], bg="black",fg="yellow",font=(u'MS ゴシック', CHAR_SIZE)).pack()

# grid 1,0
Label(leftframe, text="C-1", bg="black", fg="white", font=(u'MS ゴシック', SS_CHAR_SIZE)).grid(row=1, column=0)

# grid 0,1
red_c2_frame = Frame(leftframe,highlightbackground="red", highlightcolor="red", highlightthickness=10)
red_c2_frame.grid(row=0, column=1, padx=1)
Label(red_c2_frame, textvariable=variables[2], bg="black",fg="yellow",font=(u'MS ゴシック', CHAR_SIZE)).pack()

# grid 1,1
Label(leftframe, text="C-2",bg="black", fg="white", font=(u'MS ゴシック', SS_CHAR_SIZE)).grid(row=1, column=1)

rightframe = Frame(root, bg="black")
rightframe.pack( side = RIGHT )

# grid 0,0
blue_c1_frame = Frame(rightframe,highlightbackground="blue", highlightcolor="blue", highlightthickness=10)
blue_c1_frame.grid(row=0,column=0,padx=1)
Label(blue_c1_frame, textvariable=variables[4], bg="black",fg="yellow",font=(u'MS ゴシック', CHAR_SIZE)).pack()

# grid 1,0
Label(rightframe, text="C-2", bg="black", fg="white", font=(u'MS ゴシック', SS_CHAR_SIZE)).grid(row=1, column=0)

# grid 0,1
blue_c2_frame = Frame(rightframe,highlightbackground="blue", highlightcolor="blue", highlightthickness=10)
blue_c2_frame.grid(row=0, column=1, padx=1)
Label(blue_c2_frame, textvariable=variables[5], bg="black",fg="yellow",font=(u'MS ゴシック', CHAR_SIZE)).pack()

# grid 1,1
Label(rightframe, text="C-1",bg="black", fg="white", font=(u'MS ゴシック', SS_CHAR_SIZE)).grid(row=1, column=1)

bottomframe = Frame(root, bg="black")
bottomframe.pack( side = BOTTOM )

# Timer
timer_frame = Frame(bottomframe)
timer_frame.pack()

Label(timer_frame, textvariable=minute, bg="black",fg="lime", font=(u'MS ゴシック', CHAR_SIZE-30)).pack(side=LEFT)
Label(timer_frame, text=":", bg="black",fg="lime", font=(u'MS ゴシック', CHAR_SIZE-30)).pack(side=LEFT)
Label(timer_frame, textvariable=second, bg="black",fg="lime", font=(u'MS ゴシック', CHAR_SIZE-30)).pack()

# start/stop light
ss_frame = Frame(bottomframe, bg="black")
ss_frame.pack()

start_canvas = Canvas(ss_frame, width=60, height=80, bg="black", highlightthickness=0)
start_canvas.create_oval(10, 30, 60, 80, fill="orange")

Label(ss_frame, text="start-stop",bg="black", fg="white", font=(u'MS ゴシック', S_CHAR_SIZE)).grid(row=0, column=1)

stop_canvas =Canvas(ss_frame, width=60, height=80, bg="black",highlightthickness=0)
stop_canvas.grid(row=0, column=2)
stop_canvas.create_oval(10, 30, 60, 80, fill="orange")

root.mainloop()


stop_flag = True
thread.join()