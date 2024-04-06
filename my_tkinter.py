from tkinter import Tk, Label, Button, Entry

from geometry_calculator import ShapeCalculator as sc


def circle_clicked():
    def calculate_and_print():
        try:
            result = sc.calculate_circle_area(radius.get())
            lbl_res.config(
                text=f"площадь круга равна {result}",
                font=("Arial Bold", 20),
                fg="black"
            )

        except ValueError as e:
            lbl_res.config(
                text=f"Ошибка: {e}",
                font=("Arial Bold", 16),
                fg="red"
            )

    circle_window = Tk()
    circle_window.geometry("600x300")
    circle_window.title("площадь круга")

    lbl = Label(circle_window, text="введите радиус", font=("Arial Bold", 20))
    lbl.grid(column=0, row=0)

    lbl_res = Label(circle_window, text="")
    lbl_res.grid(column=0, row=3, columnspan=6)

    radius = Entry(circle_window, width=10)
    radius.grid(column=1, row=0)

    btn_calculate_circle = Button(
        circle_window, text="посчитать", command=calculate_and_print
    )
    btn_calculate_circle.grid(column=1, row=1)

    circle_window.mainloop()


def triangle_clicked():
    def calculate_and_print():
        sides = " ".join([side_a.get(), side_b.get(), side_c.get()])
        result = sc.calculate_triangle_area(sides)
        lbl_res.config(
            text=f"площадь треугольника равна {result}",
            font=("Arial Bold", 20),
            fg="black"
        )

        is_right_triangle = sc.is_right_triangle(sides)
        lbl_res_is_right_triangle.config(
            triangle_window,
            text=f"прямоугольный: {is_right_triangle}",
            font=("Arial Bold", 20),
            fg="black"
        )

    triangle_window = Tk()
    triangle_window.geometry("600x300")
    triangle_window.title("площадь треугольника")

    lbl_a = Label(
        triangle_window,
        text="введите сторону A",
        font=("Arial Bold", 20)
    )
    lbl_a.grid(column=0, row=0)
    side_a = Entry(triangle_window, width=10)
    side_a.grid(column=1, row=0)

    lbl_b = Label(
        triangle_window,
        text="введите сторону B",
        font=("Arial Bold", 20)
    )
    lbl_b.grid(column=0, row=1)
    side_b = Entry(triangle_window, width=10)
    side_b.grid(column=1, row=1)

    lbl_c = Label(
        triangle_window,
        text="введите сторону C",
        font=("Arial Bold", 20)
    )
    lbl_c.grid(column=0, row=2)
    side_c = Entry(triangle_window, width=10)
    side_c.grid(column=1, row=2)

    lbl_res = Label(triangle_window, text="")
    lbl_res.grid(column=0, row=4, columnspan=6)

    lbl_res_is_right_triangle = Label(triangle_window, text="")
    lbl_res_is_right_triangle.grid(column=0, row=5, columnspan=6)

    btn_calculate_triangle = Button(
        triangle_window, text="посчитать", command=calculate_and_print
    )
    btn_calculate_triangle.grid(column=1, row=3)

    triangle_window.mainloop()


window = Tk()
window.geometry("600x300")
window.title("площадь фигур")
lbl = Label(window, text="выберете фигуру", font=("Arial Bold", 20))
lbl.grid(column=0, row=0, columnspan=4)
btn_circle = Button(window, text="круг", command=circle_clicked)
btn_circle.grid(column=0, row=2)
btn_triangle = Button(window, text="треугольник", command=triangle_clicked)
btn_triangle.grid(column=1, row=2)
window.mainloop()
