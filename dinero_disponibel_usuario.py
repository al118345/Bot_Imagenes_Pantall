


from PIL import Image
im = Image.open("poker.png")

crop_rectangle = (1413,1325,1635,1383)
cropped_im = im.crop(crop_rectangle)

cropped_im.show()
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


ocr_result = pytesseract.image_to_string(cropped_im, lang='eng')

print(replace_chars(ocr_result))


