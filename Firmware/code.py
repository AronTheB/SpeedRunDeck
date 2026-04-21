import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Initialize keyboard
kbd = Keyboard(usb_hid.devices)

# Define physical pins for 3x2 Hackpad
KEY_PINS = [
    board.D7,  # Key 1
    board.D8,  # Key 2
    board.D9,  # Key 3
    board.D10,  # Key 4
    board.D6,  # Key 5
    board.D5,  # Key 6
]

# Keybinds from Configurator
KEYBINDS = [
    [Keycode.F3, Keycode.G],
    [Keycode.F3, Keycode.F],
    [Keycode.SHIFT, Keycode.F3, Keycode.F],
    [Keycode.SHIFT, Keycode.F3],
    [Keycode.J],
    [Keycode.F3, Keycode.C],
]

# Setup Pins
keys = []
for pin in KEY_PINS:
    k = digitalio.DigitalInOut(pin)
    k.direction = digitalio.Direction.INPUT
    k.pull = digitalio.Pull.UP
    keys.append(k)

key_states = [False] * len(keys)

print("Hackpad SpeedrunDeck Ready!")

while True:
    for i, key in enumerate(keys):
        # Button is pressed (False because of Pull.UP)
        if not key.value and not key_states[i]:
            key_states[i] = True
            print("Pressed:", i)
            if i < len(KEYBINDS) and KEYBINDS[i]:
                kbd.press(*KEYBINDS[i])

        # Button is released (True)
        elif key.value and key_states[i]:
            key_states[i] = False
            if i < len(KEYBINDS) and KEYBINDS[i]:
                kbd.release(*KEYBINDS[i])

    time.sleep(0.01)
