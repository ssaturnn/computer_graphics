import copy
import math
import sys
from math import fabs, floor
from tkinter import Tk, Button, Label, Entry, Canvas, messagebox, Menu, Frame, SUNKEN, colorchooser
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from colorutils import Color

WIDTH = 1200
HEIGHT = 600
RADIUS = 3

EPS = 1e-8

cat_pic = []
pre = []

cb = Color(hex='#7fffd4')

TASK = '''Нарисовать картинку, крутить её'''

def exit_prog():
    sys.exit()

def del_all_dots():
    global last_activity, dots
    dots.clear()
    last_activity.append(copy.deepcopy(dots))
    canvas.delete("all")


    



def main():
    global canvas

    #Окно
    root = Tk()
    root.geometry("%dx%d" % (WIDTH, HEIGHT))
    root.title("Лабораторная работа №3")
    root.minsize(WIDTH, HEIGHT)
    root["bg"] = "#40e0d0"


 

    #Координаты отрезка
    label_x1 = Label(root, text="X1:", anchor='c',
                              bg='#00ffff')
    label_x1.place(relx=0, rely=0.21, relwidth=0.04, relheight=0.06)
    line_x1 = Entry(root, bg='#00ffff')
    line_x1.place(relx=0.045, rely=0.21, relwidth=0.04, relheight=0.06)

    label_y1 = Label(root, text="Y1:", anchor='c',
                              bg='#00ffff')
    label_y1.place(relx=0.15, rely=0.21, relwidth=0.04, relheight=0.06)
    line_y1 = Entry(root, bg='#00ffff')
    line_y1.place(relx=0.195, rely=0.21, relwidth=0.04, relheight=0.06)

    label_x2 = Label(root, text="X2:", anchor='c',
                              bg='#00ffff')
    label_x2.place(relx=0, rely=0.275, relwidth=0.04, relheight=0.06)
    line_x2 = Entry(root, bg='#00ffff')
    line_x2.place(relx=0.045, rely=0.275, relwidth=0.04, relheight=0.06)

    label_y2 = Label(root, text="Y2:", anchor='c',
                              bg='#00ffff')
    label_y2.place(relx=0.15, rely=0.275, relwidth=0.04, relheight=0.06)
    line_y2 = Entry(root, bg='#00ffff')
    line_y2.place(relx=0.195, rely=0.275, relwidth=0.04, relheight=0.06)

    line_btn = Button(text="Построить отрезок",
                  bg='#00ffff',
                  activebackground='#00ffff',
                  command=lambda: drawLine([line_x1.get(), line_y1.get()],
                  [line_x2.get(), line_y2.get()], color_combo.current(),
                   method_combo.current()))
    line_btn.place(relx=0, rely=0.345, relwidth=0.3, relheight=0.08)

    #Спектр
    menu_label_spectr = Label(text="Спектр:", anchor='w', bg='#00ffff')
    menu_label_spectr.place(relx=0.7, rely=0, relwidth=0.3, relheight=0.05)

    label_len = Label(root, text="Длина:", anchor='c',
                              bg='#00ffff')
    label_len.place(relx=0.7, rely=0.06, relwidth=0.15, relheight=0.06)
    len_spectr = Entry(root, bg='#00ffff')
    len_spectr.place(relx=0.855, rely=0.06, relwidth=0.14, relheight=0.06)

    label_angle = Label(root, text="Угол:", anchor='c',
                             bg='#00ffff')
    label_angle.place(relx=0.7, rely=0.13, relwidth=0.15, relheight=0.06)
    angle_spectr = Entry(root, bg='#00ffff')
    angle_spectr.place(relx=0.855, rely=0.13, relwidth=0.14, relheight=0.06)

    spectr_btn = Button(text="Построить спектр",
                      bg='#00ffff',
                      activebackground='#00ffff',
                      command=lambda: drawSpectr(len_spectr.get(),
                      color_combo.current(), angle_spectr.get(),
                      method_combo.current()))
    spectr_btn.place(relx=0.7, rely=0.23, relwidth=0.3, relheight=0.08)

    #Диаграмма
    plt_1_btn = Button(text="Диаграмма ступенчатости", bg='#00ffff',
                    activebackground='#00ffff',
                    command=lambda: step_diagram(len_spectr.get()))

    plt_1_btn.place(relx=0.7, rely=0.34, relwidth=0.3, relheight=0.08)


    #Canvas
    canvas = Canvas(root, bg="#fff", #148012
                        highlightthickness=4, highlightbackground="#40e0d0")
    canvas.place(relx=0.3, rely=0, relwidth=0.4, relheight=1)
    canvas.bind("<Button-1>", lambda e: add_dot_event(e, color_combo.current(),
                method_combo.current()))

    #Меню
    menu = Menu(root)
    root.config(menu=menu)
    menu.add_command(label="Задание", command=lambda:\
                        messagebox.showinfo("Задание", TASK))
    menu.add_command(label="Автор",command=lambda:\
                        messagebox.showinfo("Автор", "Турчанинов Александр ИУ7-44Б"))
    menu.add_command(label="Очистить холст", command=lambda:\
                        del_all_dots())
    #menu.add_command(label="Построить с шагом")#, command=special_add)
    menu.add_command(label="Выход", command=root.destroy)


    root.mainloop()

if __name__ == "__main__":
    main()
