# typeracer-bot
A bot for typeracer, for if you want to go *fast*.

Note: this script does not pass the captcha that occurs for >100wpm speeds.

## Requirements
You need Python to run this script. It has been tested with Python version 3.8.3.

You also need a web browser. It has been tested with Firefox, but it should also be possible to set up with Google Chrome, Microsoft Edge, and Safari.

This was created on Microsoft Windows, and so instructions are for Windows.

## Installation & Use
Clone this repository
```
git clone https://github.com/0x534b/typeracer-bot.git
```

I recommend using a virtual environment to run this project
```
python -m venv <virtual environment directory name>
```

Activate the environment and install required dependencies from `pip`
```
<virtual environment directory name>/Scripts/activate
pip install -r requirements.txt
```

Make sure the proper driver for your web browser is on your `PATH`. These are listed [here](https://selenium-python.readthedocs.io/installation.html). The one used for Firefox specifically can be found [here](https://github.com/mozilla/geckodriver/releases).

You should now be able to run the script by activating the virtual environment and executing it with the Python interpreter
```
<virtual environment directory name>/Scripts/activate
python typeracer.py
```