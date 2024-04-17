def fibonacci():

    #Initialization of variable x and y to represent the current and next Fibonacci numbers.
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

userNum = int(input("Kindly input the fibonacci numbers you want to generate: "))

fibo = fibonacci()

#Iterate over the user number
for num in range(userNum): 
    print(next(fibo), end=" ")
