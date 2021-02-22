import time
import click
from tkinter import Tk
from pynput.keyboard import Controller, Key
import random

@click.command()
@click.option('--clipboard', '-c', is_flag=True,
help="Use first clipboard value as input instead of a file.")
@click.option('--delay', '-d', default=5, 
help="How long to wait before I start typing.", show_default=True)
@click.option('--file', '-f', type=click.Path(exists=True),
help="Input file.")
@click.option('--speed', '-s', default=-1.0,
help="How fast should I type. -1 gives random speed between 50ms and 100ms. Using 0 can freeze websites.", show_default=True)
def main(clipboard, delay, file, speed):

    """Simple automated typing cli, for working with files and clipboard."""

    keyboard = Controller()
    time.sleep(delay)
    _input = ""

    if clipboard:
        _input = Tk().clipboard_get()
    else:
        try:
            _input = open(file, "r").read()
        except OSError:
            click.FileError(file)

    for c in _input:
        if speed == -1:
            time.sleep(random.uniform(0.05, 0.1))
        else:
            time.sleep(speed)
        if c == "\n":
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        else:
            keyboard.press(c)
            keyboard.release(c)

if __name__ == "__main__":
    main()

