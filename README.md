# 43300 FINAL PROJECT

## INSTALL

- Run `pip install .`.

### PREREQUISITES

- Sensor requires GPIO support.
- Host machine must be running a MySQL instance. (`sudo apt-get install mysql-server`)
    - (It is recommended you create a db_creator user)
- Python Module requirements listed in [requirements.txt](requirements.txt)

## RUNNING

### DATABASE (Run this on your machine __first!__)

- Run `python3 -m sensornetwork.db init` to build the database.
- If needed, run `python3 -m sensornetwork.db drop` to remove the database.

### HOST MACHINE (That's you!)

- Run `python3 -m sensornetwork.host`.

### SENSOR (Run this on the Raspberry Pi.)

- Run `python3 -m sensornetwork.sensor`.

### WEB SERVER (Also you!)

- Run `python3 -m sensornetwork.web`.

## AUTHORS

- Willow Ciesialka
- Isaiah Victor