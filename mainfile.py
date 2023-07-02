import pyautogui, time
noOfOptions = int(input("How many options are there?"))
print(noOfOptions)
time.sleep(5)
import string
import random
mainName = ""
def namemaker():
    global mainName
    listOfAlpha = list(string.ascii_lowercase)
    randLetters = random.choices(listOfAlpha, k=7)
    for i in range(len(randLetters)):
         mainName = mainName + randLetters[i]
    print(f"name changed to: {mainName}")

while True:
    namemaker()
    if noOfOptions == 5:
        pyautogui.moveTo(818, 510)
        time.sleep(0.1)
        pyautogui.click(button='right')
        time.sleep(0.1)
        pyautogui.moveTo(866, 659)
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.typewrite(mainName)
        pyautogui.press('enter')
        mainName=""
    if noOfOptions == 4:
        pyautogui.moveTo(818, 510)
        time.sleep(0.1)
        pyautogui.click(button='right')
        time.sleep(0.1)
        pyautogui.moveTo(884, 633)
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.typewrite(mainName)
        pyautogui.press('enter')
        mainName = ""




