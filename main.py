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
points_list = []
last_act = []

#creating window
window = Tk()
window.title("Lab 01")

#creating Canvas
canv = Canvas(window, width=1000, height=1000, bg='white')
canv.grid(row=0, column=0)

zero = canv.create_oval(0, 0, 0, 0, state=HIDDEN)


#FUNCS
def str_to_float(str):
    try:
        x = float(str)
        return x
    except:
        return str



def create_point(x, y, text=0):
    point_id = canv.create_oval(x - 0.1, y - 0.1, x + 0.1, y + 0.1, width=3, outline='black', fill='black', activeoutline='gray34', activefill='gray34')
    last_act.clear()
    last_act.append('del')
    last_act.append('poi')
    last_act.append(point_id)
    if text == 1:
        x -= canv.coords(zero)[0]
        y -= canv.coords(zero)[1]
    points_list.append([x, y, point_id])


def point_coords(event):
    xp = event.x
    yp = event.y
    create_point(xp, yp)


def finish_point_draw(event):
    canv.unbind('<Button-1>')
    canv.unbind('<ButtonRelease-1>')


def start_point_draw():
    lblpointerr.grid_forget()
    canv.bind('<Button-1>', point_coords)
    canv.bind('<ButtonRelease-1>', finish_point_draw)


def point_text():
    lblpointerr.grid_forget()
    pointx = str_to_float(enter_point_x.get())
    pointy = str_to_float(enter_point_y.get())
    if type(pointx) != float or type(pointy) != float:
        lblpointerr.grid(row=5, column=0)
        return
    pointx += canv.coords(zero)[0]
    pointy += canv.coords(zero)[1]
    create_point(pointx, pointy, text=1)
    enter_point_x.delete(0, END)
    enter_point_y.delete(0, END)




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



#BUTTONS
frmpaint = Frame(window)
frmtext = Frame(window)

point_btn = Button(frmpaint, text='◦', command=start_point_draw)
point_btn.grid(row=0, column = 1)

#undo_btn = Button(frmpaint, text='↺', command=undo_last_act)
#undo_btn.grid(row=0, column=2)

frmpaint.grid(row=0, column=1, sticky=N)

enter_point_x = Entry(frmtext)
label_point_x = Label(frmtext, text='Координата X точки')
label_point_x.grid(row=0, column=0)
enter_point_x.grid(row=1, column=0)

enter_point_y = Entry(frmtext)
label_point_y = Label(frmtext, text='Координата Y точки')
label_point_y.grid(row=2, column=0)
enter_point_y.grid(row=3, column=0)

btnpointtext = Button(frmtext, text='Нарисовать точку', command=point_text)
lblpointerr = Label(frmtext, text='Некорректные координаты точки')
btnpointtext.grid(row=4, column=0)



#MAIN MENU
mainmenu = Menu(window)
window.config(menu=mainmenu)

mainmenu.add_command(label='About Program', command=aboutprog)
mainmenu.add_command(label='Author', command=aboutauthor)
mainmenu.add_command(label='Quit', command=quitprog)

frmtext.grid(row=0, column=2, sticky=N)

#mainloop
window.mainloop()

