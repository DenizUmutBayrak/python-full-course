#Python reading files (.txt, .json, .csv)

#import json  #import csv

file_path = "output.txt" #output.json #output.csv

with open(file_path, "r") as file:
    content = file.read()

    #content = json.load(file)

    #content = csv.reader(file)
    # for line in content:
        #print(line)
    print(content)