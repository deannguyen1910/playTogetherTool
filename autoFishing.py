from re import T
from typing import Tuple
import pyautogui
from PIL import Image
import pynput
from pynput.mouse import Button, Controller
import time
import random
import array

def randomBetween(a, b):
    temp_a = a*100
    temp_b = b*100
    if (temp_b < temp_a):
        temp = temp_a
        temp_a = temp_b
        temp_b = temp
    n = random.randrange(temp_b - temp_a)
    n += temp_a
    return n /100

def _fishingFrame(left_crop, top_crop, right_crop, bottom_crop, color_a, color_b, pic): #a(left; top) b(right; bottom)
    pic.crop((left_crop, top_crop, right_crop, bottom_crop))
    
    #pic = Image.open(r'C:\Users\dean\Desktop\Test\tesstpic.png').crop((left_crop, top_crop, right_crop, bottom_crop))
    #pic.save(r'C:\Users\dean\Desktop\Test\PicCheck.png')
    pic = pic.convert('RGB')
    width, height = pic.size

    for i in range (height):
        for j in range (width):
            r, g, b = pic.getpixel((j, i))
            if  (r >= color_a) and (g >= color_a) and (b >= color_a) and (r <=color_b) and (g <= color_b) and (b <= color_b): return True

    return False

def _fishingSign(pic_com, pixel_x, pixel_y, r1, g1, b1): 
    pic = pic_com
    pic = pic.convert('RGB')

    r, g, b = pic.getpixel((pixel_x, pixel_y))    
    
    if (abs(r - r1) >= 1) or (abs(g - g1) >= 1) or (abs(b - b1) >= 1):
        return True

    return False

def _fishingSignAdvanced(pic_old, p1_x, p1_y, p2_x, p2_y):
    pic = pic_old
    pic = pic.convert('RGB')
    
    r1, g1, b1 = pic.getpixel((p1_x, p1_y))
    r2, g2, b2 = pic.getpixel((p2_x, p2_y))
    
    if (abs(r1 - r2) <= 5) and (abs(g1 - g2) <= 5) and (abs(b1 -b2) <= 5):
        return False

    return True

def _brokenSign(pic_com, pixel_x, pixel_y, r1, g1, b1): 
    pic = pic_com
    pic = pic.convert('RGB')

    r, g, b = pic.getpixel((pixel_x, pixel_y))    
    
    count = 0
    if (abs(r - r1) <= 5) and (abs(g - g1) <= 5) and (abs(b - b1) <= 5):
        return True
    
    return False

class autoclick:
    def click_Fishing(x, y):
        mouse = Controller()
        current_x, current_y = mouse.position
        mouse.move(x - current_x, y - current_y)
        mouse.click(Button.left)

    def click_closeResult(x, y):
        mouse = Controller()
        current_x, current_y = mouse.position
        mouse.move(x - current_x, y - current_y)
        time.sleep(0.2)
        mouse.click(Button.left)

    def reFishing(x, y):
        mouse = Controller()
        current_x, current_y = mouse.position
        mouse.move(x - current_x, y - current_y)
        time.sleep(1)
        mouse.press(Button.left)
        time.sleep(randomBetween(0.5, 1.2))
        mouse.release(Button.left)

    def fix_Rob(bag_x, bag_y, rob_x, rob_y, repair_x, repair_y, confirm_x, confirm_y):
        
        mouse = Controller()
        current_x, current_y = mouse.position
        mouse.move(bag_x - current_x, bag_y - current_y)
        time.sleep(1)
        mouse.click(Button.left)
        time.sleep(1.1)
        
        current_x, current_y = mouse.position
        mouse.move(rob_x - current_x, rob_y - current_y)
        time.sleep(1)
        mouse.click(Button.left)
        time.sleep(1.1)

        pic = pyautogui.screenshot()
        #while (_fishingFrame(repair_x, repair_y, repair_x + 1, repair_y + 1, 100, 100, pic) == True): # COLOR OF REPARING # Confirm it's broken
        while (_fishingSignAdvanced(pic, 1629, 537, 1591, 409) == True):
            current_x, current_y = mouse.position
            mouse.move(repair_x - current_x, repair_y - current_y)
            time.sleep(1)
            mouse.click(Button.left)
            time.sleep(1.1)

            current_x, current_y = mouse.position
            mouse.move(confirm_x - current_x, confirm_y - current_y)
            time.sleep(1)
            mouse.click(Button.left)
            time.sleep(3)
            mouse.click(Button.left)
            time.sleep(1.1)

        current_x, current_y = mouse.position
        mouse.move(1799 - current_x, 109 - current_y)
        time.sleep(1)
        mouse.click(Button.left)
        time.sleep(1.1)

        return True

class GUI:
    def get():
        print(1)

def _autoFishing():
    #Getting the info
    #fishing_Sign_left = 921, fishing_Sign_top = 298, fishing_Sign_right = 943, fishing_Sign_bottom = 360 
    #fishing_left = 1647, fishing_top = 775, fishing_right = 1780, fishing_bottom = 882
    #refishing_left = 1540, refishing_top = 621, refishing_right = 1614, refishing_bottom = 686

    confirmVal = False
    #pic = []
    #pic.append(pyautogui.screenshot())
    #pic.append(pyautogui.screenshot())
    #pic[0] = pyautogui.screenshot()

    time.sleep(3)
    pic = pyautogui.screenshot()
    pic1 = pic.convert('RGB')
    r, g, b = pic1.getpixel((566, 427))

    while (1):
        time.sleep(0.05) #according to fps

        pic = pyautogui.screenshot()

        #if (_fishingSign(pic, 566, 427, r, g, b) == True): 

        if(_fishingSignAdvanced(pic, 469, 302, 540, 267) == True) :
            autoclick.click_Fishing(randomBetween(1539, 1725), randomBetween(759, 942))
            time.sleep(randomBetween(3.33, 5.33))   
            
            pic = pyautogui.screenshot()
            while (_fishingFrame(1708, 302, 1751, 349, 253, 255, pic) == False):
               time.sleep(1)
               pic = pyautogui.screenshot()
            
            
            if (_fishingFrame(1708, 302, 1751, 349, 253, 255, pic) == True):
                autoclick.click_closeResult(1454, 901) ## close the resultp
            time.sleep(0.3)
            #pic = pyautogui.screenshot()

            time.sleep(randomBetween(0.82, 1.00))
            
            autoclick.reFishing(randomBetween(1433, 1539),randomBetween(617, 719))
            #1164 279
            time.sleep(1)
            pic = pyautogui.screenshot()
            if (1):
            #if(_brokenSign(pic, 942, 548, 253, 253, 253) == True): # Refishing spot
            #if (_fishingSignAdvanced(pic, 1164, 279, 1050, 800 == True)):
                print ("Fixing rob")
                autoclick.fix_Rob(1781, 587, 1346, 109, 1707, 527, 946, 815)
                time.sleep(1.7)
            else: 
                print ("nononono")
                
            time.sleep(3)

def main():
    _autoFishing()
    print ("done")

if __name__ == "__main__":
    main()