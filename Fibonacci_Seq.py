



import sys
sys.set_int_max_str_digits(0)
while True:
    x = input("Please Enter a Number: ")

    if x.isnumeric():
        x = int(x)
        if x == 0:
            print("Enter a number above zero!!")
        if x > 0:
            ab = int(x)
            break
    print("Please Enter a Valid Number")

###Loop for fibonacci sequence
a = 0
b = 1
while True:
    a = b
    b = a + b
    
    if len(str(a)) == ab:
        print(a)
        break
