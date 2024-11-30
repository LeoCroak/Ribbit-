# original code found on https://github.com/LeoCroak/Ribbit-

word = input("Enter a word:")

for letter in word:
    if letter in "aeiouAEIOU":
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is not a vowel")