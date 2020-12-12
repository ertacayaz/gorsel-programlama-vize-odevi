adres = "www.alierbey.com"

for i in range(len(adres)) :
    if (adres[i:] == ".com"):
        print("Bu bir adrestir")
        break
    elif (adres[i:] == ".net"):
        print("bu bır adrestir")
        break
    elif (adres[i:] == ".org"):
        print("bu bir adrestir")
        break
    else:
        continue
else :
    print('bu bir adres değil')