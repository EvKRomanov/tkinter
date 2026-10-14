import tkinter as tk
import random

# Параметры окна
WIDTH = 800
HEIGHT = 600
NUM_DROPS = 120  # Количество капель

class RainDrop:
    def __init__(self, canvas):
        self.canvas = canvas
        self.reset(initial=True)

    def reset(self, initial=False):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT) if initial else random.randint(-50, -10)
        
        self.speed = random.randint(4, 12)
        self.length = self.speed * 2
        
        self.id = self.canvas.create_line(
            self.x, self.y, 
            self.x, self.y + self.length, 
            fill="#4a76a8", 
            width=1 if self.speed < 8 else 2
        )

    def update(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.canvas.delete(self.id)
            self.reset(initial=False)
        else:
            self.canvas.coords(self.id, self.x, self.y, self.x, self.y + self.length)

# Создание главного окна
root = tk.Tk()
root.title("Лабораторная работа: Симуляция дождя")
root.resizable(False, False)

# Создание холста (Canvas)
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#1a1c23")
canvas.pack()

# Создание капель
drops = [RainDrop(canvas) for _ in range(NUM_DROPS)]

def animate():
    for drop in drops:
        drop.update()
    root.after(16, animate)

# Старт цикла анимации и приложения
animate()
root.mainloop()