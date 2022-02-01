# LightsOut
An app for a smart-home lighting system


# Functionalities:
- MQTT: There is a mqtt system set up so that it simulates user movement across rooms and turns lights off/on accordingly
[mock_movement_sensor.py, internal_light_switch.py]
- GUI: The user can create and update his profile
- GUI: The user can add rooms to his profile and manage them
- GUI: The user can customize the lighting in each room
- wake-up/sleep functionality: The user can set a wake-up/sleep hour and the lights will dim/ brighten at that hour
[in mqtt (restul fata de ce am mentionat mai sus)]
- User can choose to set wake-up-hour and sleep-hour through his location (prelucrare de date reale)
[dateloc.py si GUI]