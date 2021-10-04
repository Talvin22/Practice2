link = input(str())

a = 1
b = 0
#564
for i in link:
    a = a * int(i)
    b = b + int(i)


print('добуток=' + str(a) + ' , сума=' + str(b))
