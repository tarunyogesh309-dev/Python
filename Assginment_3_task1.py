def fatorial(n):
    fat = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(1, n+1):
            fat = fat * i
    return fat

t = int(input("Enter a number: ")) 
result = fatorial(t)
print("Factorial of ", t, " is: ", result)
