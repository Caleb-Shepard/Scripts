from pynput.mouse import Button, Controller
import time

mouse = Controller()

while True:
    mouse.press(Button.right)
    time.sleep(10)
    mouse.release(Button.right)
    mouse.press(Button.left)
    mouse.release(Button.left)
