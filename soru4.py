a = 0

for i in range(100,999):
    x = str(i)[0]
    y = str(i)[1]
    z = str(i)[2]

    if x !=y and x!= z and y != z:
        print(i)
        a += 1

print("Toplam: {}".format(str(a)))
