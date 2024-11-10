# original code found on https://github.com/LeoCroak/Ribbit-

# converts grams into kg and tons

chosenvalue = input("Enter a value of grams, kilograms, or tons:")
chosennumber = input("Enter your number:")
 
while True:
    try:
        chosennumber = float(chosennumber)
        break
    except ValueError:
        chosennumber = input("Please enter a valid number:")

if chosenvalue.lower() == "grams":
    print(f"{chosennumber}g in kilograms is {chosennumber / 1000} kg and in tons is {chosennumber / 1_000_000} T")
elif chosenvalue.lower() == "kilograms":
    print(f"{chosennumber}kg in grams is {chosennumber * 1000} g and in tons is {chosennumber / 1000} T")
elif chosenvalue.lower() == "tons":
    print(f"{chosennumber}T in grams is {chosennumber * 1_000_000} g and in kilograms is {chosennumber * 1000} kg")
else:
    print("There was an error")