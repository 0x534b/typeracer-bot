import argparse
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WAIT_TIME = 60
# SPEED_SCALER = 1.9219219219219221
SPEED_SCALER = 1

parser = argparse.ArgumentParser(description='Crush your opponents at typeracer.')
parser.add_argument('--friendly-link', nargs=1, help='a link for a friendly match')
parser.add_argument('--max-wpm', nargs=1, help='max typing speed: the default 400 words per minute is fairly safe to avoid disqualification')

args = parser.parse_args()

if args.wpm is None:
	wpm = 400
else:
	wpm = args.max_wpm[0]


# Change these if you are playing against a friend
friendly = args.friendly_link is not None

if friendly:
	url = args.friendly_link[0]
else:
	url = "http://play.typeracer.com/"

# Load up the page..
driver = webdriver.Firefox()
driver.get(url)

# find the button on the page to join the race
if friendly:
	# wait up to 15 secs for the start button to load
	elem = WebDriverWait(driver, WAIT_TIME).until(
	EC.presence_of_element_located((By.CLASS_NAME, "raceAgainLink"))
	)
else:
	elem = WebDriverWait(driver, WAIT_TIME).until(
	EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Enter a Typing Race')]"))
	)

# click the button to join the race
elem.click()

# read the text prompt
elems = WebDriverWait(driver, WAIT_TIME).until(
	EC.presence_of_all_elements_located((By.XPATH, '//span[@unselectable="on"]'))
	)

texts = [span.text for span in elems]

# deal with the possibility that the first word is one letter
if len(texts) == 3:
	texts = [texts[0] + texts[1]] + texts[2:]

# the first letter + the rest of the first word + the rest of the text
string = ' '.join(texts)

# wait up to 20 secs for the race to start
WebDriverWait(driver, WAIT_TIME).until(EC.invisibility_of_element((By.CLASS_NAME, "countdownPopup")))

# select the text input field
elem = driver.find_element(by=By.CLASS_NAME, value="txtInput")
elem.click()

speed = int(wpm) * SPEED_SCALER
delta = (1/speed * 60)

old_time = time.time()

for word in string.split(' '):
	elem.send_keys(word + ' ')
	while 1:
		new_time = time.time()
		if new_time - old_time >= delta:
			break
	old_time = new_time

