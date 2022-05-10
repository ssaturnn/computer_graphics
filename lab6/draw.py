import time
from tkinter import messagebox
from PIL import ImageColor

from geometry import Point

WINDOW_WIDTH = 1300
WINDOW_HEIGHT = 710

CANVAS_WIDTH = 900
CANVAS_HEIGHT = 780

DELAY_TIME = 0.02

EDGE_COLOR = "#1c0202"
BG_COLOR = "#ffffff"


def highlight_pixel(img, x, y, color):
    img.put(color, (x, y))


def highlight_str(img, color, start_x, end_x, start_y, end_y):
    img.put(color, (start_x, start_y, end_x, end_y))


def draw_line(img, points):
    for cur_point in points:
        highlight_pixel(img, cur_point[0], cur_point[1], cur_point[2])


def fill_figure(canvas, img, polygons, polygon_color, mode_var, time_label, color_btn, seed_pixel):
    if seed_pixel.getCoords() == (-1, -1):
        messagebox.showwarning("Ошибка",
                               "Отсутствует затравка")
        return

    color_btn.config(state="disabled")

    delay = mode_var.get()

    start_time = time.time()
    method_with_seed_m(canvas, img, polygon_color, delay, seed_pixel)
    end_time = time.time()

    time_str = str(round(end_time - start_time, 2)) + "s"
    time_label.config(text=time_str)

    color_btn.config(state="normal")


def method_with_seed(canvas, img, fill_color, delay, seed_pixel):
    edge_color_rgb = ImageColor.getcolor(EDGE_COLOR, "RGB")
    fill_color_rgb = ImageColor.getcolor(fill_color, "RGB")

    stack = list()

    # Занести затравочный пиксель в стек
    stack.append(seed_pixel)

    # Пока стек не пуст
    while len(stack):
        # Извлечь затравочный пиксель из стека
        seed_pixel = stack.pop()
        x = seed_pixel.x
        y = seed_pixel.y

        highlight_pixel(img, x, y, fill_color)
        x -= 1

        # Закрасить пиксели текущей строки слева от затравочного
        while img.get(x, y) != edge_color_rgb and img.get(x, y) != fill_color_rgb:
            highlight_pixel(img, x, y, fill_color)
            x -= 1

        # Запомнить координату самого левого закрашенного пикселя
        x_left = x + 1

        # Закрасить пиксели текущей строки справа от затравочного
        x = seed_pixel.x + 1
        while img.get(x, y) != edge_color_rgb and img.get(x, y) != fill_color_rgb:
            highlight_pixel(img, x, y, fill_color)
            x += 1

        # Запомнить координату самого правого закрашенного пикселя
        x_right = x - 1

        # Поиск новых затравочных пикселей на строках сверху и снизу
        # Проход по верхней строке

        x = x_left
        y += 1

        while x <= x_right:
            # Флаг нахождения затравки
            flag = False

            # x <= x_right для области шириной 1 пиксель (когда x_left = x_right)
            while img.get(x, y) != edge_color_rgb and img.get(x, y) != fill_color_rgb and x <= x_right:
                flag = True
                x += 1

            # Поместить в стек крайний справа пиксель
            if flag:
                if x == x_right and img.get(x, y) != edge_color_rgb and img.get(x, y) != fill_color_rgb:
                    stack.append(Point(x, y))
                else:
                    stack.append(Point(x - 1, y))

            # Продолжить проверку, если интервал был прерван
            x_start = x
            while (img.get(x, y) == edge_color_rgb or img.get(x, y) == fill_color_rgb) and x < x_right:
                x += 1

            if x == x_start:
                x += 1

        # Проход по нижней строке

        x = x_left
        y -= 2

        while x <= x_right:
            # Флаг нахождения затравки
            flag = False

            # x <= x_right для области шириной 1 пиксель (когда x_left = x_right)
            while img.get(x, y) != edge_color_rgb and img.get(x, y) != fill_color_rgb and x <= x_right:
                flag = True
                x += 1

            # Поместить в стек крайний справа пиксель
            if flag:
                if x == x_right and img.get(x, y) != edge_color_rgb and img.get(x, y) != fill_color_rgb:
                    stack.append(Point(x, y))
                else:
                    stack.append(Point(x - 1, y))

            # Продолжить проверку, если интервал был прерван
            x_start = x
            while (img.get(x, y) == edge_color_rgb or img.get(x, y) == fill_color_rgb) and x < x_right:
                x += 1

            if x == x_start:
                x += 1

        if delay:
            canvas.update()
            time.sleep(0.01)






















def method_with_seed_m(canvas, img, fill_color, delay, seed_pixel):
    edge_color_rgb = ImageColor.getcolor(EDGE_COLOR, "RGB")
    fill_color_rgb = ImageColor.getcolor(fill_color, "RGB")

    stack = list()

    # Занести затравочный пиксель в стек
    stack.append(seed_pixel)

    # Пока стек не пуст
    while len(stack):
        # Извлечь затравочный пиксель из стека
        seed_pixel = stack.pop()
        x = seed_pixel.x
        y = seed_pixel.y

        highlight_pixel(img, x, y, fill_color)
        x -= 1

        # Закрасить пиксели текущей строки слева от затравочного
        while img.get(x, y) != edge_color_rgb and img.get(x, y) != fill_color_rgb:
            #highlight_pixel(img, x, y, fill_color)
            x -= 1

        # Запомнить координату самого левого закрашенного пикселя
        x_left = x + 1
        img.put(fill_color, (x_left, y, seed_pixel.x + 1, y + 1))

        # Закрасить пиксели текущей строки справа от затравочного
        x = seed_pixel.x + 1
        while img.get(x, y) != edge_color_rgb and img.get(x, y) != fill_color_rgb:
            #highlight_pixel(img, x, y, fill_color)
            x += 1

        # Запомнить координату самого правого закрашенного пикселя
        x_right = x - 1
        img.put(fill_color, (seed_pixel.x + 1, y, x_right + 1, y + 1))

        # Поиск новых затравочных пикселей на строках сверху и снизу
        # Проход по верхней строке

        x = x_left
        y += 1

        while x <= x_right:
            # Флаг нахождения затравки
            flag = False

            # x <= x_right для области шириной 1 пиксель (когда x_left = x_right)
            while img.get(x, y) != edge_color_rgb and img.get(x, y) != fill_color_rgb and x <= x_right:
                flag = True
                x += 1

            # Поместить в стек крайний справа пиксель
            if flag:
                if x == x_right and img.get(x, y) != edge_color_rgb and img.get(x, y) != fill_color_rgb:
                    stack.append(Point(x, y))
                else:
                    stack.append(Point(x - 1, y))

            # Продолжить проверку, если интервал был прерван
            x_start = x
            while (img.get(x, y) == edge_color_rgb or img.get(x, y) == fill_color_rgb) and x < x_right:
                x += 1

            if x == x_start:
                x += 1

        # Проход по нижней строке

        x = x_left
        y -= 2

        while x <= x_right:
            # Флаг нахождения затравки
            flag = False

            # x <= x_right для области шириной 1 пиксель (когда x_left = x_right)
            while img.get(x, y) != edge_color_rgb and img.get(x, y) != fill_color_rgb and x <= x_right:
                flag = True
                x += 1

            # Поместить в стек крайний справа пиксель
            if flag:
                if x == x_right and img.get(x, y) != edge_color_rgb and img.get(x, y) != fill_color_rgb:
                    stack.append(Point(x, y))
                else:
                    stack.append(Point(x - 1, y))

            # Продолжить проверку, если интервал был прерван
            x_start = x
            while (img.get(x, y) == edge_color_rgb or img.get(x, y) == fill_color_rgb) and x < x_right:
                x += 1

            if x == x_start:
                x += 1

        if delay:
            canvas.update()
            time.sleep(0.01)

