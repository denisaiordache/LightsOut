# LightsOut

This application is an example of how to build a mock IoT device, simulating a Smart Home Lighting System.

Implemented HTTP REST API resources:

* User profile
* Room
* Light

Implemented MQTT API features:

* Mock movement sensor and internal light switch that turns lights off/on when user moves from one room to another
* Mock internal clock, database checker and light intensity shifter that shift the intensity of the light according to the user's Sleep/Wake-up Hour
### Credits
The MQTT features make use of some of the code from this paho-mqtt tutorial: https://www.emqx.com/en/blog/how-to-use-mqtt-in-python
The External API calls are done using: https://geocoder.readthedocs.io and https://api.sunrise-sunset.org

### OpenAPI specification

You can check out tools that automate the generation of the specification like:
https://openap.is

### Instalation

You should have python3 and pip3 installed.   

1. cd into this project
`cd app`  

2. Install libraries  
`pip install -r requirements.txt`  

3. Make sure that the "RESET_DATABASE_ON_STARTUP" flag in app/config/config.py is set to True  
   
4. Run
`python application.py`  

5. cd into the mqtt folder  
`cd mqtt`  

6. Run each of the following mqtt scripts in their own seperate terminal:  
    -for the movement sensor:  
    `python mock_movement_sensor.py`  
    `python internal_light_switch.py`  
    -for the wake-up/sleep functionalities:  
    `python light_intesity_shifter.py`  
    `python internal_clock.py`  
    `python database_checker.py`  
  
7. cd into the GUI folder  
`cd ..`  
`cd GUI`  

8. Run the GUI  
`python mainApp.py`  

9. cd into the testing folder  
`cd ..`  
`cd tests`  
`cd unit.integration_tests`  

10. Run the tests  
`pytest test_createProfileFrames.py`  
`pytest test_mainApp.py`  
`pytest test_roomsView.py`  
`pytest test_routes.py`  
`pytest test_updateProfile.py`  

### Testing
Using testing tutorial: https://flask.palletsprojects.com/en/2.0.x/ and https://pytest-flask.readthedocs.io/en/latest/#