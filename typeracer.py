import argparse
import re
import time

from bs4 import BeautifulSoup
from pynput.keyboard import Key, Controller
from selenium import webdriver

parser = argparse.ArgumentParser(description='Crush ppl at typeracer.')

parser.add_argument('--friendly-link', nargs=1, help='a link for a friendly match')
args = parser.parse_args()

# Change these if you are playing against a friend
friendly = args.friendly_link is not None

if friendly:
	url = args.friendly_link[0]
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

