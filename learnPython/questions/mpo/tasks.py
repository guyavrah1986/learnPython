import threading
import time
import getch

from sshkeyboard import listen_keyboard
import keyboard


def word_call_back(word: str):
    print("the word:" + word + " was inserted")


if __name__ == "__main__":
    print("main - start")
    word_to_capture = "abc"
    keyboard.add_word_listener(word_to_capture, word_call_back, triggers=['space'], match_suffix=False, timeout=2)
    while True:
        print("while True")

    print("main - end")