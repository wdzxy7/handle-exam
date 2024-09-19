import os
import pyautogui
import keyboard
import requests
from matplotlib import pyplot as plt

url = "http://xxxxx:8080/get_code"

savefolder = './filesfolder'


def get_shot():
    mouse_x, mouse_y = pyautogui.position()

    screen_width, screen_height = pyautogui.size()
    width = screen_width - mouse_x
    height = screen_height - mouse_y

    if mouse_x + width > screen_width:
        width = screen_width - mouse_x
    else:
        width = screen_width - mouse_x

    if mouse_y + height > screen_height:
        height = screen_height - mouse_y
    else:
        height = screen_height - mouse_y

    width = max(0, width)
    height = max(0, height - 53)

    screenshot = pyautogui.screenshot(region=(mouse_x, mouse_y, width, height)) # x,y,w,h
    return screenshot

def get_screen_and_rquest_llm():
    print('start screenshot !')
    img = get_shot()
    # plt.imshow(img)
    # plt.show()
    img_save_path = os.path.join(savefolder, 'screenshot.png')
    img.save(img_save_path)
    files={'input_file': open(img_save_path,'rb')}
    response = requests.request("POST", url, files=files)
    if response.json()['msg'] == 'success':
        print('please see the computer2 screen and get code !')
    else:
        print('please "Shift+Z" get new img or use "Shift+R" get code again !')

## don't screenshot, continue ocr the old picture
def get_code_again():
    img_save_path = os.path.join(savefolder, 'screenshot.png')
    files={'input_file': open(img_save_path,'rb')}
    response = requests.request("POST", url, files=files)
    if response.json()['msg'] == 'success':
        print('please see the computer2 screen and get code !')
    else:
        print('please "Shift+Z" get new img or use "Shift+R" get code again !')


keyboard.add_hotkey('Shift+Z', get_screen_and_rquest_llm)
keyboard.add_hotkey('Shift+X', get_code_again)


# 进入监听状态
try:
    keyboard.wait('ctrl+b')
except KeyboardInterrupt:
    pass