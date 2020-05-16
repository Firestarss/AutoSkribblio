import json
import requests
import sys
import os.path
import string
from bs4 import BeautifulSoup

def main(args=sys.argv):
    link = args[1]
    info = BeautifulSoup(requests.get(link).text, 'html.parser')

    """
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
    """
    # playerid = info.body.div.next_sibling.next_sibling.find(id="screenGame").div.next_sibling.find(id="containerPlayerlist").find(id="containerGamePlayers").div.id
    # print(playerid)
    #
    # word = info.body.div.next_sibling.next_sibling.find(id="ScreenGame").div.find(id="currentWord")
    #print(word)
    #create list of word
    """
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
    """

    time = info.body.div.next_sibling.next_sibling.find(id="screenGame").div.div.find(id="timer")

    print(time)
    # playerClass = info.body.div.next_sibling.next_sibling.find(id="ScreenGame").div.next_sibling.find(id="containerPlayerlist").find(id="containerGamePlayers").find(id=playerid)['class']
    # print(playerClass)
    # while time < 0:
    #     newword = info.body.div.next_sibling.next_sibling.find(id="ScreenGame").div.find(id="currentWord")
    #     if word != newword:
    #         word = newword
    #         #create new list of words
    #     guessSingleWord()
    #     info = BeautifulSoup(requests.get(link).text, 'html.parser')
    #     playerClass = info.body.div.next_sibling.next_sibling.find(id="ScreenGame").div.next_sibling.find(id="containerPlayerlist").find(id="containerGamePlayers").find(id=playerid)['class']
    #     if playerClass == "player guessedWord":
    #         break
    #     time = info.body.div.next_sibling.next_sibling.find(id="ScreenGame").div.div.find(id="timer")

    """
    2. IF the player has to draw
        use google chrome extension to draw
    """

if __name__ == "__main__":
    main()
