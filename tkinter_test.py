import tkinter as tk

board_size_px = 500
grid_size = 7
board_border_px = 10
num_attackers = 12
num_defenders = 8

root = tk
frame = root.Canvas(bg='black', height=510, width=510)

frame.create_line(10, 10, 500, 10, 500, 500, 10, 500, 10, 10, fill='white',width=1)

for n in range(1, grid_size): # vertical lines
    frame.create_line(10+70*n, 10, 10+70*n, 500, fill='sea green', width=1)

for n in range(1, grid_size): # horizontal
    frame.create_line(10, 10+70*n, 500, 10+70*n, fill='blue', width=1)

# place king in center (make triangle)
frame.create_line(510/2, 510/2-35+5, 510/2-35+5, 510/2+35-5, 510/2+35-5, 510/2+35-5, 510/2, 510/2-35+5, fill='red', width=1)

# place defenders

#frame.create_oval(510/2-30, 510/2-30, 510/2+30, 510/2+30, fill='red', width=1)

for n in range(3, 6): # horizontal
    frame.create_oval(70/2*n-30+10, 70/2*n-30+10, 70/2*n+30+10, 70/2*n+30+10, fill='pink', width=1)

# x0 = x - r
#     y0 = y - r
#     x1 = x + r
#     y1 = y + r
#     return canvasName.create_oval(x0, y0, x1, y1)

frame.pack()
root.mainloop()

# frame.create_line(5, 5, 5+square_size, 5, 5+square_size, 5+square_size, 5, 5+square_size, 5, 5, fill='white',width=1)
# frame.create_line(5, 5, 5+square_size*n, 5, 5+square_size*n, 5+square_size*n, 5, 5+square_size*n, 5, 5, fill='sea green',width=1)
#Canvas.create_line(x1, y1, x2, y2, ...., options = ...)
#frame.create_line(5, 5, 5+square_size, 5+square_size, fill='white',width=1)
#frame.create_rectangle(10, 10, 200, 360, fill='sea green')
#frame.create_line(370, 40, 460, 40, 460, 130, 370, 130, 370, 40, fill='white', width=1)
#Canvas.create_line(x1, y1, x2, y2, ...., options = ...)
#frame.create_line(100,200,100,200,fill='white',width=200)