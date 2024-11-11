#original code found on https://github.com/LeoCroak/Ribbit-

#imports go below here

#start of the code
unit = input("Fahrenheit or celsius? F or C?")
amount = input("Enter the temperature:")
# collcects user input

#checks if we can convert amount into a number

while True:
    try:
        amount = float(amount)
        break
    except ValueError:
        amount = input("Enter a valid temperature:")

#loops again until a valid value has been entered

if unit.lower() == "c":
    amount = round((9 * amount) / 5 + 32 ,1)
    print(f"The temperature in Fahrenheit is {amount}°F")
elif unit.lower() == "f":
    amount = round((amount - 32) * 5 / 9 ,1)
    print(f"The temperature in Celsius is {amount}°C")
else:
    print("there was a error")

#logic for the calculations