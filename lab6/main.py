from tkinter import Tk, Radiobutton, Canvas, Label, Entry, Button, \
    PhotoImage, DISABLED, BooleanVar, Listbox, END
from draw import WINDOW_HEIGHT, WINDOW_WIDTH, CANVAS_WIDTH, CANVAS_HEIGHT
from tkinter import colorchooser, messagebox

from draw import highlight_pixel, draw_line, fill_figure, BG_COLOR, EDGE_COLOR
from geometry import *
from bresenham import bresenham_int

MAIN_BG = "#79edde"
HEADERS_BG = "#998369"
BUTTON_BG = "#ffffff"
FONT_HEADERS = 'Helvetica 13'
FONT_TEXT = 'Helvetica 13'


class RootWindow:

    def __init__(self):
        self.window = Tk()
        self.window.title("ЛР6 - Алгоритмы заполнения с затравкой (Турчанинов Александр ИУ7-44Б)")
        self.window.geometry("%dx%d+0+0" % (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.window.resizable(False, False)
        self.window["bg"] = MAIN_BG

        """
            Canvas
        """
        self.canvas = Canvas(self.window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.place(x=0, y=0)

        self.p_min = [CANVAS_WIDTH, CANVAS_HEIGHT]
        self.p_max = [0, 0]

        self.img = PhotoImage(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.create_image(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, image=self.img, state="normal")

        """
            Algorithm name
        """
        Label(text="Построчный алгоритм заполнения с затравкой",
              font=FONT_HEADERS+' bold', fg="black", bg=MAIN_BG, anchor="center"). \
            place(width=398, x=CANVAS_WIDTH + 2, y=15)

        """
            Colorchooser
        """
        self.color = "#dfb771"

        Label(text="Закраска:", font=FONT_TEXT, bg=MAIN_BG).place(x=CANVAS_WIDTH + 10, y=60)

        Button(self.window, state=DISABLED).place(width=50, height=50, x=CANVAS_WIDTH + 340, y=60)

        self.color_btn = Button(self.window, bg=self.color, command=self.choose_color)
        self.color_btn.place(width=42, height=42, x=CANVAS_WIDTH + 344, y=64)

        """
            Delay
        """
        self.mode_var = BooleanVar()
        self.mode_var.set(0)

        Radiobutton(text="Без задержки", variable=self.mode_var, value=0,
                    font=FONT_TEXT, bg=MAIN_BG, anchor="w"). \
            place(width=140, x=CANVAS_WIDTH + 180, y=60)

        Radiobutton(text="С задержкой", variable=self.mode_var, value=1,
                    font=FONT_TEXT, bg=MAIN_BG, anchor="w"). \
            place(width=140, x=CANVAS_WIDTH + 180, y=85)

        """
            Add point
        """
        Label(text="Добавление точки", font=FONT_TEXT, bg=MAIN_BG). \
            place(x=CANVAS_WIDTH + 10, y=140)

        self.point_var = BooleanVar()
        self.point_var.set(0)

        Radiobutton(text="Точка фигуры", variable=self.point_var, value=0,
                    font=FONT_TEXT, bg=MAIN_BG, anchor="w"). \
            place(width=140, x=CANVAS_WIDTH + 10, y=185)

        Radiobutton(text="Затравка", variable=self.point_var, value=1,
                    font=FONT_TEXT, bg=MAIN_BG, anchor="w"). \
            place(width=140, x=CANVAS_WIDTH + 10, y=210)

        Label(text="X:", font=FONT_TEXT, bg=MAIN_BG).place(x=CANVAS_WIDTH + 230, y=140)
        Label(text="Y:", font=FONT_TEXT, bg=MAIN_BG).place(x=CANVAS_WIDTH + 230, y=168)

        self.x_entry = Entry(font=FONT_TEXT)
        self.x_entry.place(width=125, height=22, x=CANVAS_WIDTH + 265, y=140)

        self.y_entry = Entry(font=FONT_TEXT)
        self.y_entry.place(width=125, height=22, x=CANVAS_WIDTH + 265, y=168)

        Button(text="Добавить точку", font=FONT_TEXT, bg=HEADERS_BG, fg="white",
               command=self.input_point). \
            place(width=160, height=30, x=CANVAS_WIDTH + 230, y=210)

        """
            Points list
        """
        Label(text="Список точек", font=FONT_TEXT, bg=MAIN_BG). \
            place(width=380, x=CANVAS_WIDTH + 10, y=270)

        self.points_listbox = Listbox(font=FONT_TEXT)
        self.points_listbox.place(width=380, height=200, x=CANVAS_WIDTH + 10, y=300)

        """
            Mouse instructions
        """
        Label(bg=HEADERS_BG).place(width=380, height=100, x=CANVAS_WIDTH + 10, y=515)

        Label(text="Построение с помощью мыши", font=FONT_TEXT, bg=MAIN_BG). \
            place(width=376, x=CANVAS_WIDTH + 12, y=517)

        Label(text="Левая кнопка - добавить точку", font=FONT_TEXT, bg=MAIN_BG, anchor='w'). \
            place(width=376, x=CANVAS_WIDTH + 12, y=547)
        Label(text="Правая кнопка - замкнуть фигуру", font=FONT_TEXT, bg=MAIN_BG, anchor='w'). \
            place(width=376, x=CANVAS_WIDTH + 12, y=567)
        Label(text="Средняя кнопка - добавить затравку", font=FONT_TEXT, bg=MAIN_BG, anchor='w'). \
            place(width=376, x=CANVAS_WIDTH + 12, y=587)

        """
            Time
        """
        Label(text="Время закраски:", font=FONT_HEADERS, bg=MAIN_BG). \
            place(x=CANVAS_WIDTH + 10, y=630)

        self.time_label = Label(font=FONT_HEADERS, bg=MAIN_BG)
        self.time_label.place(x=CANVAS_WIDTH + 170, y=630)

        """
            Fill
        """
        Button(text="Закрасить изображенную фигуру", font=FONT_TEXT, bg=HEADERS_BG, fg="white",
               command=lambda: fill_figure(self.canvas, self.img, self.polygons, self.color, self.mode_var,
                                           self.time_label, self.color_btn, self.seed_pixel)). \
            place(width=380, height=40, x=CANVAS_WIDTH + 10, y=660)

        """
            Clear screen
        """
        Button(text="Очистить экран", font=FONT_TEXT, bg=HEADERS_BG, fg="white", command=self.clear_canvas). \
            place(width=380, height=40, x=CANVAS_WIDTH + 10, y=720)

        self.polygons = [Polygon()]
        self.seed_pixel = Point(-1, -1)

        self.canvas.bind('<1>', self.left_click)
        self.canvas.bind('<2>', self.center_click)
        self.canvas.bind('<3>', self.right_click)
        self.canvas.bind('<B1-Motion>', self.left_click)

    def choose_color(self):
        color = colorchooser.askcolor()
        self.color = color[1]
        self.color_btn.config(bg=self.color)

    def clear_canvas(self):
        self.canvas.delete("all")
        self.points_listbox.delete(0, END)
        self.polygons = [Polygon()]
        self.time_label.config(text="")

        self.img = PhotoImage(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.create_image(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, image=self.img, state="normal")

    def left_click(self, event):
        point = Point(event.x, event.y)
        cur_polygon = self.polygons[-1]
        cur_polygon.addPoint(point)

        highlight_pixel(self.img, point.x, point.y, EDGE_COLOR)

        if cur_polygon.points_num >= 2:
            cur_polygon.addEdge(-2, -1)
            points = bresenham_int(cur_polygon.points[-2].getCoords(),
                                   cur_polygon.points[-1].getCoords(),
                                   EDGE_COLOR)
            draw_line(self.img, points)

        self.points_listbox.insert(END, "%d - (%d, %d)" % (cur_polygon.points_num, point.x, point.y))

    def right_click(self, event):
        cur_polygon = self.polygons[-1]
        if len(self.polygons) > 1 and cur_polygon.points_num == 0:
            messagebox.showwarning("Ошибка", "Незамкнутых фигур нет")
            return

        cur_polygon.addEdge(0, -1)

        self.polygons.append(Polygon())

        points = bresenham_int(cur_polygon.points[0].getCoords(),
                               cur_polygon.points[-1].getCoords(),
                               EDGE_COLOR)
        draw_line(self.img, points)

        self.points_listbox.insert(END, "-------------------------------")

    def center_click(self, event):
        point = Point(event.x, event.y)
        self.seed_pixel = point

        highlight_pixel(self.img, point.x, point.y, self.color)

        self.points_listbox.insert(END, "seed pixel = (%d, %d)" % (point.x, point.y))

    def input_point(self):
        try:
            x = int(self.x_entry.get())
            y = int(self.y_entry.get())
        except:
            messagebox.showwarning("Ошибка",
                                   "Координаты точки должны быть целыми числами")
            return

        point = Point(x, y)

        if self.point_var.get() == 1:
            self.seed_pixel = point

            highlight_pixel(self.img, point.x, point.y, self.color)

            self.points_listbox.insert(END, "seed pixel = (%d, %d)" % (point.x, point.y))
        else:
            cur_polygon = self.polygons[-1]
            cur_polygon.addPoint(point)

            highlight_pixel(self.img, point.x, point.y, EDGE_COLOR)

            if cur_polygon.points_num >= 2:
                cur_polygon.addEdge(-2, -1)
                points = bresenham_int(cur_polygon.points[-2].getCoords(),
                                       cur_polygon.points[-1].getCoords(),
                                       EDGE_COLOR)
                draw_line(self.img, points)

            self.points_listbox.insert(END, "%d - (%d, %d)" % (cur_polygon.points_num, point.x, point.y))


if __name__ == "__main__":
    root = RootWindow()
    root.window.mainloop()
