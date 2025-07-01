import keyboard as kb
from time import sleep
sleep(3)
while True:
    sleep(0.1)
    kb.write("привет")
    kb.press_and_release("enter")