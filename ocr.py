from PIL import Image
import pytesseract
import pandas as pd
import os

if __name__ == "__main__":

    # Path to tesseract.exe on Windows
    TESSERACT_EXE = r"C:\Users\hugboron\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

    if os.path.exists(TESSERACT_EXE):
        pytesseract.pytesseract.tesseract_cmd = TESSERACT_EXE

    img_0 = Image.open('data/img_0.jpg')
    img_0.show()

    # List of available languages
    print(pytesseract.get_languages(config=''))

    # Get result as string
    string_output = pytesseract.image_to_string(img_0)
    print(f'String output:\n\n{string_output}')

    # Get result as boxes
    boxes_output = pytesseract.image_to_boxes(img_0)
    print(f'Boxes output:\n\n{boxes_output}')

    # Get result as dictionary
    dict_output = pytesseract.image_to_data(img_0, output_type=pytesseract.Output.DICT)
    df_output = pd.DataFrame(dict_output)
    print(f'Dict output:\n\n{df_output}')

    # Get result as XML
    xml_output = pytesseract.image_to_alto_xml(img_0)
    print(f'XML output:\n\n{df_output}')










