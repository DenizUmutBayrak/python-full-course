#Python file detection

import os

file_path = "stuff/test.txt" #relative

if os.path.exists(file_path):
    print(f"The location {file_path} exist")
else:
    print("The location does not exist")