from pynput.keyboard import Key
from pynput.keyboard import Controller as KeyboardController
import pynput.keyboard as keyboard
from pyautogui import press, typewrite, hotkey
import keyboard as yeeboard


# Set the global hotkey to something arbitrary
# ! Starts and stops the script
GLOBAL_HOTKEY   = keyboard.HotKey.parse('<ctrl>+<alt>+i')
GLOBAL_STOP_KEY = keyboard.Key.esc
# ! Size 4
BUFFER = '    '

from time import sleep
sleep(1)

ime_dictionary = {
    'pepv': 'vc? :widepeepo_0::widepeepo_1::widepeepo_2::widepeepo_3::widepeepo_4::widepeepo_5::widepeepo_6::widepeepo_7:\n\
:widepeepo_0::widepeepo_1::widepeepo_2::widepeepo_3::widepeepo_4::widepeepo_5::widepeepo_6::widepeepo_7: vc?\n\
'
}

# Types text with pynput controlling the keyboard XD
def type_text(s):
    yeeboard.write(s)
    print(f'We should be printing {s}')


# Queues the key pressed
def buffer_key(key, buffer):
    if len(str(key)) == 3:
        return f"{buffer[1:4]}{str(key)[1]}"
    else:
        return '    '


def ime():
    global ime_dictionary
    global BUFFER

    for key in ime_dictionary:
        print(f'\n\n{key}\n\n')
        if key in BUFFER:
            print('YEE IN HAW YEE IN HAW')
            # If you found one, backspace
            count = 0
            while count < len(key):
                press('backspace')
                count += 1
            type_text(ime_dictionary[key])
            BUFFER = '    '
        
        
# Log and take action if any
def on_press(key):
    global BUFFER
    try:
        print(f"THE KEY IS {key}")
        # Add the key to the buffer
        BUFFER = buffer_key(key, BUFFER)
        print(f"THE BUFFER IS '{BUFFER}'")
        # Run it through our ime
        ime()
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


# Log and take action if any
def on_release(key):
    global BUFFER
    print('{0} released'.format(
        key))
    print(BUFFER)
    if key == GLOBAL_STOP_KEY:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(
    on_press  = on_press,
    on_release= on_release
    ) as listener:
        listener.join()
