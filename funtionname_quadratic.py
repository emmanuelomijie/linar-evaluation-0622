def quadratic(a, b, c) :
    print(" input the coorfficient of the first term value")
    a = float(input())
    print("input the coorfficient of the second term value")
    b = float(input())
    print("input the coorfficient of the third term value")
    c = float(input())
    A = a
    B = b
    C = c
    determinant = (b**2) - (4*a*c)
    determinant = determinant**0.5
    root1answer = float(-b) + determinant
    root2answer = float(+b) + determinant   
    denominator = 2 * a 
    firstfinalanswer = root1answer / denominator
    secondfinalanswer = root2answer / denominator
    print("The root of your quadratic equation is " + str(firstfinalanswer),", " + str(secondfinalanswer))
    #return firstfinalanswer, secondfinalanswer
quadratic("A", "B", "C")