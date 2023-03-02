import pyautogui
import pytesseract as tess
from PIL import Image, ImageGrab
import time
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print("Running the Application in 5 Seconds!")
time.sleep(5)
print("Application Started")
image = ImageGrab.grab()
image = image.crop((15,260,1250,400))
text = tess.image_to_string(image)
text = text.replace("\n"," ")
text = list(text)
if text[0]!="l":
    pyautogui.write(text[0])
text = text[1:]
for i in text:
    pyautogui.write(i)
while True:
    image = ImageGrab.grab()
    image = image.crop((15,315,1250,400))
    text = tess.image_to_string(image)
    for i in text:
        if i!="\n":
            pyautogui.write(i)
        else:
            pyautogui.write(" ")