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
from email import message
from math import sqrt
from tkinter import *
import tkinter.messagebox as mb

#creating window
window = Tk()
width = '1000' #window width
height = '1000' #window height
geometry_of_window = width + 'x' + height
window.geometry(geometry_of_window)
window.title("Lab 01")

#creating Canvas
canv = Canvas(window, width=1000, height=1000, bg='black')
canv.grid(row=0, column=0)

#FUNCS
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
    mb.showinfo(title='Author', message='Турчанинов Александр ИУ7-34Б')


def quitprog():
    window.quit()

#buttons/labels/entrys
#Label INITIALIZATION


#Label Add point





#MAIN MENU
mainmenu = Menu(window)
window.config(menu=mainmenu)

mainmenu.add_command(label='About Program', command=aboutprog)
mainmenu.add_command(label='Author', command=aboutauthor)
mainmenu.add_command(label='Quit', command=quitprog)

#mainloop
window.mainloop()

