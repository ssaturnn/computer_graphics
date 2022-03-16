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
from math import sqrt
from tkinter import *
import tkinter.messagebox as mb


#ARRAYS


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


#LABELS AND ENTRYS
input_x_label = Label(window, text='Input X:')
input_x_label.grid(column=1, row=1, sticky="W")

input_y_label = Label(window, text='Input Y:')
input_y_label.grid(column=1, row=3, sticky="W")

input_x_entry = Entry(window, width=20)
input_x_entry.grid(column=1, row=2, sticky="W")

input_y_entry = Entry(window, width=20)
input_y_entry.grid(column=1, row=4, sticky="W")

input_sides_number_label = Label(window, text="Enter the amount of sides:")
input_sides_number_label.grid(column=0, row=1, sticky="W")

input_sides_number_entry = Entry(window, width=10)
input_sides_number_entry.grid(column=0, row=2, sticky="W")

#BUTTONS
add_point_button = Button(window, text="Add point")
add_point_button.grid(column=1, row=5, sticky="W")


clear_entry_x_button = Button(window, text="clear X")
clear_entry_x_button.grid(column=2, row=2, sticky="W")

clear_entry_y_button = Button(window, text="clear Y")
clear_entry_y_button.grid(column=2, row=3, sticky="W")

clear_entry_x_button = Button(window, text="clear all")
clear_entry_x_button.grid(column=2, row=4, sticky="W")

check_for_similarness_button = Button(window, text="Check similarness")
check_for_similarness_button.grid(column=0, row=3, sticky="W")




#MAIN MENU
mainmenu = Menu(window)
window.config(menu=mainmenu)

mainmenu.add_command(label='About Program', command=aboutprog)
mainmenu.add_command(label='Author', command=aboutauthor)
mainmenu.add_command(label='Quit', command=quitprog)


#mainloop
window.mainloop()