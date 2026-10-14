import tkinter as tk
import random

# Константы окна
WIDTH = 800
HEIGHT = 600

class RainDrop:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.speed = 5
        self.length = 10
        self.id = self.canvas.create_line(self.x, self.y, self.x, self.y + self.length, fill="#4a76a8")

    def update(self):
        self.y += self.speed
        self.canvas.coords(self.id, self.x, self.y, self.x, self.y + self.length)

# Создание главного окна
root = tk.Tk()
root.title("Лабораторная работа: Симуляция дождя")
root.resizable(False, False)

# Создание холста Canvas
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#1a1c23")
canvas.pack()

root.mainloop()