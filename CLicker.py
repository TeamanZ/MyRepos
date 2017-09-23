from tkinter import *
from pyautogui import *
import sys

def Mclick(event):
    while True:
        tripleClick(x=800, y=450,)


def Mclick2(event):
    while True:
        tripleClick(x=960, y=540,)

root = Tk()
root.title('АвтоКликер By Teaman')

label1=Label(root,text='Расположите объект для кликов по центру экрана.',font='Impact 13')
label1.pack()

label11=Label(root,text='Set the subject in the center of the screen.',font='Impact 13')
label11.pack()

btn1=Button(root,text='Запустить кликер {1600x900}',fg='green')
btn1.pack()

btn2=Button(root,text='Запустить кликер {1920x1080}',fg='green')
btn2.pack()

label2=Label(text='Для закрытия программы переместите курсор в левый верхний угол экрана.',font='Impact 16',fg='red')
label2.pack()

label22=Label(text='To close the program move the cursor to the top left corner.',font='Impact 16',fg='red')
label22.pack()

btn1.bind("<Button-1>",Mclick)
btn2.bind("<Button-1>",Mclick2)

root.mainloop()
