isim = "Usak Universtesi"
ara = "ver"

if isim.find(ara) > -1:
    x = isim.find(ara ) - 1
    y = isim.find(ara) + len(ara) + 1

    print(isim[x:y])