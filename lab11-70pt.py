##########################################
#                                        #
#           70pt - Lab 11                # 
#                                        #
##########################################

# Make the ball twice as large
# Make the ball move 5 times faster

from Tkinter import *
root = Tk()
# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=0)

# Create the oval
#circle = drawpad.create_oval(10, 10, 50, 50, fill='green')
# Circle that is two times larger by changing 50 to 100
circle = drawpad.create_oval(10, 10, 100, 100, fill='green')
direction = 1
# Create our animation function
def animate():
    global direction
    # Get the x and y co-ordinates of the circle
    x1, y1, x2, y2 = drawpad.coords(circle)
    #if x2 > drawpad.winfo_width(): 
        #direction = - 1
    #elif x1 < 0:
        #direction = 1
        
    # Circle that moves five times faster by changing -1 and 1 to -5 and 5
    if x2 > drawpad.winfo_width(): 
        direction = - 5
    elif x1 < 0:
        direction = 5
    #Move our oval object by the value of direction
    drawpad.move(circle,direction,0)
    # Wait for 1 millisecond, then recursively call our animate function
    drawpad.after(1, animate)

# Kick off our animation
animate()
root.mainloop()
