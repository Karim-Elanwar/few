from random import randint
order = [
    "first",
    "second",
    "third"
]

for a in range(3):
    print("Enter your", order[a], "word:")
    word = input()
    order[a] = word

for b in order:
    new = b
    if "a" in b:
        new = new.replace("a", chr(randint(33, 37)))
    if "e" in b:
        new = new.replace("e", chr(randint(38, 42)))

    
