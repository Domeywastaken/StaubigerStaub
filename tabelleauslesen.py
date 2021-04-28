import csv


reader = csv.reader(open("C:/Users/Domi/Documents/Python/2021-04-26_bme280_sensor_42069.csv"), delimiter=";")     
for row in reader:
   print("Zeit:", row[5],"Temperatur:", row[10])     
