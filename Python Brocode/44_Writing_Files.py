#Python writing files (.txt, .json, .csv)
# .json = key value pairs

txt_data = "I like a pizza"

file_path = "output.txt"

#modes     w-> write  x-> write if file does not exist a->append r->read

with open(file = file_path, mode = "w") as file:
    file.write(txt_data)
    print(f"txt file {file_path} has been created")
