import json
import pyautogui
import time

with open("updated_list.json") as json_file:
    words = json.load(json_file)

in_str = "1234567890"
spaces = str(len(in_str))

time.sleep(4)

count = 0
for word in words[spaces]:
    count += 1
    pyautogui.typewrite(word + '\n')
    if count == 4:
        time.sleep(2.25)
        count = 0