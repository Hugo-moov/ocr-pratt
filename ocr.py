from PIL import Image
import pytesseract
import pandas as pd
import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
import json

load_dotenv()
api_key = os.getenv("AZURE_OPENAI_KEY")

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
    # print(f'Boxes output:\n\n{boxes_output}')

    # Get result as dictionary
    dict_output = pytesseract.image_to_data(img_0, output_type=pytesseract.Output.DICT)
    df_output = pd.DataFrame(dict_output)
    # print(f'Dict output:\n\n{df_output}')

    # Get result as XML
    xml_output = pytesseract.image_to_alto_xml(img_0)
    # print(f'XML output:\n\n{df_output}')

    # LLM post processing
    endpoint = os.getenv("AZURE_ENDPOINT")
    key = os.getenv("AZURE_KEY")
    model_name = os.getenv("AZURE_MODEL_NAME")
    deployment = os.getenv("AZURE_MODEL_NAME")

    subscription_key = os.getenv("AZURE_KEY")
    api_version = os.getenv("AZURE_API_VERSION")

    client = AzureOpenAI(
        api_version=api_version,
        azure_endpoint=endpoint,
        api_key=subscription_key,
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant to structure data coming from an OCR process.",
            },
            {
                "role": "user",
                "content": f"What is the total amount for this transaction ? Output the result in the format of a valid python dictionary with fields invoice_number, total_amount: {string_output}",
            }
        ],
        max_completion_tokens=13107,
        temperature=0.1,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        model=deployment
    )

    result = response.choices[0].message.content
    print(result)

    # Output validation

    class InvoiceResult(BaseModel):
        invoice_number: str
        total_amount: float

    validated = InvoiceResult(**json.loads(result))
    print(validated)











