##########################################
#                                        #
#           85pt - Lab 11                # 
#                                        #
##########################################

# Make the ball bounce up and down instead of left and right

from Tkinter import *
root = Tk()
# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=0)

# Create the oval
circle = drawpad.create_oval(10, 10, 50, 50, fill='green')
direction = 1
# Create our animation function
def animate():
    global direction
    # Get the x and y co-ordinates of the circle
    x1, y1, x2, y2 = drawpad.coords(circle)
    # Change the x's to y's and width to height to make it bounce up and down
    if y2 > drawpad.winfo_height(): 
        direction = - 1
    elif y1 < 0:
        direction = 1
    # Move our oval object by the value of direction
    # Switch the 0 and direction to make it bounce up and down
    drawpad.move(circle, 0, direction)
    # Wait for 1 millisecond, then recursively call our animate function
    drawpad.after(1, animate)

# Kick off our animation
animate()
root.mainloop()
