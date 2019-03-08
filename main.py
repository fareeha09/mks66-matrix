from display import *
from draw import *
from matrix import *
import random

screen = new_screen()
color = [ 23, 255, 200 ]

matrix = new_matrix()
i = 0
while (i < 30):
	x1 = random.randint(1,500)
	y1 = 500
	add_edge(matrix, 0, 0, 0, x1, y1, 0)
	add_edge(matrix, x1, y1, 0, 500, 0, 0)
	x1 = random.randint(1,500)
	y1 = 0
	add_edge(matrix, 0, 500, 0, x1, y1, 0)
	add_edge(matrix, x1, y1, 0, 500, 500, 0)
	
	i+=1

draw_lines( matrix, screen, color )
display(screen)
save_extension(screen, 'img.png')
