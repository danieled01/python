temperatures = [10, -20, -289, 100]
def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense"
    else:
        f = c * 9/5 +32
        return f

for item in temperatures:
    with open("test_3007.txt", "a") as myfile:
        if item > -273.15:
            myfile.write(str(c_to_f(item)) + "\n")
        
