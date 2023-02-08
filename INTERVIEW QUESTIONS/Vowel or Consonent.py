vowel=["a","e","i","o","u","A","E","I","U","O"]
char=input("enter the string:")
for i in char:
    if i in vowel:
        print(f"{i} is vowel")
    else:
        print(f"{i} is consonent")
