# Set window to be 300 by 200 with the point (0, 0) as the 
 # lower left corner and (300, 200) as the upper right corner. 
import turtle as t
t.setup(300, 200) 
t.screensize(300, 200) 
t.setworldcoordinates(0, 0, 300, 200)
# Draw two vertical lines to divide the window into thirds. 
t.penup() 
t.setpos(100, 0) # First line.
t.pendown() 
t.setpos(100, 200) 
t.penup() 
t.setpos(200, 0) # Second line.
t.pendown() 
t.setpos(200, 200)








 