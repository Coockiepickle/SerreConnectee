This git is for a connected greenhouse programmed using an Arduino Uno board and a Raspberry PI.

- temp.ino : Using a temperature sensor, it prints the temperature in the serial monitor

- humidite.ino : For now it generates a random number but it can be changed to use a humidity sensor and it prints the humidity on the serial monitor

- serie.py : This script allows for bi-directional communication between a Python script and an Arduino board over a serial connection, specifically for the purpose of retrieving temperature data from the Arduino and storing it in a JSON file.
