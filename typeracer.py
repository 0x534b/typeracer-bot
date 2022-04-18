import re
import time

from bs4 import BeautifulSoup
from pynput.keyboard import Key, Controller
from selenium import webdriver

# Change these if you are playing against a friend
friendly = False
friendly_url = ""

if friendly:
	url = friendly_url
else:
	url = "http://play.typeracer.com/"

string = ""
keyboard = Controller()

# Load up the page..
driver = webdriver.Firefox()
driver.get(url)

# Wait for the page to load
time.sleep(5)

# Press shortcut for new race
keyboard.press(Key.ctrl)
keyboard.press(Key.alt)

if friendly:
	keyboard.press('k')
else:
	keyboard.press('i')

# Release pressed keys
keyboard.release(Key.ctrl)
keyboard.release(Key.alt)

if friendly:
	keyboard.release('k')
else:
	keyboard.release('i')

# Wait for the race to start
time.sleep(15)

# Read the html
html = driver.page_source
soup = BeautifulSoup(html, features="html.parser")

# Find the text within the html
for span in soup.find_all("span", unselectable="on"):
    string += span.text

# Loop through typing each character at a time with a delay
for char in string:
	keyboard.press(char)
	keyboard.release(char)
	time.sleep(0.018)

