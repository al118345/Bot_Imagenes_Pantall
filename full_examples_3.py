from python_imagesearch.imagesearch import *

# Search for the github logo on the whole screen
# note that the search only works on your primary screen.

# This is intended to be used as examples to be copy pasted, do not run the whole file at once

pos = imagesearch('Bitmaps/10_picas.png')
if pos[0] != -1:
    print("position : ", pos[0], pos[1])
    pyautogui.moveTo(pos[0], pos[1])
else:
    print("image not found")

# default imports
try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
import re


def replace_chars(text):
    """
    Replaces all characters instead of numbers from 'text'.

    :param text: Text string to be filtered
    :return: Resulting number
    """
    list_of_numbers = re.findall(r'\d+', text)
    result_number = ''.join(list_of_numbers)
    return result_number


ocr_result = pytesseract.image_to_string(Image.open('poker.png'), lang='eng')

print(replace_chars(ocr_result))