import pyautogui as pygui
import time

choice = input('Enter name of your paint program')

pygui.press('win')
pygui.typewrite(choice)
pygui.press('enter')

paint_window = pygui.getWindow(choice)


def resize_brush(size):
    pygui.click(234, 101)
    pygui.typewrite(size)
    center_brush()
    return True


def center_brush():
    cen_x = (float(pygui.size()[0])) * .5
    cen_y = (float(pygui.size()[1])) * .5
    pygui.moveTo(cen_x, cen_y)


def create_new_project():
    pygui.hotkey('ctrl', 'n')
    # canvas width
    pygui.typewrite('600')
    pygui.press('tab')
    # canvas height
    pygui.typewrite('600')
    pygui.press('enter')
    return True


# waiting for window to open, in order to maximize
while not paint_window:
    paint_window = pygui.getWindow(choice)
    time.sleep(1)
else:
    pygui.getWindow(choice).maximize()

create_new_project()
