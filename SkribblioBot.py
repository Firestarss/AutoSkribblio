import json
import requests
import sys
import os.path
import string
from bs4 import BeautifulSoup

with open("updated_list.json") as json_file:
    words = json.load(json_file)

print(words['10'])
print(words['16'])
print(words['17'])
print(words['18'])
print(words['19'])

"""
main
    give it the link
    open the link in beautiful soup

    Find player id
        1. body ->
        2. div class="container-fluid" ->
        3. div id="screenGame" ->
        4. div class="containerGame" ->
        5. div id="containerPlayerlist" ->
        6. div id="containerGamePlayers" ->
        7. div (save id as playerid) ->
        8. div class="info" ->
        9. div class="name"
            if last 5 chars of name == (You) save the id as your personal player id if not then go back to step7 and move to next sibling (div on same level)

    find what the word is to guess:
        if the word is full of ____ then got to step 1
        if teh word has letters go to step 2

    1. Find length of word trying to get guessed
        timer = body -> div class"container-fluid" -> div id="screenGame" -> div class="gameHeader" -> div class="timer-container" -> div class="timer"
        timer > 0:
            take a guess:
                if the class for div id=playerid is "player guessedWord":
                    break
            timer = body -> div class"container-fluid" -> div id="screenGame" -> div class="gameHeader" -> div class="timer-container" -> div class="timer"

    2. IF the player has to draw
        use google chrome extension to draw
"""
