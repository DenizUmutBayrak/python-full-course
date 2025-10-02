import json

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}

file_path = "output.json"

try:
    with open(file_path, "w") as file:
        json.dump(employee, file, indent=4) #add 4 space to beginnin    g of the key-word pairs
        print(f"json file saved to {file_path}")
except FileExistsError:
    print(f"json file already exists in {file_path}")