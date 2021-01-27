import ijson as ijson
from bmi_calculator import Calculator

def ijson_reader(filename):
    with open(filename,'r') as f:
        rows = ijson.items(f, 'item')
        for row in rows:
            obj = Calculator(row['WeightKg'], row['HeightCm'])
            print(obj.get_category())
            print(obj.calculate())
        print("Done")

ijson_reader('data.json')