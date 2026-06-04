import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.digitalio import Digitalioscanner

keyboard = KMKKeyboard()

keyboard.matrix = DigitalioScanner(
    pins=(board.D10, board.D9, board.D8, board.D7)
    value_when_pressed=False,
    pull=True
)

keyboard.keymap = [
    [KC.D, KC.E, KC.V, KC.O]
]

if __name__  == '__main__':
    keyboard.go()
