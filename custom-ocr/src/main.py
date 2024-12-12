import argparse
import os
import time
import logging
# from enum import StrEnum
# import os
# import tkinter as tk

# import gpyocr
import pyperclip
import numpy as np
import cv2

from dotenv import load_dotenv
from PIL import ImageGrab, Image

# MAKE SURE THE DOT ENV PATH IS CORRECT!!!
# more like make sure this python script is run in the dir it is placed in
# so that relative pathing can find everything correctly
# if want to change this to full path need to change the ocr.env to full path as well
load_dotenv("ocr.env")

# TEMP_FILE = "file/img.jpg"

def save_text(fpath: str, text: str, mode: str = "a"):
    with open(fpath, "a", encoding="utf-8") as file:
        file.write(text)
        file.write("\n")

def open_image(fpath: str) -> Image:
    return Image.open(fpath)

def get_img_clipboard():
    try:
        img = ImageGrab.grabclipboard()
    except Exception as e:
        if "failed to open clipboard" in str(e):
            # This gets raised when there is no change in the clipboard content
            return None
    if not img:
        return None
        # raise Exception("No image in clipboard detected!")
    # img.convert('RGB').save(TEMP_FILE)
    return img

def detect_text(img):
    """
    Detects text in the file.
    
    Modified from:
    https://cloud.google.com/vision/docs/ocr#vision_text_detection_gcs-python
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    # Pass in PIL.image
    if isinstance(img, Image.Image):
        # Encode the image to base64
        if not img.mode.startswith("RGB"):
            img = img.convert("RGB")
        img = np.array(img)
        img = cv2.imencode(".jpg", img)[1].tobytes()
    image = vision.Image(content=img)

    # Image to Text
    response = client.text_detection(image=image)
    # Extract Response
    texts = response.text_annotations

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    elif len(texts) < 1:
        return "Empty"
    return texts[0].description

def ocr(img, engine="gcp"):
    output = None
    if engine == "gcp":
        output = detect_text(img)
    else:
        print("Engine Not Supported")
    return output

def poll():
    image = None
    while True:
        try:
            new_image = get_img_clipboard()
            if not new_image:
                continue
            if image != new_image:
                image = new_image
            text = ocr(image, engine="gcp")
            pyperclip.copy(text)

            logging.info(text)
            print(text)
            print()
        except Exception as e:
            # logging.exception("Exception")
            print("Exception: ", e)
            pass
        time.sleep(1)


def main(input, output):
    # Input validation
    print(os.getcwd())
    if input == "clipboard" or output == "clipboard":
        print(f"Input method clipboard not implemented")
        return
    if not os.path.exists(input):
        print(f"Input file does not exist: {input}")
        return

    # img file -> text file
    image = open_image(input)
    if image is None:
        print("None for {input}")
        return
    text = ocr(image, engine="gcp")
    save_text(output, text)

def test():
    # Get Image From Clipboard
    print(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))
    print(os.environ.get("TESSDATA_PREFIX"))
    image = get_img_clipboard()
    if image is None:
        print("None")
        return
    # Image-Text
    text = ocr(image, engine="gcp")
    # Ouptut Text to Clipboard
    pyperclip.copy(text)
    print(text)
    return text

if __name__ == "__main__":
    """
    Image to Text Tool


    Usage:
        clipboard-clipboard:
            Screenshot to clipboard, run script
        ui:
            shortcut, click twice, 

    """
    print("Running custom-ocr...")
    parser = argparse.ArgumentParser(
                    prog='OCR Tool',
                    description='Image to Text',
                    epilog='-h for help')
    
    # Set Modes for Processing
    parser.add_argument('-i', '--input', default="clipboard")
    parser.add_argument('-o', '--output', default="clipboard")
    parser.add_argument('-m', '--mode', default="main", choices=["main", "poll", "test"])
    
    args = parser.parse_args()

    if args.mode:
        if args.mode == "poll":
            poll()
        elif args.mode == "main":
            main(args.input, args.output)
        elif args.mode == "test":
            test()