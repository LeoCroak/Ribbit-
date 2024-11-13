# original code found on https://github.com/LeoCroak/Ribbit-

chosenumber = input("Enter a number you want to countdown from:")

while True:
    try:
        chosenumber = int(chosenumber)
        break
    except ValueError:
        chosennumber = input("Enter a valid number you want to countdown from:")

for x in range(chosenumber, 0, -1): 
    print(x)

print("Countdown completed!:")