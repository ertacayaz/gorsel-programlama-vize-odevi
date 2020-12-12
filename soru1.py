eposta = "ali.erbey@usak.edu.tr"

for i in  eposta:
    if ( i == "@" ):
        print("bu bir eposta adresidir")
        break
else:
    print("bu bir eposta adresi değildir ")