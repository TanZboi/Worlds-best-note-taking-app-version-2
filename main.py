from tkinter import *
from tkinter.colorchooser import askcolor

import customtkinter
import customtkinter as ct



class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'
    STARTING_BGCOLOUR = 'white'

    def __init__(self):

        self.root = customtkinter.CTk()

        self.file_button = customtkinter.CTkButton(self.root, text='New Page', command=self.file)
        self.file_button.grid(row=0, column=0)

        self.pen_button = customtkinter.CTkButton(self.root, text='Pen', command=self.use_pen)
        self.pen_button.grid(row=0, column=1)

        self.brush_button = customtkinter.CTkButton(self.root, text='Dark Mode', command=self.set_dark)
        self.brush_button.grid(row=0, column=2)

        self.brush_button = customtkinter.CTkButton(self.root, text='Light Mode', command=self.set_light)
        self.brush_button.grid(row=1, column=2)

        self.color_button = customtkinter.CTkButton(self.root, text='Color', command=self.choose_color)
        self.color_button.grid(row=0, column=3)

        self.eraser_button = customtkinter.CTkButton(self.root, text='Eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=4)

        self.clear_button = customtkinter.CTkButton(self.root, text='Clear', command=self.clear_canvas)
        self.clear_button.grid(row=0, column=5)

        self.choose_size_button = customtkinter.CTkSlider(self.root, from_=1, to=30)
        self.choose_size_button.grid(row=0, column=6)

        self.c = Canvas(self.root, bg='white', width=1280, height=720)
        self.c.grid(row=2, columnspan=7)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.bgcolour = self.STARTING_BGCOLOUR
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.color = 'black'

    def set_dark(self):
        self.c.configure(bg='black')
        self.color = 'white'
        #redraw all lines in white
        for item in self.c.find_all():
            self.c.itemconfig(item, fill='white')

    def set_light(self):
        self.c.configure(bg='white')
        self.color = 'black'
        for item in self.c.find_all():
            self.c.itemconfig(item, fill='black')

    def file(self):
        if __name__ == '__main__':
            Paint()

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.color = 'white'

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.configure(relief=RAISED)
        some_button.configure(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y
        print(self.old_x, self.old_y)

    def clear_canvas(self):
        self.c.delete(ALL)

    def reset(self, event):
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Paint()