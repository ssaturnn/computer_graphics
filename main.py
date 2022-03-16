'''
Будем называть два многоугольника подобными, если существует взаимно
однозначное отображение сторон этих двух фигур такое, что соответствующие
стороны пропорциональны с коэффициентом пропорциональности k, а углы,
образованные двумя соответствующими сторонами, равны.
Найти два подобных N-угольника, где N – максимально возможное.
Многоугольники задаются на плоскости координатами вершин контуров. Вершины
в контуре перечисляются в порядке обхода против часовой стрелки. Считать, что
две величины равны с точностью до двух знаков после запятой.
'''
#import
from glob import glob
from math import sqrt
from msilib.schema import Error
from tkinter import *
import tkinter.messagebox as mb

from matplotlib.pyplot import title

#ERRORS
class Error(Exception):
    pass
class NisNotDefined(Error):
    """N is not defined"""
    pass

#ARRAYS
polygon1_points = []
polygon2_points = []
N = -1

#creating window
window = Tk()
window.title("Lab 01")
window.geometry('1200x1200')


#creating Canvas
canv = Canvas(window, width=1200, height=800, bg='black')
canv.grid(row=0, column=0, columnspan=6, sticky="N")


#Info
def aboutprog():
    mb.showinfo(title='About program', message='Будем называть два многоугольника подобными, если существует взаимно \
однозначное отображение сторон этих двух фигур такое, что соответствующие \
стороны пропорциональны с коэффициентом пропорциональности k, а углы, \
образованные двумя соответствующими сторонами, равны. \
Найти два подобных N-угольника, где N – максимально возможное. \
Многоугольники задаются на плоскости координатами вершин контуров. Вершины \
в контуре перечисляются в порядке обхода против часовой стрелки. Считать, что \
две величины равны с точностью до двух знаков после запятой.')


def aboutauthor():
    mb.showinfo(title='Author', message='Турчанинов Александр ИУ7-44Б')


def quitprog():
    window.quit()

#BUTTON_FUNCS
#Polygon 1
def clear_x1():
    input_x1_entry.delete(0, END)

def clear_y1():
    input_y1_entry.delete(0, END)

def clear_all1():
    input_x1_entry.delete(0, END)
    input_y1_entry.delete(0, END)

def add_point_to_polygon1():
    try:
        global count1
        global N
        global polygon1_points
        if N == -1:
            raise NisNotDefined
        count1+=1
        if count1 > N:
            raise ValueError
        x = int(input_x1_entry.get())
        y = int(input_y1_entry.get())
        polygon1_points.append(x)
        polygon1_points.append(y)
    except NisNotDefined:
        mb.showerror(title="Error", message="You should define the amount of sides first")
    except ValueError:
        mb.showerror(title="Error", message="Too many points")
    except:
        mb.showerror(title="Error", message="Incorrect point coords input for polygon2")

#Polygon 2
def clear_x2():
    input_x2_entry.delete(0, END)

def clear_y2():
    input_y2_entry.delete(0, END)

def clear_all2():
    input_x2_entry.delete(0, END)
    input_y2_entry.delete(0, END)

def add_point_to_polygon2():
    try:
        global count2
        global N
        global polygon2_points
        if N == -1:
            raise NisNotDefined
        count2+=1
        if count2 > N:
            raise ValueError
        x = int(input_x2_entry.get())
        y = int(input_y2_entry.get())
        polygon2_points.append(x)
        polygon2_points.append(y)
    except NisNotDefined:
        mb.showerror(title="Error", message="You should define the amount of sides first")    
    except ValueError:
        mb.showerror(title="Error", message="Too many points")
    except:
        mb.showerror(title="Error", message="Incorrect point coords input for polygon2")

#sumbit
def submit():
    try:
        global N
        global count1
        global count2
        count1 = 0
        count2 = 0
        N = int(input_sides_number_entry.get())
    except:
        mb.showerror(title="Error", message="Incorrect sides amount input")


#LABELS AND ENTRYS
#Polygon1
for_polygon_1_label = Label(window, text="Polygon 1")
for_polygon_1_label.grid(column=1, row=1, sticky="W")

input_x1_label = Label(window, text='Input X1:')
input_x1_label.grid(column=1, row=2, sticky="W")

input_y1_label = Label(window, text='Input Y1:')
input_y1_label.grid(column=1, row=4, sticky="W")

input_x1_entry = Entry(window, width=20)
input_x1_entry.grid(column=1, row=3, sticky="W")

input_y1_entry = Entry(window, width=20)
input_y1_entry.grid(column=1, row=5, sticky="W")

#Polygon2
for_polygon_2_label = Label(window, text="Polygon 2")
for_polygon_2_label.grid(column=3, row=1, sticky="E")

input_x2_label = Label(window, text='Input X2:')
input_x2_label.grid(column=3, row=2, sticky="E")

input_y2_label = Label(window, text='Input Y2:')
input_y2_label.grid(column=3, row=4, sticky="E")

input_x2_entry = Entry(window, width=20)
input_x2_entry.grid(column=3, row=3, sticky="E")

input_y2_entry = Entry(window, width=20)
input_y2_entry.grid(column=3, row=5, sticky="E")

#Sides amount
input_sides_number_label = Label(window, text="Enter the amount of sides:")
input_sides_number_label.grid(column=0, row=1, sticky="W")

input_sides_number_entry = Entry(window, width=15)
input_sides_number_entry.grid(column=0, row=2, sticky="W")

#BUTTONS
#Buttons for polygon1
add_to_polygon1_point_button = Button(window, text="Add point to polygon1", command=add_point_to_polygon1)
add_to_polygon1_point_button.grid(column=1, row=6, sticky="W")

clear_entry_x1_button = Button(window, text="clear X1", command=clear_x1)
clear_entry_x1_button.grid(column=2, row=3, sticky="W")

clear_entry_y1_button = Button(window, text="clear Y1", command=clear_y1)
clear_entry_y1_button.grid(column=2, row=4, sticky="W")

clear_entry_x1_and_y_button = Button(window, text="clear all1", command=clear_all1)
clear_entry_x1_and_y_button.grid(column=2, row=5, sticky="W")

#Buttons for polygon2
add_to_polygon2_point_button = Button(window, text="Add point to polygon2", command=add_point_to_polygon2)
add_to_polygon2_point_button.grid(column=3, row=6, sticky="E")

clear_entry_x2_button = Button(window, text="clear X2", command=clear_x2)
clear_entry_x2_button.grid(column=4, row=3, sticky="E")

clear_entry_y2_button = Button(window, text="clear Y2", command=clear_y2)
clear_entry_y2_button.grid(column=4, row=4, sticky="E")

clear_entry_x2_and_y_button = Button(window, text="clear all2", command=clear_all2)
clear_entry_x2_and_y_button.grid(column=4, row=5, sticky="E")


#Buttons for similarness and sides amount
check_for_similarness_button = Button(window, text="Check similarness")
check_for_similarness_button.grid(column=0, row=3, sticky="W")

submit_sides_amount_button = Button(window, text="Submit", command=submit)
submit_sides_amount_button.grid(column=0, row=2)




#MAIN MENU
mainmenu = Menu(window)
window.config(menu=mainmenu)

mainmenu.add_command(label='About Program', command=aboutprog)
mainmenu.add_command(label='Author', command=aboutauthor)
mainmenu.add_command(label='Quit', command=quitprog)


#mainloop
window.mainloop()