import keyboard


def new_event(event : keyboard.KeyboardEvent) -> None :
    print(f"hi{event.name} - {event.event_type}")

keyboard.on_release(callback=new_event)
keyboard.wait()