def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    if b == 0:
        raise ValueError(
            "Can not divide by Zero"
        )
    return a/b
    

def main():
    a = 10
    b = 5
    print("Python Calulator")
    print("First number:",a)
    print("Second number:",b)
    print("Addition:",add(a,b))
    print("Substraction:",sub(a,b))
    print("Multiplication:",mult(a,b))
    print("Division:",div(a,b))

if __name__ == "__main__":
    main()



    