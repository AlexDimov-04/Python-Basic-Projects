sequence = []


# func for Fibonacci series up to n
def fibonacci_seq(n):
    a, b = 0, 1
    while a < n:
        sequence.append(a)
        a, b = b, a + b


# boundary for the sequence
number = int(input("Enter a number boundary for the Fibonacci sequence!: "))
fibonacci_seq(number)

# checks if the number is in the sequence
num = int(input("Enter a random number: "))
print()
print(*sequence, sep=', ')

if num in sequence:
    print("Your number is in the sequence!")
else:
    print("Your number is not in the sequence!")
