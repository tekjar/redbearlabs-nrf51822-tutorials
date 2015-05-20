# nrf51822-tutorials


######build.py

Helps to easily build your projects and combine it with softdevice hex files

e.g 

**python build.py examples/ble_peripheral/ble_app_hrs** --> Builds the hrs example in the sdk. uses s110 by default

**python build.py -s s120 examples/ble_peripheral/ble_app_hrs -o hrs_full.hex**

