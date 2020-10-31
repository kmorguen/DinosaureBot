from PIL import ImageGrab
import pyautogui


class Cordinates():
    replayBtn = ()


def restarGame():
    pyautogui.click(Cordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp('space')

xs
restarGame()
time.sleep(1)
pressSpace()

