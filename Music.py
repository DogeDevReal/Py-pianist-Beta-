from multiprocessing.connection import wait
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from pynput.keyboard import Key, Controller
import time
root = Tk()
n = 30

root.title('MyKeyboard')
root.geometry("600x200")
root.maxsize(600,200)
root.iconbitmap('Icon2.ico')
p = 0.2
y = 0.2
def bruh():
    keyboard = Controller()
    time.sleep(1)
    keyboard.press("g")
    time.sleep(y)
    keyboard.release("g")

    time.sleep(p)
    keyboard.press("h")
    time.sleep(y)
    keyboard.release("h")   

    time.sleep(p)
    keyboard.press("g")
    time.sleep(y)
    keyboard.release("g")

    time.sleep(p)
    keyboard.press("k")
    time.sleep(y)
    keyboard.release("k")

    time.sleep(p)
    keyboard.press("j")
    time.sleep(y)
    keyboard.release("j")
    time.sleep(p)

    keyboard.press("g")
    time.sleep(y)
    keyboard.release("g")

    time.sleep(p)
    keyboard.press("g")
    time.sleep(y)
    keyboard.release("g")

    time.sleep(p)
    keyboard.press("h")
    time.sleep(y)
    keyboard.release("h")

    time.sleep(p)
    keyboard.press("g")
    time.sleep(y)
    keyboard.release("g")

    time.sleep(p)
    keyboard.press("l")
    time.sleep(y)
    keyboard.release("l")

    time.sleep(p)
    keyboard.press("k")
    time.sleep(y)
    keyboard.release("k")

    time.sleep(p)
    keyboard.press("g")
    time.sleep(y)
    keyboard.release("g")

    time.sleep(p)
    keyboard.press("g")
    time.sleep(y)
    keyboard.release("g")

    time.sleep(p)
    keyboard.press("g")
    time.sleep(y)
    keyboard.release("g")

    time.sleep(p)
    keyboard.press(";")
    time.sleep(y)
    keyboard.release(";")  

    time.sleep(p)
    keyboard.press("k")
    time.sleep(y)
    keyboard.release("k")

    time.sleep(p)
    keyboard.press("k")
    time.sleep(y)
    keyboard.release("k")  

    time.sleep(p)
    keyboard.press("j")
    time.sleep(y)
    keyboard.release("j")

    time.sleep(p)
    keyboard.press("h")
    time.sleep(y)
    keyboard.release("h")

    time.sleep(p)
    keyboard.press("'")
    time.sleep(y)
    keyboard.release("'")

    time.sleep(p)
    keyboard.press("'")
    time.sleep(y)
    keyboard.release("'")

    time.sleep(p)
    keyboard.press(";")
    time.sleep(y)
    keyboard.release(";")

    time.sleep(p)
    keyboard.press("k")
    time.sleep(y)
    keyboard.release("k")

    time.sleep(p)
    keyboard.press("l")
    time.sleep(y)
    keyboard.release("l")

    time.sleep(p)
    keyboard.press("k")
    time.sleep(y)
    keyboard.release("k")


B1 = Button(root, text = 'play happy birthday',command= bruh)
B1.place(x = 30 , y  = 30)
root.mainloop()
