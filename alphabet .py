# taking user input
ch = input("Enter a character: ")
if((ch>='A' and ch<= 'Z') or (ch>='a' and ch<='z')):
    print(ch, "is an Alphabet")
else:
    print(ch, "is not an Alphabet")
