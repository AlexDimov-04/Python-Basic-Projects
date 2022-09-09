degrees = input("Which temperature would you like to convert C->F / F->C? ")

if degrees == "C->F":
    celsius = int(input("Enter a temperature in Celsius: "))
    fahrenheit = 9 / 5 * celsius + 32
    print(f"\n{celsius}° by Celsius is {fahrenheit}° by Fahrenheit!")

elif degrees == "F->C":
    fahrenheit = int(input("Enter a temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"\n{fahrenheit}° by Fahrenheit is {celsius:.2f}° by Celsius!")
