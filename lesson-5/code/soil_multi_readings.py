import ds18b20_therm as soil_temp
from time import sleep

interval = 5
temp_probe = soil_temp.DS18B20()
y = []


print("Taking 10 readings, one every " + str(interval) + " seconds...")

for i in range(10):
    y.append(temp_probe.read_temp())
    print("Reading " + str(i) )
    sleep(interval)

