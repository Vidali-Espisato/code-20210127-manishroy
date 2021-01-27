import csv
import ijson as ijson
from bmi_calculator import Calculator

def ijson_reader(filename, out_file):
    with open(filename,'r') as f:
        with open(out_file, 'a') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            rows = ijson.items(f, 'item')
            for row in rows:
                obj = Calculator(row['WeightKg'], row['HeightCm'])
                csv_writer.writerow([row['Gender'], f"{row['WeightKg']} kg", f"{row['HeightCm']} cm | {obj.height} m", obj.bmi, obj.category, obj.risk])
