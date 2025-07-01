import keyboard as kb
from time import sleep
sleep(5)
spam = True
while spam:
    if kb.is_pressed('r'):
        spam = False
        break
    sleep(0.1)
    kb.write("как спам?")
    kb.press_and_release("enter")