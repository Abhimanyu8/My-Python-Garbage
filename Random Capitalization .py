from random import choice

sentence= input("lines to be made fun of : ")

print(''.join(choice((str.upper,str.lower))(c) for c in sentence))

