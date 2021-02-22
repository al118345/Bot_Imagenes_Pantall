from screen_search import *



def salt_final():
    crop_rectangle = (1000, 800, 1635, 1000)
    cropped_im = ImageGrab.grab(crop_rectangle)

    # cropped_im.show()
    # default imports
    try:
        from PIL import Image
    except ImportError:
        import Image

    import pytesseract

    ocr_result = pytesseract.image_to_string(cropped_im, lang='spa')
    return '1938' in ocr_result

def bloqueo():
    search = Search("tor/error_5.png")
    pos = search.imagesearch()
    if pos[0] != -1:
        return False
    if '¿Por qué ha sucedido esto?' in texto():
        print('texto encontrado')
        return False
    if 'No se puede acceder a este sitio web' in texto2():
        print('texto encontrado')
        return False
    print(texto3())
    if 'ESTO ES UNA' in texto3():
        print('texto encontrado')
        return False
    return True

def bloqueo1():
    search = Search("tor/error_captcha.png")
    pos = search.imagesearch()
    if pos[0] != -1:
        return False
    return True

from PIL import ImageGrab

def texto():
    crop_rectangle = (1000, 150, 1635, 275)
    cropped_im = ImageGrab.grab(crop_rectangle)

    #cropped_im.show()
    # default imports
    try:
        from PIL import Image
    except ImportError:
        import Image

    import pytesseract


    ocr_result = pytesseract.image_to_string(cropped_im, lang='spa')
    return ocr_result


def texto2():
    crop_rectangle = (1000, 150, 1635, 500)
    cropped_im = ImageGrab.grab(crop_rectangle)

    #cropped_im.show()
    # default imports
    try:
        from PIL import Image
    except ImportError:
        import Image

    import pytesseract


    ocr_result = pytesseract.image_to_string(cropped_im, lang='spa')
    return ocr_result

def texto3():
    crop_rectangle = (1000, 150, 1635, 700)
    cropped_im = ImageGrab.grab(crop_rectangle)

    #cropped_im.show()
    # default imports
    try:
        from PIL import Image
    except ImportError:
        import Image

    import pytesseract


    ocr_result = pytesseract.image_to_string(cropped_im, lang='spa')
    return ocr_result
def intento():
    search = Search("tor_windows/cerrar-brave.PNG")
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
    search = Search("tor_windows/menu-brave.PNG")




    pos = search.imagesearch()

    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.moveTo(pos[0], pos[1])
    else:
        print("image not found")

    pyautogui.click()


    search = Search("tor_windows/tor-brave.PNG")


    pos = search.imagesearch()
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.moveTo(pos[0], pos[1])
    else:
        print("image not found")


    pyautogui.click()
    #pyautogui.hotkey('alt', 'shift', 'n')
    pyautogui.hotkey('alt', 'shift', 'n')


    '''
    search = Search("tor/test_buscar2.png")
    pos = search.imagesearch()
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
        pyautogui.moveTo(pos[0], pos[1])
    else:
        print("image not found")
    '''
    lista = [
        'https://www.youtube.com/watch?v=4t23hglhHO8&t',

        'https://www.youtube.com/watch?v=BFRGyju1uLo',
        'https://www.youtube.com/watch?v=JOFR6ChA2Ho&t',
             'https://www.youtube.com/watch?v=V00UF8PQcMA&t',
             'https://www.youtube.com/watch?v=vCFioQizM4w&t',
             'https://www.youtube.com/watch?v=QKFBKafxeco&t',
             'https://www.youtube.com/watch?v=VsA5vxfda8I&t',
             'https://www.youtube.com/watch?v=uwiHVmB3qw8&t',
             'https://www.youtube.com/watch?v=KN2PmVz0xmw&t',
             'https://www.youtube.com/watch?v=Urx62V0OFAk&t',
             'https://www.youtube.com/watch?v=f4Erw0p0G8U',
             'https://www.youtube.com/watch?v=G45ehCje3HU',
             'https://www.youtube.com/watch?v=2wQpZbbI6Vk',
             'https://www.youtube.com/watch?v=DMKTzmOBTmE',
             'https://www.youtube.com/watch?v=tbEzovevM44',
             'https://www.youtube.com/watch?v=U7HeCvS3U8I',
             'https://www.youtube.com/watch?v=GxnWNRi3K9g&t=1s',
             'https://www.youtube.com/watch?v=J8PDfVY2FfI&t',
             'https://www.youtube.com/watch?v=SJ2KtPdaGWY&t',
             'https://www.youtube.com/watch?v=CUsklt966rA'
             ]


    import random
    print(len(lista))
    lista[0]

    for i in list(lista[random.randint(0,len(lista)-1)]):
        if i in '/':
            print('entre')
            pyautogui.hotkey('shift', '/')
        else:
            if i in '=':
                print('entre')
                pyautogui.hotkey('shift', '=')
            else:
                pyautogui.write(i, interval=0.01)
        print(i)
    pyautogui.press('enter',interval=0.01)

def no_gracias():
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
                print('acepto')
                pyautogui.moveTo(pos[0], pos[1])
                time.sleep(1)
                pyautogui.click()
                pyautogui.press('space', interval=0.01)

'''
crop_rectangle = (1000, 800, 1635, 1000)
cropped_im = ImageGrab.grab(crop_rectangle)

#cropped_im.show()
# default imports
try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract

ocr_result = pytesseract.image_to_string(cropped_im, lang='spa')
print( ocr_result)

'''


intento()
while True:
    import random
    segundos = random.randint(425,590)
    time.sleep(3)
    search = Search("tor/entiendo2.png")
    pos = search.imagesearch()
    if pos[0] != -1:

        pyautogui.moveTo(pos[0], pos[1])
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        '''
        search = Search("tor/play.png")
        pos = search.imagesearch()
        if pos[0] != -1:
            pyautogui.moveTo(pos[0], pos[1])
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)
            time.sleep(10000)
        '''
        search = Search("tor/play_2.png")
        pos = search.imagesearch()
        if pos[0] != -1 and pos[0] != 1352:
            print('zona1')
            pyautogui.moveTo(pos[0], pos[1])
            time.sleep(1)
            pyautogui.press('space', interval=0.01)
            time.sleep(1)
            print('duermo')
            time.sleep(segundos)
            intento()


    search = Search("tor/error_captcha.png")
    pos = search.imagesearch()
    if pos[0] != -1:
        intento()

    search = Search("tor/error_5.png")
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
                print('acepto')
                pyautogui.moveTo(pos[0], pos[1])
                time.sleep(1)
                pyautogui.click()
                pyautogui.press('space', interval=0.01)
                time.sleep(5)
                print('duermo')
                time.sleep(segundos)
                intento()
            else:
                print('nadie')
                time.sleep(5)
                no_gracias()
                if not bloqueo():
                    intento()
                    continue
                if not bloqueo1():
                    intento()
                    continue
                pyautogui.press('space', interval=0.01)
                print('duermo')
                time.sleep(20)
                no_gracias()
                if not bloqueo():
                    intento()
                    continue
                if not bloqueo1():
                    intento()
                    continue
                search = Search("tor/play_2.png")
                pos = search.imagesearch()
                print(pos[0])
                if pos[0] != -1 and pos[0] ==1045:
                    print('entre en play')
                    pyautogui.moveTo(pos[0], pos[1])
                    time.sleep(1)
                    pyautogui.press('space', interval=0.01)
                time.sleep(20)
                no_gracias()
                if not bloqueo():
                    intento()
                    continue
                if not bloqueo1():
                    intento()
                    continue
                search = Search("tor/play_2.png")
                pos = search.imagesearch()
                print(pos[0])
                if pos[0] != -1 and pos[0] ==1045:
                    print('entre en play2')
                    pyautogui.moveTo(pos[0], pos[1])
                    time.sleep(1)
                    pyautogui.press('space', interval=0.01)
                if not salt_final():
                    print('Nada cargado')
                    intento()
                    continue
                time.sleep(segundos-20)
                intento()
                print("image not found")
