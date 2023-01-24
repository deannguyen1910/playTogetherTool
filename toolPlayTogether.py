import os
from tkinter.constants import W
import pyautogui
import tkinter
from PIL import Image
import time
import struct


#def _getCropPos():
    #print()

#class randomPos:
    #def Circle(radius, center):


def _FishingFrame(left, top, right, bottom):
    pic = pyautogui.screenshot().crop((left, top, right, bottom))
    #pic = Image.open(r'C:\Users\dean\Desktop\Test\pic.png') 
    pic.save(r'C:\Users\dean\Desktop\Test\Full.png')
    #pic = pic.crop((left, top, right, bottom))
    pic.save(r'C:\Users\dean\Desktop\Test\Crop.png')

    #color = pic.getpixel(100, 100) ## ADJUST THE COORDINATE OF THE IMAGE
    #print(color)
    #if (color != (253,255,253)): ## get the color 
    #    
    #    return 0
    #else: return 1

def toolFishing():
    #UI ---- Getting right box
    print("place the box on the", '"', '!', '"') 
    box = tkinter.Tk()
    button = tkinter.Button(box, text='Confirm', width=20, command=box.destroy)
    button.pack()
    box.mainloop()

    # get mouse and Pos info

    while 1:
        time.sleep(0.05)
        if (_FishingFrame == 1):
            #cursor
            print("got the fish \n" )
            #got the fish
            break
    


def main():
    _FishingFrame(0,0, 100, 100)
    #toolFishing()
    #print ("hello word")

if __name__ == "__main__":
    main()

