from screen_search import *


def intento():
    search = Search("tor/cerrar_brave.png")
    pos = search.imagesearch()
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.moveTo(pos[0], pos[1])
    else:
        print("image not found")
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)




    # Search for the github logo on the whole screen
    # note that the search only works on your primary screen.
    search = Search("tor/menu_brave2.png")




    pos = search.imagesearch()

    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.moveTo(pos[0], pos[1])
    else:
        print("image not found")

    pyautogui.click()


    search = Search("tor/tor_menu.png")


    pos = search.imagesearch()
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.moveTo(pos[0], pos[1])
    else:
        print("image not found")


    pyautogui.click()
    #pyautogui.hotkey('alt', 'shift', 'n')
    pyautogui.hotkey('alt', 'shift', 'n')



    search = Search("tor/test_buscar2.png")
    pos = search.imagesearch()
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.moveTo(pos[0], pos[1])
    else:
        print("image not found")



    for i in list('https://www.youtube.com/watch?v=KN2PmVz0xmw&list=UUJXa8TUeY_1nSqsIFyrnU-g'):
        if i in '/':
            print('entre')
            pyautogui.hotkey('shift', '/')
        else:
            if i in '=':
                print('entre')
                pyautogui.hotkey('shift', '=')
            else:
                pyautogui.write(i, interval=0.05)
        print(i)
    pyautogui.press('enter',interval=0.25)

intento()
while True:
    time.sleep(3)
    search = Search("tor/entiendo.png")
    pos = search.imagesearch()
    if pos[0] != -1:
        pyautogui.moveTo(pos[0], pos[1])
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        search = Search("tor/play.png")
        pos = search.imagesearch()
        if pos[0] != -1:
            pyautogui.moveTo(pos[0], pos[1])
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)
            time.sleep(10000)



    search = Search("tor/problema.png")
    pos = search.imagesearch()
    if pos[0] != -1:
         intento()
    else:
        search = Search("tor/error2.png")
        pos = search.imagesearch()
        if pos[0] != -1:
            intento()
        else:
            time.sleep(5)
            search = Search("tor/no_gracias_2.png")
            pos = search.imagesearch()
            if pos[0] != -1:
                pyautogui.moveTo(pos[0], pos[1])
                time.sleep(1)
                pyautogui.click()
                pyautogui.press('enter', interval=0.1)
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
                time.sleep(10000)
            else:
                print("image not found")
