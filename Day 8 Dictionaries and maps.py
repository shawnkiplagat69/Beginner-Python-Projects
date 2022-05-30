n=int(input())
#prompt the user for the number of entries, n, for the phonebook
phonebook={}
#contact=[]
for i in range(n):
    contact=input().split()
    phonebook[contact[0]]=contact[1]

while True:
    try:
        inpt = input()
        if inpt in phonebook:
            print(inpt+"="+phonebook[inpt])
        else:
            print("Not found")
    except EOFError:
        break
