import copy
import math
from tkinter import Tk, Button, Label, Entry, END, Canvas, messagebox, Menu, GROOVE, FIRST, LAST, CENTER, LEFT, E, N, S, \
    SW, NE, SE, NW, W

from matplotlib.sankey import UP, RIGHT

WIDTH = 1000
HEIGHT = 600
RADIUS = 3

EPS = 1e-9

TASK = "Реализовать масштабирование, перенос, поворот на примере котика."


def init_cat_pic(cat_pic):
    # Голова
    pre = poly_oval(200, 120, 400, 280, 100, 0)
    cat_pic.append(pre)

    # Глаза
    pre = poly_oval(235, 155, 295, 215, 100, 0)
    cat_pic.append(pre)
    pre = poly_oval(305, 155, 365, 215, 100, 0)
    cat_pic.append(pre)

    # Зрачки
    pre = poly_oval(270, 180, 280, 190, 100, 0)
    cat_pic.append(pre)
    pre = poly_oval(330, 180, 320, 190, 100, 0)
    cat_pic.append(pre)

    # Типа рот
    pre = poly_oval(260, 200, 300, 240, 100, 0, math.pi, math.pi * 2)
    cat_pic.append(pre)
    pre = poly_oval(300, 200, 340, 240, 100, 0, math.pi, math.pi * 2)
    cat_pic.append(pre)

    # Уши
    pre = [220, 155, 230, 75, 280, 125]
    cat_pic.append(pre)
    pre = [320, 125, 370, 75, 380, 155]
    cat_pic.append(pre)

    # нос
    pre = [290, 210, 300, 220, 310, 210, 290, 210]
    cat_pic.append(pre)

    # Подпородок
    pre = poly_oval(290, 240, 310, 250, 100, 0, math.pi, math.pi * 2)
    cat_pic.append(pre)

    # Усы лево
    pre = [280, 220, 170, 230]
    cat_pic.append(pre)
    pre = [275, 225, 180, 250]
    cat_pic.append(pre)
    pre = [280, 230, 190, 270]
    cat_pic.append(pre)

    # Усы право
    pre = [320, 220, 430, 230]
    cat_pic.append(pre)
    pre = [325, 225, 420, 250]
    cat_pic.append(pre)
    pre = [320, 230, 410, 270]
    cat_pic.append(pre)

    # Волосы
    pre = [285, 125, 295, 100]
    cat_pic.append(pre)
    pre = [295, 127, 305, 100]
    cat_pic.append(pre)
    pre = [305, 129, 315, 100]
    cat_pic.append(pre)

    # Тело (L)
    pre = poly_oval(220, 150, 600, 600, 100, 0, math.pi * 1.17, math.pi * 1.4)
    cat_pic.append(pre)

    # Тело (R)
    pre = poly_oval(0, 150, 380, 600, 100, 0, math.pi * 1.83, math.pi * 1.6)
    cat_pic.append(pre)

    # Низ тела (L)
    pre = [220, 415, 250, 415]
    cat_pic.append(pre)

    # Низ тела (R)
    pre = [350, 415, 380, 415]
    cat_pic.append(pre)

    # Нога (L)
    pre = poly_oval(250, 390, 300, 440, 100, 0, math.pi, math.pi * 2)
    cat_pic.append(pre)

    # Нога (R)
    pre = poly_oval(300, 390, 350, 440, 100, 0, math.pi, math.pi * 2)
    cat_pic.append(pre)

    # Нога бочина (L)
    pre = [250, 415, 250, 340]
    cat_pic.append(pre)

    # Нога бочина (R)
    pre = [350, 415, 350, 340]
    cat_pic.append(pre)

    # Нога Центр
    pre = [300, 415, 300, 330]
    cat_pic.append(pre)

    # Грудак
    pre = poly_oval(270, 300, 330, 330, 100, 0, math.pi, math.pi * 2)
    cat_pic.append(pre)

    # Хвост (Основа круг)
    pre = poly_oval(340, 375, 430, 455, 100, 0, math.pi / 3, math.pi / 2 * 2.45)
    cat_pic.append(pre)

    # Хвост (палка верх)
    pre = [380, 415, 310, 460]
    cat_pic.append(pre)

    # Хвост (палка низ)
    pre = [410, 450, 330, 480]
    cat_pic.append(pre)

    # Хвост (конец круг)
    pre = poly_oval(300, 457, 340, 500, 100, 0, math.pi / 2, -math.pi / 2)
    cat_pic.append(pre)

    # Хвост (палка конец)
    pre = [320, 500, 330, 480]
    cat_pic.append(pre)


def draw_cat(canvas, cat_pic, is_scale=False):
    tmp = copy.deepcopy(cat_pic)
    x0 = 0
    xn = canvas.winfo_width()
    y0 = 0
    yn = canvas.winfo_height()

    if is_scale:
        tmp, x0, y0, xn, yn = copy.deepcopy(find_resize_koef(tmp))


    main_canvas.delete("all")
    draw_axis(canvas, x0, xn, y0, yn)
    for item in tmp:
        draw_arc(canvas, item, 'red')


def poly_oval(x0, y0, x1, y1, steps=60, rotation=0, start=0, end=math.pi * 2 + 0.2):
    rotation = rotation * math.pi / 180.0
    a = (x1 - x0) / 2.0
    b = (y1 - y0) / 2.0
    xc = x0 + a
    yc = y0 + b
    point_list = []
    # create the oval as a list of points
    for i in range(steps):
        # Calculate the angle for this step
        # 360 degrees == 2 pi radians
        theta = start + (start - end) * (float(i) / steps)
        x1 = a * math.cos(theta)
        y1 = b * math.sin(theta)
        # rotate x, y
        x = (x1 * math.cos(rotation)) + (y1 * math.sin(rotation))
        y = (y1 * math.cos(rotation)) - (x1 * math.sin(rotation))

        point_list.append(round(x + xc))
        point_list.append(round(y + yc))
    return point_list


def draw_arc(canvas, arr, color='white'):
    i = 0
    while i < (len(arr) - 3):
        canvas.create_line(arr[i], arr[i + 1], arr[i + 2], arr[i + 3], fill=color)
        i += 2

def num_count(num):
    count = 0
    while num != 0:
        num = num // 10
        count += 1
    return count


def draw_axis(canvas, x0=0, xn=600, y0=0, yn=600):
    hei = canvas.winfo_height()
    wid = canvas.winfo_width()

    canvas.create_line(20, 0, 20, hei, fill='white', arrow=LAST)  # Axis Y
    canvas.create_line(0, 20, wid, 20, fill='white', arrow=LAST)  # Axis X

    print(num_count(xn))

    canvas.create_text(24, 10, text='{}'.format(y0), fill='white', anchor=W)
    canvas.create_text(10, 20, text='{}'.format(x0), fill='white', anchor=NW)
    canvas.create_text(24, hei - 15, text='{}'.format(yn), fill='white', anchor=SW)
    canvas.create_text(wid - 4 * num_count(xn), 24, text='{}'.format(xn), fill='white', anchor=N)


def move(tur, dx, dy):
    try:
        dx = float(dx)
        dy = float(dy)
        last_activity.append(copy.deepcopy(tur))
        for i in range(len(tur)):
            j = 0
            while j < len(tur[i]):
                tur[i][j] += dx
                tur[i][j + 1] += dy
                j += 2

        draw_cat(main_canvas, tur)
    except:
        messagebox.showerror("Ошибка", "Неверно введены данные")


def spin(tur, angle, x_c, y_c):
    try:
        angle = float(angle)
        x_c = float(x_c)
        y_c = float(y_c)
        last_activity.append(copy.deepcopy(tur))

        angle = (angle * math.pi) / 180

        for i in range(len(tur)):
            j = 0
            while j < len(tur[i]):
                tur[i][j] -= x_c
                tur[i][j + 1] -= y_c

                tur[i][j], tur[i][j + 1] = tur[i][j] * math.cos(angle) - tur[i][j + 1] * math.sin(angle), \
                                           tur[i][j] * math.sin(angle) + tur[i][j + 1] * math.cos(angle)

                tur[i][j] += x_c
                tur[i][j + 1] += y_c
                j += 2

        draw_cat(main_canvas, tur)
    except:
        messagebox.showerror("Ошибка", "Неверно введены данные")


def scale(tur, kx, ky, x_c, y_c):
    try:
        print("cat")
        print(cat_pic)
        kx = float(kx)
        ky = float(ky)
        x_c = float(x_c)
        y_c = float(y_c)
        last_activity.append(copy.deepcopy(tur))

        for i in range(len(tur)):
            j = 0
            while j < len(tur[i]):
                tur[i][j] = kx * (tur[i][j] - x_c) + x_c
                tur[i][j + 1] = ky * (tur[i][j + 1] - y_c) + y_c
                j += 2

        draw_cat(main_canvas, tur)
    except:
        messagebox.showerror("Ошибка", "Неверно введены данные")


def exit_prog():
    root.destroy()


def go_to_start():
    last_activity.append(copy.deepcopy(cat_pic))
    cat_pic.clear()
    init_cat_pic(cat_pic)
    draw_cat(main_canvas, cat_pic)


def find_resize_koef(cat_pic):
    x_min = cat_pic[0][0]
    y_min = cat_pic[0][1]
    x_max = cat_pic[0][0]
    y_max = cat_pic[0][1]

    for i in range(len(cat_pic)):
        j = 0
        while j < len(cat_pic[i]):
            if cat_pic[i][j] < x_min:
                x_min = cat_pic[i][j]
            if cat_pic[i][j + 1] < y_min:
                y_min = cat_pic[i][j + 1]
            if cat_pic[i][j] > x_max:
                x_max = cat_pic[i][j]
            if cat_pic[i][j + 1] > y_max:
                y_max = cat_pic[i][j + 1]
            j += 2

    tmp_dots = copy.deepcopy(cat_pic)

    dx = x_max - x_min
    dy = y_max - y_min



    for i in range(len(tmp_dots)):
        j = 0
        while j < len(tmp_dots[i]):
            tmp_dots[i][j] = tmp_dots[i][j] - x_min
            tmp_dots[i][j + 1] = tmp_dots[i][j + 1] - y_min
            j += 2

    min_win = min(main_canvas.winfo_width(), main_canvas.winfo_height())

    k_x = (min_win * 0.8) / dx
    k_y = (min_win * 0.8) / dy

    min_k = min(k_x, k_y)

    for i in range(len(tmp_dots)):
        j = 0
        while j < len(tmp_dots[i]):
            tmp_dots[i][j] = tmp_dots[i][j] * min_k + 0.1 * min_win
            tmp_dots[i][j + 1] = tmp_dots[i][j + 1] * min_k + 0.1 * min_win
            j += 2
    print(x_min)
    print(x_max)
    print(y_min)
    print(y_max)
    return tmp_dots, x_min, y_min, x_max, y_max


def previous_state(event):
    print("last:")
    print(last_activity)
    global cat_pic
    cat_pic.clear()
    if len(last_activity) > 1:
        cat_pic = copy.deepcopy(last_activity[-1])
        last_activity.pop()
    if len(last_activity) == 1:
        cat_pic = copy.deepcopy(last_activity[-1])
    draw_cat(main_canvas, cat_pic)

def config(event):
    if event.widget == root:
        draw_cat(main_canvas, cat_pic)



cat_pic = []
last_activity = []

if __name__ == "__main__":
    init_cat_pic(cat_pic)
    last_activity.append(copy.deepcopy(cat_pic))

    root = Tk()
    root.geometry("%dx%d" % (WIDTH, HEIGHT))
    root.title("Лабораторная работа №2")
    root.minsize(WIDTH, HEIGHT)

    main_canvas = Canvas(root, bg="black")
    main_canvas.place(relx=0.4, rely=0, relwidth=0.6, relheight=1)


    menu_label = Label(text="Меню", bg='red')
    menu_label.place(relx=0, rely=0, relwidth=0.4, relheight=0.05)

    menu_label_center = Label(text="Центр масштабирования и поворота", bg='grey')
    menu_label_center.place(relx=0, rely=0.05, relwidth=0.4, relheight=0.05)

    label_center_x = Label(text="X:", bg='grey')
    label_center_x.place(relx=0, rely=0.1, relwidth=0.05, relheight=0.05)

    center_x = Entry(root, width=14)
    center_x.delete(0, END)
    center_x.insert(END, 300)
    center_x.place(relx=0.05, rely=0.1, relwidth=0.15, relheight=0.05)

    label_center_y = Label(text="Y:", bg='grey')
    label_center_y.place(relx=0.2, rely=0.1, relwidth=0.05, relheight=0.05)

    center_y = Entry(root, width=14)
    center_y.delete(0, END)
    center_y.insert(END, 300)
    center_y.place(relx=0.25, rely=0.1, relwidth=0.15, relheight=0.05)

    label_border = Label(bg='red')
    label_border.place(relx=0, rely=0.15, relwidth=0.4, relheight=0.05)

    menu_label_move = Label(text="Перемещение", bg='#d0d0d0')
    menu_label_move.place(relx=0, rely=0.2, relwidth=0.4, relheight=0.05)

    label_move_x = Label(text="dX:", bg='#d0d0d0')
    label_move_x.place(relx=0, rely=0.25, relwidth=0.05, relheight=0.05)

    move_x = Entry(root, width=14)
    move_x.delete(0, END)
    move_x.insert(END, 0)
    move_x.place(relx=0.05, rely=0.25, relwidth=0.15, relheight=0.05)

    label_move_y = Label(text="dY:", bg='#d0d0d0')
    label_move_y.place(relx=0.2, rely=0.25, relwidth=0.05, relheight=0.05)

    move_y = Entry(root, width=14)
    move_y.delete(0, END)
    move_y.insert(END, 0)
    move_y.place(relx=0.25, rely=0.25, relwidth=0.15, relheight=0.05)

    move_btn = Button(text="Переместить", width=9, height=2, bg='#d0d0d0', relief=GROOVE,
                      command=lambda: move(cat_pic, move_x.get(), move_y.get()))
    move_btn.place(relx=0.0, rely=0.3, relwidth=0.4, relheight=0.1)

    menu_label_scale = Label(text="Масштабирование", bg='grey')
    menu_label_scale.place(relx=0, rely=0.4, relwidth=0.4, relheight=0.05)

    label_scale_x = Label(text="kX:", bg='grey')
    label_scale_x.place(relx=0, rely=0.45, relwidth=0.05, relheight=0.05)

    scale_x = Entry(root, width=14)
    scale_x.delete(0, END)
    scale_x.insert(END, 1)
    scale_x.place(relx=0.05, rely=0.45, relwidth=0.15, relheight=0.05)

    label_scale_y = Label(text="kY:", bg='grey')
    label_scale_y.place(relx=0.2, rely=0.45, relwidth=0.05, relheight=0.05)

    scale_y = Entry(root, width=14)
    scale_y.delete(0, END)
    scale_y.insert(END, 1)
    scale_y.place(relx=0.25, rely=0.45, relwidth=0.15, relheight=0.05)

    scale_btn = Button(text="Масштабировать", width=9, height=2, bg='grey', relief=GROOVE,
                       command=lambda: scale(cat_pic, scale_x.get(), scale_y.get(), center_x.get(), center_y.get()))
    scale_btn.place(relx=0.0, rely=0.5, relwidth=0.4, relheight=0.1)

    menu_label_spin = Label(text="Поворот", bg='#d0d0d0')
    menu_label_spin.place(relx=0, rely=0.6, relwidth=0.4, relheight=0.05)

    label_spin_x = Label(text="Угол(градусы):", bg='#d0d0d0')
    label_spin_x.place(relx=0, rely=0.65, relwidth=0.2, relheight=0.05)

    spin_ang = Entry(root, width=14)
    spin_ang.delete(0, END)
    spin_ang.insert(END, 0)
    spin_ang.place(relx=0.2, rely=0.65, relwidth=0.2, relheight=0.05)

    spin_btn = Button(text="Повернуть", width=9, height=2, bg='#d0d0d0', relief=GROOVE,
                      command=lambda: spin(cat_pic, spin_ang.get(), center_x.get(), center_y.get()))
    spin_btn.place(relx=0.0, rely=0.7, relwidth=0.4, relheight=0.1)

    label_border = Label(bg='red')
    label_border.place(relx=0, rely=0.8, relwidth=0.4, relheight=0.05)

    solve_btn = Button(text="Сброс", width=23, height=2,
                       command=go_to_start)
    solve_btn.place(relx=0, rely=0.85, relwidth=0.4, relheight=0.15)

    main_menu = Menu(root)
    root.config(menu=main_menu)
    main_menu.add_command(label="О программе", command=lambda: messagebox.showinfo("О программе", TASK))
    main_menu.add_command(label="Об авторе", command=lambda: messagebox.showinfo("Об авторе", "Шаронов А. ИУ7-44Б"))
    main_menu.add_command(label="Масштабировать", command=lambda: draw_cat(main_canvas, cat_pic, True))
    main_menu.add_command(label="Выход", command=exit_prog)

    root.bind("<Control-z>", lambda e: previous_state(e))
    root.bind("<Configure>", config)

    draw_cat(main_canvas, cat_pic)
    root.mainloop()
