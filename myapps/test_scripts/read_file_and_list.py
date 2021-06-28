text_file = "sample.txt"

def read_file_contents(file):
    open_file = open(file) 
    read_file = open_file.read()
    return read_file.splitlines()
#    return read_file

print(read_file_contents(text_file))
