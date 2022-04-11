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
from cmath import acos
from glob import glob
from math import sqrt
from math import acos
from math import degrees
from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk

from matplotlib.pyplot import title

#ERRORS
class Error(Exception):
    pass
class NisNotDefined(Error):
    """N is not defined"""
    pass

class Ncannotbe2orLower(Error):
    pass

class LessPointsThanN(Error):
    pass

#ARRAYS
polygon1_points = []
polygon2_points = []
point1_number = []
point2_number = []
N = -1

#creating window
window = Tk()
window.title("Lab 01")
window.geometry('1221x620')

#Creating Frames
Frame_for_polygon1 = Frame(window)
Frame_for_polygon2 = Frame(window)
Frame_for_canvas = Frame(window)
Frame_for_actions = Frame(window)
Frame_for_polygon1.grid(row=0, column=0)
Frame_for_canvas.grid(row=0, column=1)
Frame_for_polygon2.grid(row=0, column=2)
Frame_for_actions.grid(row=1, column=1)

#creating Canvas
canv = Canvas(Frame_for_canvas, width=690, height=520, bg='white')
canv.grid(row=0, column=0)


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
        point1_number.append(count1)
        points1_combobox.configure(values=point1_number)
        x = int(input_x1_entry.get())
        y = int(input_y1_entry.get())
        polygon1_points[count1-1].append(x)
        polygon1_points[count1-1].append(y)
        if count1 != 1:
            polygon1_points[count1-2].append(x)
            polygon1_points[count1-2].append(y)
        if count1 == N:
            polygon1_points[count1-1].append(polygon1_points[0][1])
            polygon1_points[count1-1].append(polygon1_points[0][2])
        print(polygon1_points)
        clear_all1()
    except NisNotDefined:
        mb.showerror(title="Error", message="You should define the amount of sides first")
    except ValueError:
        mb.showerror(title="Error", message="Too many points")
    except:
        mb.showerror(title="Error", message="Incorrect point coords input for polygon2")

#Draw Polygon 1
def draw_polygon1():
    global N
    global polygon1_points
    try:
        if len(polygon1_points) < N * 2:
            raise LessPointsThanN
        canv.create_polygon(polygon1_points, fill="white", outline="black")
    except LessPointsThanN:
        mb.showerror(title="Error", message="Enter more Points")
    except:
        mb.showerror(title="Error", message="You should add points at first")


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
        point2_number.append(count2)
        points2_combobox.configure(values=point2_number)
        x = int(input_x2_entry.get())
        y = int(input_y2_entry.get())
        polygon2_points[count2-1].append(x)
        polygon2_points[count2-1].append(y)
        if count2 != 1:
            polygon2_points[count2-2].append(x)
            polygon2_points[count2-2].append(y)
        if count2 == N:
            polygon2_points[count2-1].append(polygon2_points[0][1])
            polygon2_points[count2-1].append(polygon2_points[0][2])
        print(polygon2_points)
        clear_all2()
    except NisNotDefined:
        mb.showerror(title="Error", message="You should define the amount of sides first")
    except ValueError:
        mb.showerror(title="Error", message="Too many points")
    except:
        mb.showerror(title="Error", message="Incorrect point coords input for polygon2")

#Draw Polygon 2
def draw_polygon2():
    global N
    global polygon2_points
    try:
        if len(polygon2_points) < N * 2:
            raise LessPointsThanN
        canv.create_polygon(polygon2_points, fill="white", outline="black")
    except LessPointsThanN:
        mb.showerror(title="Error", message="Enter more Points")
    except:
        mb.showerror(title="Error", message="You should add points at first")

#sumbit
def submit():
    try:
        global N
        global count1
        global count2
        global polygon1_points
        global polygon2_points
        count1 = 0
        count2 = 0
        polygon1_points = []
        polygon2_points = []
        N = int(input_sides_number_entry.get())
        for i in range(0, N):
            polygon1_points.append([i+1])
        for i in range(0, N):
            polygon2_points.append([i+1])
        if N <=2:
            raise Ncannotbe2orLower
    except Ncannotbe2orLower:
        mb.showerror(title="Error", message="Amount of sides cannot be 2 or lower")
    except:
        mb.showerror(title="Error", message="Incorrect sides amount input")


#Finding all angles
def find_angles_of_polygon1():
    global N
    global polygon1_points
    global polygon2_points
    #polygon 1
    print(polygon1_points)
    for i in range(1, N):
        #Left angle count
        if i != N-1:
            xvector = polygon1_points[i][3] - polygon1_points[i][1]
            yvector = polygon1_points[i][4] - polygon1_points[i][2]
            yvector_next = polygon1_points[i+1][4] - polygon1_points[i+1][2]
            xvector_next = polygon1_points[i+1][3] - polygon1_points[i+1][1]
            xvector_prev = (polygon1_points[i-1][3] - polygon1_points[i-1][1]) * -1
            yvector_prev = (polygon1_points[i-1][4] - polygon1_points[i-1][2]) * -1
            revx = (polygon1_points[i][3] - polygon1_points[i][1]) * -1
            revy = (polygon1_points[i][4] - polygon1_points[i][2]) * -1
            #Left angle
            scalar_left = xvector*xvector_prev + yvector*yvector_prev
            multiply_left = sqrt(xvector**2 + yvector**2) * sqrt(xvector_prev**2 + yvector_prev**2)
            angle_left = degrees(acos(scalar_left/multiply_left))
            #Right angle
            scalar_right = revx*xvector_next + revy*yvector_next
            multiply_right = sqrt(revx**2 + revy**2) * sqrt(xvector_next**2 + yvector_next**2)
            angle_right = degrees(acos(scalar_right/multiply_right))
            #Appending
            polygon1_points[i].append(angle_left)
            polygon1_points[i].append(angle_right)
        else:
            #Left angle
            angle_left = polygon1_points[-2][7]
            #Right angle
            xvector_next = polygon1_points[0][3] - polygon1_points[0][1]
            yvector_next = polygon1_points[0][4] - polygon1_points[0][2]
            revx = -1 * (polygon1_points[-1][3] - polygon1_points[-1][1])
            revy = -1 * (polygon1_points[-1][4] - polygon1_points[-1][2])
            scalar_right = revx*xvector_next + revy*yvector_next
            multiply_right = sqrt(revx**2 + revy**2) * sqrt(xvector_next**2 + yvector_next**2)
            angle_right = degrees(acos(scalar_right/multiply_right))
            #Appending
            polygon1_points[-1].append(angle_left)
            polygon1_points[-1].append(angle_right)
        #Appending to 1 position
        print("**********")
        print(polygon1_points)
        print("************")
    polygon1_points[0].append(polygon1_points[-1][7])
    polygon1_points[0].append(polygon1_points[1][6])
    print(polygon1_points)
            


        
    


#Similarness Button
def check_similarness():
    global N
    global polygon1_points
    global polygon2_points
    #drawing
    #draw_polygon1()
    #draw_polygon2()
    #finding sides size
    #1 polygon
    if polygon1_points != []:
        try:
            for i in range(0, N):
                a = sqrt((polygon1_points[i+1][1]-polygon1_points[i][1])**2 + (polygon1_points[i+1][2]-polygon1_points[i][2])**2)
                a = float("%.2f" % a)
                polygon1_points[i].append(a)
        except:
            print(i)
            a = sqrt((polygon1_points[-1][1]-polygon1_points[0][1])**2 + (polygon1_points[-1][2]-polygon1_points[0][2])**2)
            a = float("%.2f" % a)
            polygon1_points[i].append(a)
        find_angles_of_polygon1()
        print(polygon1_points)
    #2 polygon
    '''if polygon2_points != []:
        try:
            for i in range(0, N):
                a = sqrt((polygon2_points[i+1][1]-polygon2_points[i][1])**2 + (polygon2_points[i+1][2]-polygon2_points[i][2])**2)
                a = float("%.2f" % a)
                polygon2_points[i].append(a)
        except:
            a = sqrt((polygon2_points[-1][1]-polygon2_points[0][1])**2 + (polygon2_points[-1][2]-polygon2_points[0][2])**2)
            a = float("%.2f" % a)
            polygon2_points[i].append(a)'''


def clear_previous():
    global polygon1_points
    global polygon2_points
    polygon1_points = []
    polygon2_points = []

    
    


#LABELS AND ENTRYS
#Polygon1
for_polygon_1_label = Label(Frame_for_polygon1, text="Polygon 1")
for_polygon_1_label.grid(column=1, row=1, sticky="N")

input_x1_label = Label(Frame_for_polygon1, text='Input X1:')
input_x1_label.grid(column=1, row=2, sticky="N")

input_y1_label = Label(Frame_for_polygon1, text='Input Y1:')
input_y1_label.grid(column=1, row=4, sticky="N")

input_x1_entry = Entry(Frame_for_polygon1, width=20)
input_x1_entry.grid(column=1, row=3, sticky="N")

input_y1_entry = Entry(Frame_for_polygon1, width=20)
input_y1_entry.grid(column=1, row=5, sticky="N")

#Polygon2
for_polygon_2_label = Label(Frame_for_polygon2, text="Polygon 2")
for_polygon_2_label.grid(column=3, row=1, sticky="N")

input_x2_label = Label(Frame_for_polygon2, text='Input X2:')
input_x2_label.grid(column=3, row=2, sticky="N")

input_y2_label = Label(Frame_for_polygon2, text='Input Y2:')
input_y2_label.grid(column=3, row=4, sticky="N")

input_x2_entry = Entry(Frame_for_polygon2, width=20)
input_x2_entry.grid(column=3, row=3, sticky="N")

input_y2_entry = Entry(Frame_for_polygon2, width=20)
input_y2_entry.grid(column=3, row=5, sticky="N")




#Sides amount
input_sides_number_label = Label(Frame_for_actions, text="Enter the amount of sides:")
input_sides_number_label.grid(column=0, row=1, sticky="NESW")

input_sides_number_entry = Entry(Frame_for_actions, width=15)
input_sides_number_entry.grid(column=0, row=2, sticky="NSEW")


#BUTTONS
#Buttons for polygon1
add_to_polygon1_point_button = Button(Frame_for_polygon1, text="Add point to polygon1", command=add_point_to_polygon1)
add_to_polygon1_point_button.grid(column=1, row=6, sticky="W")

clear_entry_x1_button = Button(Frame_for_polygon1, text="clear X1", command=clear_x1)
clear_entry_x1_button.grid(column=2, row=3, sticky="W")

clear_entry_y1_button = Button(Frame_for_polygon1, text="clear Y1", command=clear_y1)
clear_entry_y1_button.grid(column=2, row=5, sticky="W")

clear_entry_x1_and_y_button = Button(Frame_for_polygon1, text="clear ALL1", command=clear_all1)
clear_entry_x1_and_y_button.grid(column=2, row=4, sticky="W")

draw_polygon1_button = Button(Frame_for_polygon1, text="Draw Polygon1", command=draw_polygon1)
draw_polygon1_button.grid(column=1, row=7, sticky="W")

#Buttons for polygon2
add_to_polygon2_point_button = Button(Frame_for_polygon2, text="Add point to polygon2", command=add_point_to_polygon2)
add_to_polygon2_point_button.grid(column=3, row=6, sticky="W")

clear_entry_x2_button = Button(Frame_for_polygon2, text="clear X2", command=clear_x2)
clear_entry_x2_button.grid(column=4, row=3, sticky="W")

clear_entry_y2_button = Button(Frame_for_polygon2, text="clear Y2", command=clear_y2)
clear_entry_y2_button.grid(column=4, row=5, sticky="W")

clear_entry_x2_and_y_button = Button(Frame_for_polygon2, text="clear ALL2", command=clear_all2)
clear_entry_x2_and_y_button.grid(column=4, row=4, sticky="W")

draw_polygon2_button = Button(Frame_for_polygon2, text="Draw Polygon2", command=draw_polygon2)
draw_polygon2_button.grid(column=3, row=7, sticky="W")

#COMBOBOBXES
#Polygon 1
choose_point_from_polygon1 = Label(Frame_for_polygon1, text="Points List:")
choose_point_from_polygon1.grid(column=1, row=8, sticky="W")

points1_combobox = ttk.Combobox(Frame_for_polygon1, values=point1_number)
points1_combobox.grid(column=1, row=9)

#Polygon2
choose_point_from_polygon2 = Label(Frame_for_polygon2, text="Points List:")
choose_point_from_polygon2.grid(column=3, row=8, sticky="W")

points2_combobox = ttk.Combobox(Frame_for_polygon2, values=point2_number)
points2_combobox.grid(column=3, row=9)




#Buttons for similarness and sides amount
check_for_similarness_button = Button(Frame_for_actions, text="Check Similarness", command=check_similarness)
check_for_similarness_button.grid(column=0, row=3, sticky="W")

submit_sides_amount_button = Button(Frame_for_actions, text="Submit", command=submit)
submit_sides_amount_button.grid(column=1, row=2)




#MAIN MENU
mainmenu = Menu(window)
window.config(menu=mainmenu)

mainmenu.add_command(label='About Program', command=aboutprog)
mainmenu.add_command(label='Author', command=aboutauthor)
mainmenu.add_command(label='Quit', command=quitprog)


#mainloop
window.mainloop()