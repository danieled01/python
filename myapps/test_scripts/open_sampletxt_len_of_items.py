file = "sample.txt"
open_file = open(file)
read_file = open_file.read()

for item in read_file.splitlines():
    print(len(item))
