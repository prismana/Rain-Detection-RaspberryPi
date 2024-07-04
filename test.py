import sys

actual_name = sys.argv[1]
file_path = sys.argv[2]

print("Actual name", actual_name)
print("File  path: ", file_path)

with open(file_path, "r") as file:
    line_1 = file.readline()

print(line_1)