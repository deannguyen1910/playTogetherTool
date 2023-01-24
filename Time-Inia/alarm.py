from os import system, name
import time
import winsound
import datetime


def timeFunc():
    local_time = time.ctime(time.time())
    clear()
    print("The local time is:", local_time)

def clear():
    if name == 'nt':
        _ = system('cls')

    return

def alarmIf():
    now = datetime.datetime.now()
    if (now.second >= 10): return
    
    #For Inia
    if (now.minute == 13): 
        winsound.Beep(528, 1000)
        print("\nTime for Inia")
    elif (now.minute == 43): winsound.Beep(528,1000)
    elif (now.minute == 18):
        winsound.Beep(528,1000)
        print("\nTime for Inia")
    elif (now.minute == 48): winsound.Beep(528,1000)

    #For Whale (later update)
    if (now.minute == 54):
        winsound.Beep(528, 1000)
        print("\nTime for Whale")
    elif (now.minute == 6): winsound.Beep(528, 1000)
    elif (now.minute == 24): 
        winsound.Beep(528, 1000)
        print("\nTime for Whale")
    elif (now.minute == 36): winsound.Beep(528, 1000)
    


def displayTime():
    while (1):
        time.sleep(1)
        timeFunc()
        alarmIf()


def main():
    displayTime()
    
if __name__ == "__main__":
    main()