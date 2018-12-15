ch = input("Enter Any Character: ")

if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    print("Entered Character ({0}) is an Alphabet".format(ch))

else:
    print("Entered Character", ch, "is not an Alphabet")
