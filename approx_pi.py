import random
import tkinter as tk
import tk_tools

root = tk.Tk()
canvas = tk.Canvas(root, bg="black", height=600, width=600)
canvas.pack()
canvas.create_oval(0,0,600,600, outline = 'white')

"""
Количество проверок можно поставить больше, тогда и на канвасе будет больше цветных точек и
получившееся число больше приближенно к Пи, но займёт больше времени
"""
n = 10000 #количество проверок
i = 0 #количество выполненных проерок
count = 0 #количество точек, попавших в круг
def dote():
    global n, i, count
    if i < n:
        # Произвольно генерировать координаты x, y
        x = random.random()
        y = random.random()
        #Проверка на вхождение точки в круг
        if (pow((0.5 - x),2) + pow((0.5 - y),2)) <= pow(0.5, 2):
            #Ставится зеленая точка
            canvas.create_line(x*600, y*600, x*600+1, y*600, fill = 'green')
            count += 1
        else:
            #Ставится синяя точка, если точка не входит в круг
            canvas.create_line(x*600, y*600, x*600+1, y*600, fill = 'blue')
        i += 1
        root.after(1, dote)
    else:
        #Получившееся значение числа, приближенному к Пи
        print( 4 * (count / n))
        
root.after(0, dote)
root.mainloop()

