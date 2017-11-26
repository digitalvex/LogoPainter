import pyautogui as pygui
import time

choice = input('Enter name of your paint program')

pygui.press('win')
pygui.typewrite(choice)
pygui.press('enter')

paint_window = pygui.getWindow(choice)


def select_tool(toolname):
    if toolname == 'brush':
        pygui.press('b')
    elif toolname == 'bucket':
        pygui.press('f')
    elif toolname == 'eraser':
        pygui.press('e')


def fill_square(x=0, y=0):
    pygui.moveRel(x, y)
    pygui.press('f')
    pygui.click()


def create_square(size, x=0, y=0):
    pygui.dragRel(size + x, 0, duration=.05)
    pygui.dragRel(0, size + y, duration=.05)
    pygui.dragRel(-size - x, 0, duration=.05)
    pygui.dragRel(0, -size - y, duration=.05)


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
center_brush()

s = -1
for i in range(4):
    s *= -1
    create_square(50 * s)
    time.sleep(1.25)

# fills in squares diagonal from each other
fill_square(15, 15)
fill_square(-30, -30)

select_tool('brush')
center_brush()
create_square(50, 50, 50)
