# -*- coding: utf-8 -*-

from tkinter import*
import threading
import time

# TODO: Support another match_time ex. python3 main.py -s=60
def reset(match_time):
	for i in range(6):
		variables[i].set(0)

	seconds.set(match_time)
	minute.set(int(match_time/60))
	second.set(match_time%60)

	stop_flag = False

def count_time():
	global stop_flag

	global seconds
	global minute
	global second

	while not stop_flag and seconds.get() != 0:
		# if seconds == 15:
		# TODO: buzu
		tmp = seconds.get()
		seconds.set(tmp-1)
		minute.set(int((tmp-1)/60))
		second.set((tmp-1)%60)
		time.sleep(1)

	# if seconds == 0:
	# TODO: buzu

def key(event):
	global variables
	global sop_flag
	global thread

	RED_PLUS_S = 'f'
	RED_MINUS_S = 'v'
	RED_PLUS_C1 = 'd'
	RED_MINUS_C1 = 'c'
	RED_PLUS_C2 = 's'
	RED_MINUS_C2 = 'x'

	BLUE_PLUS_S = 'j'
	BLUE_MINUS_S = 'n'
	BLUE_PLUS_C1 = 'k'
	BLUE_MINUS_C1 = 'm'
	BLUE_PLUS_C2 = 'l'
	BLUE_MINUS_C2 = ','

	if event.char == RED_PLUS_S:
		variables[0].set(variables[0].get()+1)
	elif event.char == BLUE_PLUS_S:
		variables[3].set(variables[3].get()+1)
	elif event.char == " ":
		if not thread:
			thread = threading.Thread(target=count_time)
			stop_flag = False
			thread.start()
		else:
			stop_flag = True
			thread.join()
			thread=None
	else:
		print(ord(event.char))


is_initial = True
stop_flag = False
thread = None

root = Tk()
variables = []
for i in range(6):
	variables.append(IntVar())
seconds = IntVar()
minute = IntVar()
second = IntVar()

# TODO: Add a reset 
if is_initial:
	reset(90)
	is_initial = False

root.attributes("-fullscreen", True)
root.configure(bg="black")

frame = Frame(root,bg="black")
frame.focus_set()
frame.bind("<Key>", key)

frame.pack()

CHAR_SIZE = 300

# TODO: Add a senshu
red_score_frame = Frame(frame,highlightbackground="red", highlightcolor="red", highlightthickness=10)
red_score_frame.pack(side=LEFT, padx=5)
Label(red_score_frame, textvariable=variables[0], bg="black",fg="yellow",font=(u'MS ゴシック', CHAR_SIZE), padx=200).pack()

blue_score_frame = Frame(frame,highlightbackground="blue", highlightcolor="blue",highlightthickness=10)
blue_score_frame.pack(padx=5)
Label(blue_score_frame, textvariable=variables[3], bg="black",fg="yellow",font=(u'MS ゴシック', CHAR_SIZE), padx=200).pack()

leftframe = Frame(root, bg="black")
leftframe.pack( side = LEFT )

red_c1_frame = Frame(leftframe,highlightbackground="red", highlightcolor="red", highlightthickness=10)
red_c1_frame.pack(side=LEFT, padx=1)
Label(red_c1_frame, textvariable=variables[1], bg="black",fg="yellow",font=(u'MS ゴシック', CHAR_SIZE)).pack()

red_c2_frame = Frame(leftframe,highlightbackground="red", highlightcolor="red", highlightthickness=10)
red_c2_frame.pack(padx=1)
Label(red_c2_frame, textvariable=variables[2], bg="black",fg="yellow",font=(u'MS ゴシック', CHAR_SIZE)).pack()

rightframe = Frame(root, bg="black")
rightframe.pack( side = RIGHT )

blue_c1_frame = Frame(rightframe,highlightbackground="blue", highlightcolor="blue", highlightthickness=10)
blue_c1_frame.pack(side=RIGHT, padx=1)
Label(blue_c1_frame, textvariable=variables[4], bg="black",fg="yellow",font=(u'MS ゴシック', CHAR_SIZE)).pack()

blue_c2_frame = Frame(rightframe,highlightbackground="blue", highlightcolor="blue", highlightthickness=10)
blue_c2_frame.pack(padx=1)
Label(blue_c2_frame, textvariable=variables[5], bg="black",fg="yellow",font=(u'MS ゴシック', CHAR_SIZE)).pack()

bottomframe = Frame(root, bg="black")
bottomframe.pack( side = BOTTOM )

# Timer
timer_frame = Frame(bottomframe)
timer_frame.pack()

Label(timer_frame, textvariable=minute, bg="black",fg="lime", font=(u'MS ゴシック', CHAR_SIZE-30)).pack(side=LEFT)
Label(timer_frame, text=":", bg="black",fg="lime", font=(u'MS ゴシック', CHAR_SIZE-30)).pack(side=LEFT)
Label(timer_frame, textvariable=second, bg="black",fg="lime", font=(u'MS ゴシック', CHAR_SIZE-30)).pack()

ss_frame = Frame(bottomframe)
ss_frame.pack()
Label(ss_frame, text="start-stop",bg="black", fg="white", font=(u'MS ゴシック', 100)).pack()
root.mainloop()

stop_flag = True
thread.join()