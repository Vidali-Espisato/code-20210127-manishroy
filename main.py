from json_reader import ijson_reader


if __name__=="__main__":
    output_file = "output.csv"
    input_file = "data.json"
    try:
        open(output_file)
    except:
        open(output_file, 'w').write("Gender, Weight, Height(cm | m), BMI, Category, Risk\n")
    ijson_reader(input_file, output_file)
