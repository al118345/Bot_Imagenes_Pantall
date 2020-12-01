from screen_search import *

search = Search("tor/problema.png")
pos = search.imagesearch()
if pos[0] != -1:
    print('esta')
else:
    print('no')
    search = Search("tor/no_gracias_"
                    "2.png")
    pos = search.imagesearch()
    if pos[0] != -1:
        pyautogui.moveTo(pos[0], pos[1])
        time.sleep(1)
        pyautogui.click()
        pyautogui.press('enter', interval=0.25)
        time.sleep(5)
        print('esta')
    else:
        print("image not found")

    search = Search("tor/acepto.png")
    pos = search.imagesearch()
    if pos[0] != -1:
        pyautogui.moveTo(pos[0], pos[1])
        time.sleep(1)
        pyautogui.click()
        pyautogui.press('enter', interval=0.25)
        time.sleep(5)
    else:
        print("image not found")
