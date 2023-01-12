import tkinter as tk
import math

ORIENTATION  = -1
def calculate_position(data):

    center_x, center_y, radius, distance, angle, angle_speed, x, y = data

    #  зададим координаты
    x = center_x - distance * math.sin(math.radians(-angle))*ORIENTATION
    y = center_y - distance * math.cos(math.radians(-angle))*ORIENTATION

    #  сохраним положение, чтобы другой объект мог использовать его как центр вращения
    data[6] = x
    data[7] = y

    #  вычислим координаты овала
    x1 = x - radius
    y1 = y - radius
    x2 = x + radius
    y2 = y + radius

    return x1, y1, x2, y2

def create_object(data):

    x1, y1, x2, y2 = calculate_position(data)

    # создадим овал
    return c.create_oval(x1, y1, x2, y2 )

def move_object(object_id, data):

    x1, y1, x2, y2 = calculate_position(data)

    # движение овала
    c.coords(object_id, x1, y1, x2, y2)

def animate():
    #  движение земли: угол += угол_скорость
    earth[4] += earth[5]
    move_object(e_id, earth)


# запуск анимации сгова черех 100ms
    root.after(100, animate)

# --- main ---

# canvas size
WIDTH  = 600
HEIGHT = 600

# зададим центр солнечной системы
center_x = WIDTH//2
center_y = HEIGHT//2

# objects data
# [center of rotation x and y, radius, distance from center, current angle, angle speed, current positon x and y]
sun   = [center_x, center_y, 40, 0, 0, 0, 0, 0]
earth = [center_x, center_y, 10, 100, 0, 1, 0, 0]


# - init -
root = tk.Tk()
root.title("Solar System")

# - canvas -
c = tk.Canvas(root, width=WIDTH, heigh=HEIGHT)
c.pack()

#  создание земли и солнышка ( радиус и окружность)
s_id = create_object(sun)
e_id = create_object(earth)


#  запуск анимации
animate()

#  запуск программы
root.mainloop()
