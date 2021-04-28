import csv
from pathlib import Path

data_folder = Path("StaubigerStaub")

file_to_open = data_folder / "20210426bme280sensor42069.csv" 



reader = csv.reader(open(file_to_open), delimiter=";")     
for row in reader:
   print("Zeit:", row[5],"Temperatur:", row[10])     
