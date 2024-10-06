# Program to monitor the temperature and humidity of a room using a DHT22 sensor
# set the variable device = 'pizero' or 'laptop' to determine which device is being used

device = 'pizero'

if device == 'pizero':
    import Adafruit_DHT
    DHT_SENSOR = Adafruit_DHT.DHT22
    DHT_PIN = 4

import time

max_temperature = -100
min_temperature = 100
max_humidity = 0
min_humidity = 100

humidity = 50
temperature = 20

file = open("output.csv", "a")
file.write("humidity, temperature, time\n")

# create infinite loop to monitor temperature and humidity

while True:
    if device == 'pizero':

    if device == 'laptop':
        # create a random number for humidity and temperature within 1 degree of the previous value
        humidity = humidity + (1 - 2 * (time.time() % 2))
        temperature = temperature + (1 - 2 * (time.time() % 2))

    if humidity is not None and temperature is not None:

        # convert temperature to fahrenheit
        temperature = int(temperature * 9/5) + 32

        # record max and min temperature and humidity
        if temperature > max_temperature:
            max_temperature = temperature
        if temperature < min_temperature:
            min_temperature = temperature
        if humidity > max_humidity:
            max_humidity = humidity
        if humidity < min_humidity:
            min_humidity = humidity
    
        # define timedate as current time and date
        timedate = time.asctime(time.localtime(time.time()))

        # format timedate as a timestamp in the format yyyy-mm-dd hh:mm:ss
        timedate = timedate[20:24] + "-" + timedate[4:7] + "-" + timedate[8:10] + " " + timedate[11:19]

        # write data to .csv file with headers
        file.write(str(humidity) + "," + str(temperature) + "," + str(timedate) +"\n")

        # show the current humidity, temperature and timedate in the same place on the screen
        print("   Humidity is: " + str(int(humidity)) + "%" + "   Temperature is: " + str(int(temperature)) + "f    DateTime is: " + str(timedate) + "  Max Temp: " + str(max_temperature) + "   Min Temp: " + str(min_temperature) + "   Max Humidity: " + str(max_humidity) + "   Min Humidity: " + str(min_humidity))
    time.sleep(5)

file.close()