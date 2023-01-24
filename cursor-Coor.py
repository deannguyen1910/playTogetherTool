from os import system, name
import pynput
from pynput.mouse import Button, Controller
import time


def clear():
    if name == 'nt':
        _ = system('cls')

def main():
    while(1):
        mouse = Controller()
        current_mouse_position = mouse.position
        print(current_mouse_position)
        time.sleep(0.001)
        clear()
        #mouse.move(1560 - x, 348 - y)
        #mouse.press(Button.right)
        #mouse.release(Button.right)
        
        
if __name__ == "__main__":
    main()


    #from pynput.mouse import Button, Controller








#mouse = Controller()

# Read pointer position
#print('The current pointer position is {0}'.format(
 #   mouse.position))

# Set pointer position
#mouse.position = (10, 20)
#print('Now we have moved it to {0}'.format(
 #   mouse.position))

# Move pointer relative to current position
#mouse.move(5, -5)

# Press and release
#mouse.press(Button.left)
#mouse.release(Button.left)

# Double click; this is different from pressing and releasing
# twice on Mac OSX
#mouse.click(Button.left, 2)

# Scroll two steps down
#mouse.scroll(0, 2)