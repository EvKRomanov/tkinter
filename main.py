import tkinter as tk

# Константы окна
WIDTH = 800
HEIGHT = 600

# Создание главного окна
root = tk.Tk()
root.title("Лабораторная работа: Симуляция дождя")
root.resizable(False, False)

# Создание холста Canvas
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#1a1c23")
canvas.pack()

root.mainloop()